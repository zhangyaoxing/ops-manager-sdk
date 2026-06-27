# Ops Manager SDK Generator

This tool is used to generate MongoDB Ops Manager SDKs. Currently only Python SDK is done for Ops Manager 8.0.

## How Is It Built
The SDK code is generated based on the [Ops Mananger API document](https://www.mongodb.com/docs/ops-manager/current/api/).
1. Playwright is used to crawl pages listed in the sitemap.
2. Metadata of each API endpoint is extracted from the page.
3. The code generator uses the metadata to generate Python code SDK.

You can find the original metadata extracted from API documents in the file `.data/api_docs.json`. It's then normalized and saved in `.data/normalized_api_docs.json`.

## How to Use
The `Makefile` has some targets that can help you run the code:

### Crawl the Documents
```bash
make crawl
```
This will crawl the document in the `.data/api_docs.json` which are:
- Older than 30 days, or
- Returned non-200 HTTP response.

If the crawls are all successful, it will generate a normalized version of the API metadata `.data/normalized_api_docs.json`. The normalized metadata fixes some known issues, and is easier to use for code generation.

### Recrawl the Documents
If there are new API endpoints added, or if you simply want to recrawl all the document, use this target:
```bash
make recrawl
```

### Reset and Crawl
If you wish to recrawl all documents of a certain resource, use the reset target. It will set the `status` of each document to `404`, so in the next crawl run, the documents can be recrawled.
```bash
make reset KEY=SnapshotSchedule
make crawl
```

### Generate Python SDK Code
After crawling the document, you can generate code for Python SDK
```bash
make pygen
```

### Formate Generated Code
Optional. Use Black to format the generated code:
```bash
make format-resources
```

## Known Issues
- The API document website has rate limits and sometimes you can't finish crawling all documents and get 403 forbidden. In this case, wait for a few minutes and try again. It will auto retry the failed URLs.
- The document is not always accurate. Sometimes I have to make reasonable assumptions. For example, the necessity can be missing. In this case the parameter is always marked as `optional`. These problems will be gone when we fix the document.