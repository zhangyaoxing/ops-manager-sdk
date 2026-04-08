from typing import Any, Optional
from pathlib import Path
import os
import json
from datetime import datetime, timedelta, timezone
import xml.etree.ElementTree as ET
import httpx
from loguru import logger
from playwright.sync_api import Locator, sync_playwright


SITEMAP_URL: str = "https://www.mongodb.com/docs/ops-manager/current/sitemap-0.xml"
API_BASE_URL: str = "https://www.mongodb.com/docs/ops-manager/current/reference/api/"
HOME_DIR: Path = Path.home() / ".ops_manager_sdk"
EXPIRE_DAYS: int = 7


def get_html_text(http_url: str) -> str:
    """Fetches the HTML content of the given URL.
    Args:
        http_url: The URL to fetch.
    Returns:
        The HTML content as a string.
    """
    response = httpx.get(http_url)
    response.raise_for_status()
    logger.debug("Fetched URL: %s", http_url)
    return response.text


def get_sitemap_urls() -> list[str]:
    """Parses the XML sitemap and extracts the URLs.
    Returns:
        A list of URLs found in the sitemap.
    """
    text = get_html_text(SITEMAP_URL)
    root = ET.fromstring(text)
    namespace: str = root.tag.split("}")[0].strip("{")
    ns = {"ns": namespace}
    api_urls: list[str] = []
    for url_node in root.findall("ns:url", namespaces=ns):
        loc_node = url_node.find("ns:loc", namespaces=ns)
        if loc_node is not None and loc_node.text is not None:
            loc: str = loc_node.text
            if loc.startswith(API_BASE_URL) and not "nav" in loc:
                api_urls.append(loc)
                logger.debug(f"Found API URL: {loc}")
    logger.info(f"Total API URLs found: {len(api_urls)}")
    return api_urls


LOCATORS = {
    # Title is unique per API.
    "title": "xpath=(//h1)[1]",
    # There can be more than one resources per API.
    "resource": "xpath=(//h2[text()='Resource'])[1]/following-sibling::div//td",
    # There can be more than one path/query/body parameters per API.
    "path_params": "xpath=(//h3[text()='Request Path Parameters'])[1]/following-sibling::div[1]/table[1]/tbody[1]/tr",
    "query_params": "xpath=(//h3[text()='Request Query Parameters'])[1]/following-sibling::div[1]/table[1]/tbody[1]/tr",
    "body_params": "xpath=(//h3[text()='Request Body Parameters'])[1]/following-sibling::div[1]/table[1]/tbody[1]/tr",
    "api_path": "xpath=//div[@class='body']/div[1]//a[contains(@href, '/reference/api/')]",
    "category_page": "xpath=//h2[contains(text(), 'Endpoints')]",
}


def extract_apis() -> dict[str, list]:
    """Fetches the HTML content of the given URLs using Playwright.
    Extract API endpoint and parameters from the HTML content.
    The API URLs are obtained from the sitemap.
    Returns:
        A dictionary containing the API endpoint and parameters.
    """
    is_debug: bool = os.getenv("LOG_LEVEL", "INFO").upper() == "DEBUG"
    # Check if the API document was crawled recently (within the last 7 days).
    HOME_DIR.mkdir(parents=True, exist_ok=True)
    output_file = HOME_DIR / "api_docs.json"
    if output_file.exists():
        output_file_time = datetime.fromtimestamp(output_file.stat().st_mtime, tz=timezone.utc)
        if datetime.now(timezone.utc) - output_file_time < timedelta(days=EXPIRE_DAYS):
            logger.info(f"API documentation already exists at {output_file}. Loading from file.")
            with output_file.open("r", encoding="utf-8") as f:
                return json.load(f)
        else:
            logger.info(f"API documentation at {output_file} is expired. Re-crawling.")
            output_file.unlink()

    with sync_playwright() as p:
        logger.info("Starting API documentation extraction...")
        browser = p.chromium.launch(headless=not is_debug)
        context = browser.new_context()
        api_docs: dict[str, list] = {}
        urls = get_sitemap_urls()

        def get_params(params_locator: Locator, **kwargs) -> list[dict[str, Any]]:
            required_override = kwargs.get("required_override", None)
            params: list[dict[str, Any]] = []
            locators: list = params_locator.all()
            for param in locators:
                param_name: str = param.locator("xpath=./td[1]").inner_text()
                param_type: str = param.locator("xpath=./td[2]").inner_text()
                if required_override is not None:
                    required: str = required_override
                else:
                    required_locator = param.locator("xpath=./td[3]")
                    if required_locator.count() > 0:
                        required = required_locator.inner_text()
                    else:
                        required = "Optional"
                default_locator = param.locator("xpath=./td[5]")
                if default_locator.count() > 0:
                    default_value: Optional[str] = default_locator.inner_text()
                else:
                    default_value = None
                params.append(
                    {
                        "name": param_name,
                        "type": param_type,
                        "required": required,
                        "default": default_value,
                    }
                )
            return params

        for index, url in enumerate(urls):
            page = context.new_page()
            page.goto(url, wait_until="domcontentloaded")
            processed = index + 1
            if processed % 10 == 0:
                logger.info(f"Processed APIs: {processed}/{len(urls)}")
            category = page.locator(LOCATORS["category_page"])
            if category.count() > 0:
                logger.info(f"Skipping category page: {url}")
                page.close()
                continue
            title: str = page.locator(LOCATORS["title"]).inner_text()
            resources: list[str] = page.locator(LOCATORS["resource"]).all_inner_texts()
            # All path parameters are required. Sometimes the document misses the "Required" column.
            path_params: list[dict[str, Any]] = get_params(
                page.locator(LOCATORS["path_params"]), required_override="Required"
            )
            query_params: list[dict[str, Any]] = get_params(page.locator(LOCATORS["query_params"]))
            body_params: list[dict[str, Any]] = get_params(page.locator(LOCATORS["body_params"]))
            category_locator: Locator = page.locator(LOCATORS["api_path"])
            if category_locator.count() == 0:
                category_name: str = "Root"
            else:
                category_name = category_locator.last.inner_text().title().replace(" ", "")
            if category_name not in api_docs:
                api_docs[category_name] = []
            api_docs[category_name].append(
                {
                    "title": title,
                    "resources": resources,
                    "path_params": path_params,
                    "query_params": query_params,
                    "body_params": body_params,
                    "capture_time": datetime.now(timezone.utc).isoformat(),
                }
            )
            page.close()
            if is_debug and index >= 10:
                break
        browser.close()
        with output_file.open("w", encoding="utf-8") as f:
            indent: Optional[int] = 4 if is_debug else None
            json.dump(api_docs, f, ensure_ascii=False, indent=indent)
        return api_docs
