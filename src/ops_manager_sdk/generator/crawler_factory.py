import os
import re
from typing import Any, Optional
from datetime import datetime, timezone
import httpx
from playwright.sync_api import (
    Browser,
    Locator,
    Page,
    Playwright,
    Response,
    BrowserContext,
    sync_playwright,
)
from loguru import logger


class StandardCrawler:
    LOCATORS: dict[str, str] = {
        "title": "xpath=(//h1)[1]",
        "name": "xpath=(//a[@aria-current='page'])[1]",
        "description": "xpath=(//div[@class='body'])[1]/section[1]/p[1]",
        "endpoints": "xpath=(//h2[contains(text(), 'Resource') or contains(text(), 'Request') or contains(text(), 'Syntax') or contains(text(), 'Endpoint')])[1]/following-sibling::div[contains(@class, 'intro-code-block')]//td",
        "path_params": "xpath=(//h3[contains(text(), 'Path Parameters')])[1]/following-sibling::div[1]/table",
        "query_params": "xpath=(//h3[contains(text(), 'Query Parameters')])[1]/following-sibling::div/table",
        "body_params": "xpath=(//h3[contains(text(), 'Body Parameters')])[1]/following-sibling::div/table",
        "body_desc": "xpath=(//h3[contains(text(), 'Body Parameters')])[1]/following-sibling::p[1]",
        "resource": "xpath=//div[@class='body']/div[1]//a[contains(@href, '/reference/api/')]",
    }
    COLUMN_MAPPING: tuple[int, int, int, int, int] = (0, 0, 0, 0, 0)

    def __init__(self, context: BrowserContext):
        self.context: BrowserContext = context

    def _column_mapping(self, params_locator: Locator) -> tuple[int, int, int, int, int]:
        """Determines the column indices for parameter name, type, required status, description, and default value.
        Args:
            params_locator: A Playwright Locator pointing to the parameter table in the API documentation.
        Returns:
            A tuple containing the column indices for name, type, required status, description, and default value.
        """
        header_locator = params_locator.locator("xpath=./thead/tr/th")
        name_col, type_col, required_col, desc_col, default_col = self.COLUMN_MAPPING
        for i in range(header_locator.count()):
            header_text = header_locator.nth(i).inner_text().strip().lower()
            # The column name of parameter name varies.
            if (
                "name" in header_text
                or "parameter" in header_text
                or "path element" in header_text
                or "field" in header_text
            ):
                name_col = i + 1
            elif "type" in header_text:
                type_col = i + 1
            elif "required" in header_text or "necessity" in header_text:
                required_col = i + 1
            elif "description" in header_text:
                desc_col = i + 1
            elif "default" in header_text:
                default_col = i + 1
        if name_col == 0:
            logger.warning(
                f"Could not find 'Name' column in parameters table. Defaulting to first column. URL: {params_locator.page.url}"
            )
            name_col = 1
        return name_col, type_col, required_col, desc_col, default_col

    def _get_params(self, params_locator: Locator, **kwargs) -> list[dict[str, Any]]:
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

        # In some documents, the parameters are listed in multiple tables instead of one table.
        # So we need to loop through all tables to get the parameters.
        tables: list = params_locator.all()
        for table in tables:
            name_col, type_col, required_col, desc_col, default_col = self._column_mapping(table)
            locators = table.locator("xpath=./tbody/tr").all()
            for param in locators:
                param_name: str = param.locator(f"xpath=./td[{name_col}]").inner_text()
                # In some pages the parameter is surrounded by {}.
                # The [n] indicates the parameter is an array, which is already known from the type.
                param_name = param_name.replace("[n]", "").strip("{}")
                if type_override is not None:
                    param_type: str = type_override
                else:
                    param_type_locator = param.locator(f"xpath=./td[{type_col}]")
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

                desc_locator: Locator = param.locator(f"xpath=./td[{desc_col}]")
                if desc_locator.count() == 0:
                    desc_locator = param.locator(f"xpath=./td[{required_col}]")
                desc: str = (
                    desc_locator.inner_text() if desc_locator.count() > 0 else "No description."
                )
                has_table = desc_locator.locator("xpath=(.//table|.//ul)").count() > 0
                if has_table and param_name != "envelope":
                    param_display = param_name.replace("\n", " ")
                    logger.debug(
                        f"Parameter {param_display} ({params_locator.page.url}) has a table in its description."
                    )
                wrong_type = param_type == "object" and "." in param_name
                if wrong_type:
                    logger.debug(
                        f"Parameter {param_name} ({params_locator.page.url}) type may be wrong."
                    )

                if required_override is not None:
                    required: str = required_override
                else:
                    required_locator = param.locator(f"xpath=./td[{required_col}]")
                    if required_locator.count() > 0:
                        required = required_locator.inner_text()
                    elif "required" in desc.lower() or "required" in param_name.lower():
                        required = "Required"
                    else:
                        required = "Optional"

                if "\nrequired" in param_name.lower():
                    param_name = param_name.split("\n")[0]
                param_name = param_name.replace("\n", " ").strip()

                default_locator: Locator = param.locator(f"xpath=./td[{default_col}]")
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
                        "description": desc,
                        "default": default_value,
                    }
                )
        return params

    def get_title(self, page: Page) -> str:
        title_locator = page.locator(self.LOCATORS["title"])
        if title_locator.count() > 0:
            title: str = title_locator.inner_text()
            logger.debug(f"Extracted title: {title} from {page.url}")
            return title
        logger.warning(f"No title found in document: {page.url}")
        return "Untitled API"

    def get_resource_name(self, page: Page) -> str:
        resource_name_locator = page.locator(self.LOCATORS["resource"])
        if resource_name_locator.count() > 0:
            resource_name: str = re.sub(
                r"[^a-zA-Z0-9]", "", resource_name_locator.last.inner_text().title()
            )
            logger.debug(f"Extracted resource name: {resource_name} from {page.url}")
            return resource_name
        return "Root"

    def get_action_name(self, page: Page) -> str:
        action_name_locator = page.locator(self.LOCATORS["name"])
        if action_name_locator.count() > 0:
            action_name: str = action_name_locator.inner_text()
            logger.debug(f"Extracted action name: {action_name} from {page.url}")
            return action_name
        logger.warning(f"No name found in document: {page.url}")
        return "Unknown Action Name"

    def get_description(self, page: Page) -> str:
        description_locator = page.locator(self.LOCATORS["description"])
        if description_locator.count() > 0:
            description: str = description_locator.inner_text()
            logger.debug(f"Extracted description: {description} from {page.url}")
            if "Base URL" not in description:
                return description
        logger.debug(f"No description found in document: {page.url}")
        return "No description."

    def get_endpoints(self, page: Page) -> list[str]:
        endpoints = page.locator(self.LOCATORS["endpoints"]).all_inner_texts()
        logger.debug(f"Extracted endpoints: {endpoints} from {page.url}")
        return endpoints

    def get_path_params(self, page: Page) -> list[dict[str, Any]]:
        # All path parameters are required. Sometimes documents miss the "Required" column.
        # All path parameters are of type string.
        # Sometimes documents miss the "Type" column or have incorrect type for path parameters.
        return self._get_params(
            page.locator(self.LOCATORS["path_params"]),
            required_override="Required",
            type_override="string",
        )

    def get_query_params(self, page: Page) -> list[dict[str, Any]]:
        return self._get_params(page.locator(self.LOCATORS["query_params"]))

    def get_body_params(self, page: Page) -> list[dict[str, Any]]:
        return self._get_params(page.locator(self.LOCATORS["body_params"]))

    def get_body_description(self, page: Page) -> str:
        body_desc_locator = page.locator(self.LOCATORS["body_desc"])
        if body_desc_locator.count() > 0:
            body_desc: str = body_desc_locator.inner_text()
            if "array of" in body_desc.lower():
                return "array"

        return "object"

    def crawl(self, url: str) -> tuple[Optional[str], Optional[dict[str, Any]]]:
        try:
            page = self.context.new_page()
            res: Optional[Response] = page.goto(url, wait_until="domcontentloaded")
            status: Optional[int] = res.status if res else None
            if status is None or status >= 300 or status < 200:
                raise httpx.HTTPError(f"Failed to load page with status code: {status}")

            title: str = self.get_title(page)
            action_name: str = self.get_action_name(page)
            resource_name: str = self.get_resource_name(page)
            description: str = self.get_description(page)
            endpoints: list[str] = self.get_endpoints(page)
            path_params: list[dict[str, Any]] = self.get_path_params(page)
            query_params: list[dict[str, Any]] = self.get_query_params(page)
            body_params: list[dict[str, Any]] = self.get_body_params(page)
            body_type: str = self.get_body_description(page)
            if len(endpoints) == 0:
                logger.warning(
                    f"No endpoints found for URL: {url}. Skipping this API documentation."
                )
                return None, None
            return resource_name, {
                "title": title,
                "name": action_name,
                "description": description,
                "endpoints": endpoints,
                "path_params": path_params,
                "query_params": query_params,
                "body_params": body_params,
                "body_type": body_type,
                "capture_time": datetime.now(timezone.utc).isoformat(),
                "doc_url": url,
                "status": status,
            }
        except (httpx.HTTPError, AttributeError) as exc:
            logger.error(f"Error processing URL {url}: {exc}")
        finally:
            page.close()
        return "Root", {
            "title": "Error",
            "capture_time": datetime.now(timezone.utc).isoformat(),
            "doc_url": url,
            "status": status,
        }


