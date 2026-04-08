import os
import sys
from loguru import logger
from ops_manager_sdk.generator.utils import extract_apis

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
    api_docs = extract_apis()
