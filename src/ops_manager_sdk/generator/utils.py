from typing import Any, Optional
from pathlib import Path
from importlib.metadata import version as distribution_version
import os
import json
from datetime import datetime, timezone
import xml.etree.ElementTree as ET

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10 ships no tomllib in the standard library.
    import tomli as tomllib

import httpx
from dotenv import load_dotenv
from loguru import logger

from ops_manager_sdk.generator.crawler_factory import CrawlerFactory
from ops_manager_sdk.generator.version import Version


PROJECT_ROOT: Path = Path(__file__).resolve().parents[3]


def _load_env_file() -> Optional[Path]:
    """Load configuration variables from a .env file.
    The project root .env is preferred, the current working directory is used as a
    fallback for installations outside the source tree. Variables that are already
    exported in the environment are never overridden.
    Returns:
        The path of the loaded .env file, or None when no file was found.
    """
    for candidate in (PROJECT_ROOT / ".env", Path.cwd() / ".env"):
        if candidate.is_file():
            load_dotenv(candidate, override=False)
            return candidate
    return None


ENV_FILE: Optional[Path] = _load_env_file()


def _read_project_version() -> str:
    """Read the version declared in the project's pyproject.toml.
    The installed distribution metadata is used as a fallback, so the version can
    still be resolved when the source tree is not available.
    Returns:
        The version string, for example "8.0.0".
    """
    pyproject_file: Path = PROJECT_ROOT / "pyproject.toml"
    if pyproject_file.is_file():
        with pyproject_file.open("rb") as file:
            declared_version = tomllib.load(file).get("project", {}).get("version")
        if declared_version is not None:
            return str(declared_version)
    return distribution_version("ops-manager-sdk-generator")


PROJECT_VERSION: Version = Version.parse(_read_project_version())
# The documentation is versioned by major and minor only, for example "v8.0".
DOCS_VERSION: str = f"v{PROJECT_VERSION.major_version}.{PROJECT_VERSION.minor_version}"


def _get_int_env(name: str, default: int) -> int:
    """Read an integer configuration variable, falling back to the default value."""
    raw_value: Optional[str] = os.getenv(name)
    if raw_value is None or raw_value.strip() == "":
        return default
    try:
        return int(raw_value)
    except ValueError:
        logger.warning(f"Invalid value for {name}: {raw_value!r}. Using default: {default}")
        return default


# Configuration variables are read from .env or from exported environment variables.
# The default values are the ones that used to be hard-coded in this module. The
# documentation URLs follow the project version declared in pyproject.toml.
SITEMAP_URL: str = os.getenv(
    "SITEMAP_URL", f"https://www.mongodb.com/docs/ops-manager/{DOCS_VERSION}/sitemap-0.xml"
)
API_BASE_URL: str = os.getenv(
    "API_BASE_URL", f"https://www.mongodb.com/docs/ops-manager/{DOCS_VERSION}/reference/api/"
)
# A relative HOME_DIR is resolved against the working directory the command starts in.
HOME_DIR: Path = Path(os.getenv("HOME_DIR", str(Path.cwd() / ".data"))).expanduser().absolute()
EXPIRE_DAYS: int = _get_int_env("EXPIRE_DAYS", 7)


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
    return sorted(api_urls)


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

    return sorted(recrawl_urls)


def extract_apis(urls: list[str]) -> dict[str, list]:
    """Fetches the HTML content of the given URLs using Playwright.
    Extract API endpoint and parameters from the HTML content.
    The API URLs are obtained from the sitemap.
    Returns:
        A dictionary containing the API endpoint and parameters.
    """
    is_debug: bool = os.getenv("ENV", "INFO").upper() == "DEVELOPMENT"
    force_crawl: bool = os.getenv("FORCE_CRAWL", "0").lower() in {"1", "true", "yes"}
    # Check if the API document was crawled recently (within the last 7 days).
    HOME_DIR.mkdir(parents=True, exist_ok=True)
    output_file = HOME_DIR / "api_docs.json"
    api_docs: dict[str, list] = {}
    if output_file.exists() and not is_debug and not force_crawl:
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
    processed_count = 0
    for index, url in enumerate(urls):
        count = index + 1
        processed_count = count
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
    if processed_count == len(urls):
        logger.info(f"{processed_count}/{len(urls)} URLs processed. All pages crawled.")
    else:
        logger.info(
            f"{processed_count}/{len(urls)} URLs processed. "
            "Crawling stopped before all pages were crawled."
        )
    CrawlerFactory.close()

    with output_file.open("w", encoding="utf-8") as f:
        indent: Optional[int] = 4
        json.dump(api_docs, f, ensure_ascii=False, indent=indent)
    return api_docs


def type_mapping(type_str: str) -> str:
    """Map the type string from documentation to a Python type hint."""
    type_str = type_str.lower()
    mapping = {
        "string": "str",
        "integer": "int",
        "long": "int",
        "number": "int",
        "boolean": "bool",
        "object": "dict",
        "timestamp": "str",
        "array of strings": "list[str]",
        "string array": "list[str]",
        "array of objects": "list[dict]",
        "object array": "list[dict]",
        "array": "list[Any]",
        "date field": "str",
    }
    return mapping.get(type_str, "Any")


def parse_value(value_str: Optional[str], type_str: str) -> Any:
    """Parse the string value to the appropriate Python type."""
    try:
        if value_str is None or value_str.lower() in ["null", "none"]:
            return None
        if type_str == "int":
            return int(value_str)
        elif type_str == "float":
            return float(value_str)
        elif type_str == "bool":
            return value_str.lower() == "true"
        elif type_str == "str":
            return f'"{value_str}"'
        else:
            return value_str
    except (ValueError, AttributeError) as e:
        logger.warning(f"Failed to parse value '{value_str}' as type '{type_str}': {e}")
        return None
