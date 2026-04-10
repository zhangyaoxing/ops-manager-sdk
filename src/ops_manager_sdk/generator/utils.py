from typing import Any, Optional
from pathlib import Path
import os
import json
from datetime import datetime, timezone
import xml.etree.ElementTree as ET
import httpx
from loguru import logger
from playwright.sync_api import Locator, Page, sync_playwright, Response


SITEMAP_URL: str = "https://www.mongodb.com/docs/ops-manager/current/sitemap-0.xml"
API_BASE_URL: str = "https://www.mongodb.com/docs/ops-manager/current/reference/api/"
HOME_DIR: Path = Path.home() / ".ops_manager_sdk"
EXPIRE_DAYS: int = 7

LOCATORS = {
    # Title is unique per API.
    "title": "xpath=(//h1)[1]",
    "name": "xpath=(//a[@aria-current='page'])[1]",
    "description": "xpath=(//div[@class='body'])[1]/section[1]/p[1]",
    # There can be more than one resources per API.
    "endpoints": "xpath=(//h2[contains(text(), 'Resource') or contains(text(), 'Request') or contains(text(), 'Syntax') or contains(text(), 'Endpoint')])[1]/following-sibling::div[contains(@class, 'intro-code-block')]//td",
    # There can be more than one path/query/body parameters per API.
    "path_params": "xpath=(//h3[contains(text(), 'Path Parameters')])[1]/following-sibling::div[1]/table[1]/tbody[1]/tr",
    "path_params_alternative": "xpath=(//h2[contains(text(), 'Resource') or contains(text(), 'Request') or contains(text(), 'Syntax') or contains(text(), 'Endpoint')])[1]/following-sibling::div[not(contains(@class, 'intro-code-block'))]//tbody[1]/tr",
    "query_params": "xpath=(//h3[contains(text(), 'Query Parameters')])[1]/following-sibling::div/table/tbody/tr",
    "body_params": "xpath=(//h3[contains(text(), 'Body Parameters')])[1]/following-sibling::div[1]/table[1]/tbody[1]/tr",
    "api_path": "xpath=//div[@class='body']/div[1]//a[contains(@href, '/reference/api/')]",
}


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
            if loc.startswith(API_BASE_URL) and not "nav" in loc:
                api_urls.append(loc)
                logger.debug(f"Found API URL: {loc}")
    logger.info(f"Total API URLs found: {len(api_urls)}")
    return api_urls


