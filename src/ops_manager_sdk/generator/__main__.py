import os
import sys
from loguru import logger
from ops_manager_sdk.generator.api_resource import APIResource
from ops_manager_sdk.generator.client import generate_client_code
from ops_manager_sdk.generator.utils import extract_apis, get_sitemap_urls

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
    urls = get_sitemap_urls()
    api_docs = extract_apis(urls)
    resources: list[tuple[str, str]] = []
    for name, apis in api_docs.items():
        resource: APIResource = APIResource(name=name, apis=apis)
        resources.extend(resource.generate_code())
    generate_client_code(resources)
