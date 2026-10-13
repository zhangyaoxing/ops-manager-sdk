# Ops Manager SDK Generator

This tool is used to generate MongoDB Ops Manager SDKs. Currently only Python SDK is done for Ops Manager 8.0.

## How Is It Built
The SDK code is generated based on the [Ops Mananger API document](https://www.mongodb.com/docs/ops-manager/current/api/).
1. Playwright is used to crawl pages listed in the sitemap.
2. Metadata of each API endpoint is extracted from the page.
3. The code generator uses the metadata to generate Python code SDK.

You can find the original metadata extracted from API documents in the file `.data/api_docs.json`. It's then normalized and saved in `.data/normalized_api_docs.json`.

## Configuration
The generator reads its configuration from a `.env` file in the project root. Copy the template and adjust as needed — every variable is optional:
```bash
cp .env.example .env
```

| Variable | Default | Description |
| --- | --- | --- |
| `SITEMAP_URL` | `https://www.mongodb.com/docs/ops-manager/v8.0/sitemap-0.xml` | Sitemap used to discover the API documentation pages. |
| `API_BASE_URL` | `https://www.mongodb.com/docs/ops-manager/v8.0/reference/api/` | Only sitemap entries with this prefix are treated as API documents. |
| `HOME_DIR` | `.data` | Directory holding `api_docs.json` and `normalized_api_docs.json`. Relative paths are resolved against the working directory the command starts in. |
| `EXPIRE_DAYS` | `7` | Number of days after which a crawled API document expires and gets recrawled. |
| `LOG_LEVEL` | `INFO` | Loguru log level, one of `CRITICAL`, `ERROR`, `WARNING`, `SUCCESS`, `INFO`, `DEBUG`, `TRACE`. |
| `ENV` | `INFO` | Set to `DEVELOPMENT` to crawl only a few pages per run before stopping. |
| `FORCE_CRAWL` | `0` | Set to `1`, `true` or `yes` to ignore the cached `api_docs.json` and recrawl everything. |

`SITEMAP_URL` and `API_BASE_URL` are not set in `.env.example`: they default to the documentation version derived from the `[project]` version in `pyproject.toml`, formatted as `v{major}.{minor}` (the examples above assume version `8.0.x`). Bumping the version in `pyproject.toml` therefore retargets the generator at the matching documentation version, and uncommenting the variables in `.env` overrides that.

Exported environment variables take precedence over `.env`, so `FORCE_CRAWL=1 make crawl` still works.

## How to Use
The `Makefile` has some targets that can help you run the code:

### Crawl the Documents
```bash
make crawl
```
This will crawl the document in the `.data/api_docs.json` which are:
- Older than `EXPIRE_DAYS` days (7 by default), or
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