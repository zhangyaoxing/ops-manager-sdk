import os
import sys
from loguru import logger
from ops_manager_sdk.generator.api_resource import APIResource
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
    for name, apis in api_docs.items():
        resource: APIResource = APIResource(name=name, apis=apis)
        resource.generate_code()
