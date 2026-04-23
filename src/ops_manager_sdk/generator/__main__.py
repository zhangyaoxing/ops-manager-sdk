import os
import sys
import json
from loguru import logger
from ops_manager_sdk.generator.api_resource import APIResource
from ops_manager_sdk.generator.pycode_gen import (
    gen_client_code,
    gen_resources_init_code,
    gen_resource_code,
)
from ops_manager_sdk.generator.utils import HOME_DIR, extract_apis, get_sitemap_urls


LOG_LEVELS: list[str] = [
    "CRITICAL",
    "ERROR",
    "WARNING",
    "SUCCESS",
    "INFO",
    "DEBUG",
    "TRACE",
]
LEVEL: str = os.getenv("LOG_LEVEL", "INFO").upper()
if LEVEL not in LOG_LEVELS:
    LEVEL = "INFO"
logger.remove()
logger.add(sys.stderr, level=LEVEL)

if __name__ == "__main__":
    # Step 1: Find all API documentation URLs from the sitemap.
    urls = get_sitemap_urls()
    # Step 2: Extract API information from the documentation pages.
    api_docs = extract_apis(urls)
    # Step 3: Normalize the extracted API information and save it to a JSON file.
    normalized_api_docs: dict[str, list[dict]] = {}
    for name, normalized_apis in api_docs.items():
        api_resource: APIResource = APIResource(name=name, apis=normalized_apis)
        class_name, normalized_apis = api_resource.normalize_doc_data()
        normalized_api_docs[class_name] = normalized_apis
    output_file = HOME_DIR / "normalized_api_docs.json"
    with output_file.open("w", encoding="utf-8") as f:
        json.dump(normalized_api_docs, f, ensure_ascii=False, indent=4)
    # Step 4: Generate Python code for the OpsManagerClient and resource classes.
    resources: list[tuple[str, str]] = []
    for class_name, normalized_apis in normalized_api_docs.items():
        resource: tuple[str, str] = gen_resource_code(class_name, normalized_apis)
        resources.append(resource)
    gen_client_code(resources)
    gen_resources_init_code(resources)