class NoPathTitleCrawler(StandardCrawler):
    LOCATORS = StandardCrawler.LOCATORS.copy()

    def __init__(self, context):
        super().__init__(context)
        # This is a special handling for the following page which misses the path parameter title.
        # https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/daemonConfigs/get-one-backup-daemon-configuration-by-host/
        self.LOCATORS["path_params"] = (
            "xpath=(//h2[contains(text(), 'Resource') or contains(text(), 'Request') or contains(text(), 'Syntax') or contains(text(), 'Endpoint')])[1]/following-sibling::div[not(contains(@class, 'intro-code-block'))]/table"
        )


class OrganizationAccessListsCrawler(StandardCrawler):
    def get_body_params(self, page: Page) -> list[dict[str, Any]]:
        params = super().get_body_params(page)
        for param in params:
            param["name"] = param["name"].replace("[i].", "")
        return params


class EventsCrawler(StandardCrawler):
    LOCATORS = StandardCrawler.LOCATORS.copy()

    def __init__(self, context) -> None:
        super().__init__(context)
        # This is a special handling for the following page which has a different structure for body parameters.
        # https://www.mongodb.com/docs/ops-manager/current/reference/api/events/
        self.LOCATORS["query_params"] = (
            "xpath=(//h3[contains(text(), 'Query Parameters')])[1]/following-sibling::section/div/table"
        )

    def get_path_params(self, page: Page) -> list[dict[str, Any]]:
        path_params: list[dict[str, Any]] = super().get_path_params(page)
        # Special handling for the following page where the "orgId" is missing.
        # https://www.mongodb.com/docs/ops-manager/current/reference/api/events/get-all-events-for-org/
        if "get-all-events-for-org/" in page.url:
            path_params.append(
                {
                    "name": "orgId",
                    "type": "string",
                    "required": "Required",
                    "description": "The unique identifier of the organization.",
                    "default": None,
                }
            )
        return path_params


