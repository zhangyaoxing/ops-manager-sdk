from typing import Any, Optional
from pathlib import Path
import os
import json
from datetime import datetime, timezone
import xml.etree.ElementTree as ET
import httpx
from loguru import logger

from ops_manager_sdk.generator.crawler_factory import CrawlerFactory


SITEMAP_URL: str = "https://www.mongodb.com/docs/ops-manager/current/sitemap-0.xml"
API_BASE_URL: str = "https://www.mongodb.com/docs/ops-manager/current/reference/api/"
HOME_DIR: Path = Path.home() / ".ops_manager_sdk"
EXPIRE_DAYS: int = 7


def get_sitemap_urls() -> list[str]:
    """Parses the XML sitemap and extracts the URLs.
    Returns:
        A list of URLs found in the sitemap.
    """
    logger.info(f"Fetching sitemap from: {SITEMAP_URL}")
    response = httpx.get(SITEMAP_URL)
    response.raise_for_status()
    text = response.text
    root = ET.fromstring(text)
    namespace: str = root.tag.split("}")[0].strip("{")
    ns = {"ns": namespace}
    api_urls: list[str] = []
    for url_node in root.findall("ns:url", namespaces=ns):
        loc_node = url_node.find("ns:loc", namespaces=ns)
        if loc_node is not None and loc_node.text is not None:
            loc: str = loc_node.text
            if loc.startswith(API_BASE_URL) and "nav" not in loc:
                api_urls.append(loc)
                logger.debug(f"Found API URL: {loc}")
    logger.info(f"Total API URLs found: {len(api_urls)}")
    return api_urls


def _extract_expired_docs(api_docs: dict[str, list[dict[str, Any]]]) -> list[str]:
    """Extracts the URLs of API documentation that were:
        - captured more than `EXPIRE_DAYS` ago.
        - returned a 403 or 401 status code.
    Args:
        api_docs: A dictionary containing the API documentation categorized by resource.
    Returns:
        A list of URLs for the API documentation that need to be recrawled.
    """
    recrawl_urls: list[str] = []
    now = datetime.now(timezone.utc)
    for _, apis in api_docs.items():
        for api in apis:
            status: Optional[int] = api["status"]
            capture_time_str: str = api["capture_time"]
            capture_time = datetime.fromisoformat(capture_time_str)
            if (
                status is None
                or status < 200
                or status >= 300
                or (now - capture_time).days >= EXPIRE_DAYS
            ):
                recrawl_urls.append(api["doc_url"])
        # remove recrawled URLs from the existing docs to avoid duplication
        apis[:] = [api for api in apis if api["doc_url"] not in recrawl_urls]

    return recrawl_urls


def extract_apis(urls: list[str]) -> dict[str, list]:
    """Fetches the HTML content of the given URLs using Playwright.
    Extract API endpoint and parameters from the HTML content.
    The API URLs are obtained from the sitemap.
    Returns:
        A dictionary containing the API endpoint and parameters.
    """
    is_debug: bool = os.getenv("ENV", "INFO").upper() == "DEVELOPMENT"
    # Check if the API document was crawled recently (within the last 7 days).
    HOME_DIR.mkdir(parents=True, exist_ok=True)
    output_file = HOME_DIR / "api_docs.json"
    api_docs: dict[str, list] = {}
    if output_file.exists() and not is_debug:
        logger.info(f"API documentation already exists at {output_file}. Loading from file.")
        with output_file.open("r", encoding="utf-8") as f:
            api_docs = json.load(f)
            logger.info(
                "Looking for URLs that need to be recrawled due to expiration or access issues..."
            )
            urls = _extract_expired_docs(api_docs)
            if len(urls) == 0:
                logger.info("No API documentation needs to be recrawled. Skipping crawling.")
                return api_docs
            logger.info(f"Found {len(urls)} API documentation to recrawl. Recrawling...")

    CrawlerFactory.initiate_crawler()
    for index, url in enumerate(urls):
        count = index + 1
        resource, api_doc = CrawlerFactory.crawl(url)
        if resource is None or api_doc is None:
            continue
        if resource not in api_docs:
            api_docs[resource] = []
        api_docs[resource].append(api_doc)
        if count % 10 == 0:
            logger.info(f"{count}/{len(urls)} URLs processed.")
            if is_debug:
                break
    CrawlerFactory.close()

    with output_file.open("w", encoding="utf-8") as f:
        indent: Optional[int] = 4 if is_debug else None
        json.dump(api_docs, f, ensure_ascii=False, indent=indent)
    return api_docs


def type_mapping(type_str: str) -> Any:
    """Map the type string from documentation to a Python type hint."""
    type_str = type_str.lower()
    mapping = {
        "string": "str",
        "integer": "int",
        "long": "int",
        "number": "float",
        "boolean": "bool",
        "object": "dict",
        "timestamp": "datetime",
        "array of strings": "list[str]",
        "string array": "list[str]",
        "array of objects": "list[dict]",
        "object array": "list[dict]",
        "array": "list[Any]",
        "date field": "datetime",
    }
    return mapping.get(type_str, "Any")


def parse_value(value_str: str, type_str: str) -> Any:
    """Parse the string value to the appropriate Python type."""
    if value_str is None:
        return None
    if type_str == "int":
        return int(value_str)
    elif type_str == "float":
        return float(value_str)
    elif type_str == "bool":
        return value_str.lower() == "true"
    elif type_str == "str":
        return value_str
    else:
        return value_str
