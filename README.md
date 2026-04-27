# Ops Manager SDK Generator

[![PyPI version](https://img.shields.io/pypi/v/ops-manager-sdk.svg)](https://pypi.org/project/ops-manager-sdk/)

This tool is used to generate MongoDB Ops Manager SDKs. Currently only Python SDK is done for Ops Manager 8.0.

## How It's Built?
The SDK code is generated based on the [Ops Mananger API document](https://www.mongodb.com/docs/ops-manager/current/api/).
1. Playwright is used to crawl pages listed in the sitemap.
2. Metadata of each API endpoint is extracted from the page.
3. The code generator uses the metadata to generate Python code SDK.

You can find the original metadata extracted from API documents in the file `.data/api_docs.json`. It's then normalized and saved in `.data/normalized_api_docs.json`.

## Known Issues
- The API document website has rate limits and sometimes you can't finish crawling all documents and get 403 forbidden. In this case, wait for a few minutes and try again. It will auto retry the failed URLs.
- The document is not always accurate. Sometimes I have to make reasonable assumptions. For example, the necessity can be missing. In this case the parameter is always marked as `optional`. These problems will be gone when we fix the document.