class GroupIDtoProjectIDCrawler(StandardCrawler):
    def get_endpoints(self, page: Page) -> list[str]:
        # Special handling for the integration pages where the "groupId" is used instead of "projectId".
        endpoints = super().get_endpoints(page)
        endpoints = [endpoint.replace("{GROUP-ID}", "{PROJECT-ID}") for endpoint in endpoints]
        return endpoints


class IntegrationCrawler(GroupIDtoProjectIDCrawler):
    def get_description(self, page) -> str:
        return """Use the following dataclasses to pass the integration settings:

- PagerDutyIntegrationSettings
- SlackIntegrationSettings
- DatadogIntegrationSettings
- HipChatIntegrationSettings
- OpsgenieIntegrationSettings
- VictorOpsIntegrationSettings
- WebhookIntegrationSettings
- MicrosoftTeamsIntegrationSettings
- PrometheusIntegrationSettings
"""

    def get_body_params(self, page) -> list[dict[str, Any]]:
        return [
            {
                "name": "type",
                "type": "string",
                "required": "Required",
                "description": "The type of the third-party integration.",
                "default": None,
            }
        ]


class MissingHeader4ColsCrawler(StandardCrawler):
    COLUMN_MAPPING: tuple[int, int, int, int, int] = (1, 2, 0, 3, 4)


