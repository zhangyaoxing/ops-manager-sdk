import argparse
import json
import os
import sys
from typing import Any

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


def crawl_docs() -> None:
    """Crawl API documentation and write .data/api_docs.json."""
    urls = get_sitemap_urls()
    extract_apis(urls)


def generate_python_code() -> None:
    """Generate normalized API docs and Python code from .data/api_docs.json."""
    input_file = HOME_DIR / "api_docs.json"
    if not input_file.exists():
        raise FileNotFoundError(
            f"API documentation not found at {input_file}. Run `make crawl` first."
        )

    with input_file.open("r", encoding="utf-8") as f:
        api_docs: dict[str, list[dict[str, Any]]] = json.load(f)

    normalized_api_docs: dict[str, list[dict[str, Any]]] = {}
    for name, normalized_apis in api_docs.items():
        api_resource: APIResource = APIResource(name=name, apis=normalized_apis)
        class_name, normalized_apis = api_resource.normalize_doc_data()
        normalized_api_docs[class_name] = normalized_apis

    output_file = HOME_DIR / "normalized_api_docs.json"
    with output_file.open("w", encoding="utf-8") as f:
        json.dump(normalized_api_docs, f, ensure_ascii=False, indent=4)

    resources: list[tuple[str, str]] = []
    for class_name, normalized_apis in normalized_api_docs.items():
        resource: tuple[str, str] = gen_resource_code(class_name, normalized_apis)
        resources.append(resource)
    gen_client_code(resources)
    gen_resources_init_code(resources)


def reset_api_docs_status(key: str) -> None:
    """Set every status value under one .data/api_docs.json key to 404."""
    input_file = HOME_DIR / "api_docs.json"
    if not input_file.exists():
        raise FileNotFoundError(
            f"API documentation not found at {input_file}. Run `make crawl` first."
        )

    with input_file.open("r", encoding="utf-8") as f:
        api_docs: dict[str, list[dict[str, Any]]] = json.load(f)

    if key not in api_docs:
        raise KeyError(f"Key {key!r} not found in {input_file}.")

    for api_doc in api_docs[key]:
        api_doc["status"] = 404

    with input_file.open("w", encoding="utf-8") as f:
        json.dump(api_docs, f, ensure_ascii=False, indent=4)
    logger.info(f"Reset {len(api_docs[key])} API document statuses under {key!r} to 404.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Ops Manager SDK generator")
    parser.add_argument(
        "command",
        choices=("crawl", "pygen", "reset"),
        help="Generator phase to run.",
    )
    parser.add_argument("key", nargs="?", help="First-level .data/api_docs.json key to reset.")
    parsed_args = parser.parse_args()
    if parsed_args.command == "reset" and parsed_args.key is None:
        parser.error("reset requires a first-level api_docs.json key")
    if parsed_args.command != "reset" and parsed_args.key is not None:
        parser.error(f"{parsed_args.command} does not accept a key argument")
    return parsed_args


if __name__ == "__main__":
    args = parse_args()
    if args.command == "crawl":
        crawl_docs()
    elif args.command == "pygen":
        generate_python_code()
    elif args.command == "reset":
        reset_api_docs_status(args.key)