def _get_params(params_locator: Locator, **kwargs) -> list[dict[str, Any]]:
    """Extracts parameters from the given locator.
    Args:
        params_locator: A Playwright Locator pointing to the parameter rows in the API documentation.
        kwargs: Optional keyword arguments for parameter extraction.
            - required_override: If provided, this value will be used for the "required" field of all parameters, overriding any value found in the document.
            - type_override: If provided, this value will be used for the "type" field of all parameters, overriding any value found in the document.
    Returns:
        A list of dictionaries, each representing a parameter with its name, type, required status, and default value.
    """
    required_override = kwargs.get("required_override", None)
    type_override = kwargs.get("type_override", None)
    params: list[dict[str, Any]] = []
    locators: list = params_locator.all()
    for param in locators:
        param_name: str = param.locator("xpath=./td[1]").inner_text()
        if type_override is not None:
            param_type: str = type_override
        else:
            param_type_locator = param.locator("xpath=./td[2]")
            if param_type_locator.count() > 0:
                param_type = param_type_locator.inner_text()
            else:
                param_type = "string"
        # If param_name is one of the following, overwrite the type.
        # Because some pages have incorrect type for these parameters
        if param_name in ["pageNum", "itemsPerPage"]:
            param_type = "number"
        if param_name in ["envelope", "pretty"]:
            param_type = "boolean"
        if param_name in ["since", "duration"]:
            param_type = "long"
        if param_name == "CLUSTER-ID":
            param_name = "clusterId"
            param_type = "string"

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
            inner_text = default_locator.inner_text()
            default_value: Optional[str] = inner_text if inner_text else None
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
            status: str = api["status"]
            capture_time_str: str = api["capture_time"]
            capture_time = datetime.fromisoformat(capture_time_str)
            if status in [403, 401] or (now - capture_time).days >= EXPIRE_DAYS:
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
    is_debug: bool = os.getenv("LOG_LEVEL", "INFO").upper() == "DEBUG"
    # Check if the API document was crawled recently (within the last 7 days).
    HOME_DIR.mkdir(parents=True, exist_ok=True)
    output_file = HOME_DIR / "api_docs.json"
    api_docs: dict[str, list] = {}
    if output_file.exists():
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

    with sync_playwright() as p:
        logger.info("Starting API documentation extraction...")
        browser = p.chromium.launch(headless=not is_debug)
        context = browser.new_context()

        for index, url in enumerate(urls):
            try:
                page: Page = context.new_page()
                res: Optional[Response] = page.goto(url, wait_until="domcontentloaded")
                status: Optional[int] = res.status if res else None
                if status in [403, 401]:
                    # In this case we still want to write the result into output file,
                    # so that the URL can be recrawled in the next run.
                    logger.warning(f"Failed to fetch page: {status} ({url})")
                    api_docs["Root"] = api_docs.get("Root", []) + [
                        {
                            "title": f"Access Denied ({status})",
                            "capture_time": datetime.now(timezone.utc).isoformat(),
                            "doc_url": url,
                            "status": status,
                        }
                    ]
                    continue

                title: str = page.locator(LOCATORS["title"]).inner_text()
                endpoints: list[str] = page.locator(LOCATORS["endpoints"]).all_inner_texts()
                if len(endpoints) == 0:
                    logger.warning(f"No endpoint found in document: {title} ({url})")
                    continue
                # All path parameters are required. Sometimes documents miss the "Required" column.
                # All path parameters are of type string. Sometimes documents miss the "Type" column or have incorrect type for path parameters.
                path_params: list[dict[str, Any]] = _get_params(
                    page.locator(LOCATORS["path_params"]),
                    required_override="Required",
                    type_override="string",
                )
                if len(path_params) == 0:
                    # Try the alternative locator for path parameters.
                    # This is a special handling for the following page:
                    # https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/daemonConfigs/get-one-backup-daemon-configuration-by-host/
                    path_params = _get_params(
                        page.locator(LOCATORS["path_params_alternative"]),
                        required_override="Required",
                        type_override="string",
                    )
                query_params: list[dict[str, Any]] = _get_params(
                    page.locator(LOCATORS["query_params"])
                )
                body_params: list[dict[str, Any]] = _get_params(
                    page.locator(LOCATORS["body_params"])
                )
                category_locator: Locator = page.locator(LOCATORS["api_path"])
                if category_locator.count() == 0:
                    category_name: str = "Root"
                else:
                    category_name = category_locator.last.inner_text().title().replace(" ", "")
                if category_name not in api_docs:
                    api_docs[category_name] = []
                action_locator: Locator = page.locator(LOCATORS["name"])
                if action_locator.count() > 0:
                    name = action_locator.inner_text()
                else:
                    name = title
                description_locator: Locator = page.locator(LOCATORS["description"])
                if description_locator.count() > 0:
                    description = description_locator.inner_text()
                else:
                    description = ""
                api_docs[category_name].append(
                    {
                        "title": title,
                        "name": name,
                        "description": description,
                        "endpoints": endpoints,
                        "path_params": path_params,
                        "query_params": query_params,
                        "body_params": body_params,
                        "capture_time": datetime.now(timezone.utc).isoformat(),
                        "doc_url": url,
                        "status": status,
                    }
                )
                if is_debug and index >= 10:
                    break
            except (httpx.HTTPError, AttributeError) as exc:
                logger.error(f"Error processing URL {url}: {exc}")
                continue
            finally:
                processed = index + 1
                if processed % 10 == 0:
                    logger.info(f"Processed APIs: {processed}/{len(urls)}")
                page.close()
        browser.close()
        with output_file.open("w", encoding="utf-8") as f:
            indent: Optional[int] = 4 if is_debug else None
            json.dump(api_docs, f, ensure_ascii=False, indent=indent)
        return api_docs