class MissingHeader5ColsCrawler(StandardCrawler):
    COLUMN_MAPPING: tuple[int, int, int, int, int] = (1, 2, 3, 4, 5)


class InvitationsCrawler(StandardCrawler):
    COLUMN_MAPPING: tuple[int, int, int, int, int] = (1, 2, 3, 4, 0)


class GetAllHostsInOneProjectCrawler(StandardCrawler):
    def get_query_params(self, page: Page) -> list[dict[str, Any]]:
        params: list[dict[str, Any]] = super().get_query_params(page)
        params[-1]["name"] = "clusterId"
        return params


class CrawlerFactory:
    crawlers: dict[str, StandardCrawler] = {}
    playwright: Playwright
    browser: Browser

    @staticmethod
    def initiate_crawler() -> None:
        is_debug: bool = os.getenv("ENV", "INFO").upper() == "DEVELOPMENT"
        CrawlerFactory.playwright = sync_playwright().start()
        CrawlerFactory.browser = CrawlerFactory.playwright.chromium.launch(headless=not is_debug)
        context = CrawlerFactory.browser.new_context()
        context.set_default_timeout(10000)
        CrawlerFactory.crawlers["standard"] = StandardCrawler(context)
        CrawlerFactory.crawlers["no_path_title"] = NoPathTitleCrawler(context)
        CrawlerFactory.crawlers["organization_access_lists"] = OrganizationAccessListsCrawler(
            context
        )
        CrawlerFactory.crawlers["events"] = EventsCrawler(context)
        CrawlerFactory.crawlers["group_id_to_project_id"] = GroupIDtoProjectIDCrawler(context)
        CrawlerFactory.crawlers["integration"] = IntegrationCrawler(context)
        CrawlerFactory.crawlers["missing_header_4_cols"] = MissingHeader4ColsCrawler(context)
        CrawlerFactory.crawlers["missing_header_5_cols"] = MissingHeader5ColsCrawler(context)
        CrawlerFactory.crawlers["invitations"] = InvitationsCrawler(context)
        CrawlerFactory.crawlers["get_all_hosts_in_one_project"] = GetAllHostsInOneProjectCrawler(
            context
        )

    @staticmethod
    def close() -> None:
        CrawlerFactory.browser.close()
        CrawlerFactory.playwright.stop()

    @staticmethod
    def crawl(url: str) -> tuple[Optional[str], Optional[dict[str, Any]]]:
        if "/get-one-backup-daemon-configuration-by-host/" in url:
            crawler = CrawlerFactory.crawlers["no_path_title"]
        elif "create-org-api-key-access-list" in url:
            crawler = CrawlerFactory.crawlers["organization_access_lists"]
        elif "/events/get-all" in url or "/measures/" in url:
            crawler = CrawlerFactory.crawlers["events"]
        elif (
            "/third-party-integration-settings-create/" in url
            or "/third-party-integration-settings-update/" in url
        ):
            crawler = CrawlerFactory.crawlers["integration"]
        elif "/third-party-integration" in url:
            crawler = CrawlerFactory.crawlers["group_id_to_project_id"]
        elif url in [
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/mongoConfigs/get-all-blockstore-configurations/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/oplog/mongoConfigs/get-all-oplog-configurations/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/oplog/s3Configs/get-all-s3-oplog-configurations/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/sync/mongoConfigs/get-all-sync-store-configurations/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/log-collections/log-collections-get-one/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/performance-advisor/get-slow-queries/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/performance-advisor/get-suggested-indexes/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/restorejobs/get-all-restore-jobs-for-one-cluster/",
        ]:
            crawler = CrawlerFactory.crawlers["missing_header_4_cols"]
        elif url in [
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alerts-get-all/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/log-collections/log-collections-get-all/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/create-one-report/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/diagnostics/get-project-diagnostic-archive/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/fileSystemConfigs/get-all-file-system-store-configurations/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/s3Configs/get-all-s3-blockstore-configurations/",
        ]:
            crawler = CrawlerFactory.crawlers["missing_header_5_cols"]
        elif "/get-all-hosts-in-group/" in url:
            crawler = CrawlerFactory.crawlers["get_all_hosts_in_one_project"]
        elif "/get-all-invitations/" in url:
            crawler = CrawlerFactory.crawlers["invitations"]
        else:
            crawler = CrawlerFactory.crawlers["standard"]
        return crawler.crawl(url)
