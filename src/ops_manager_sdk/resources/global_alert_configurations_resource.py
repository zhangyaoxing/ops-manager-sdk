from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class GlobalAlertConfigurationsResource(BaseResource):
    """Client for GlobalAlertConfigurationsResource resource."""
    class GetAllOpenAlertsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        {global_alert_config_id}: str = Field(alias="{GLOBAL-ALERT-CONFIG-ID}")
    class GetAllOpenAlertsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetAllOpenAlertsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all_open_alerts(self,
        path_params: GetAllOpenAlertsPathParams,
        query_params: Optional[GetAllOpenAlertsQueryParams],
        body_params: Optional[GetAllOpenAlertsBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Open Alerts Triggered by One Global Alert Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configuration-get-all-open-alerts-triggered/
        Description: Retrieve all open alerts triggered by a global alert configuration identified by its GLOBAL-ALERT-CONFIG-ID."""
        return self._request(
            "GET",
            "/globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}/alerts",
            path_params,
            query_params,
            body_params,
        )
    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        enabled: Optional[bool] = Field(alias="enabled")
        event_type_name: str = Field(alias="eventTypeName")
        for_all_groups: bool = Field(alias="forAllGroups")
        group_ids: Optional[list[str]] = Field(alias="groupIds")
        matchers: Optional[list[dict]] = Field(alias="matchers")
        matchers.field_name: Optional[str] = Field(alias="matchers.fieldName")
        matchers.operator: Optional[str] = Field(alias="matchers.operator")
        matchers.value: Optional[str] = Field(alias="matchers.value")
        metric_threshold: Optional[dict] = Field(alias="metricThreshold")
        metric_threshold.metric_name: Optional[str] = Field(alias="metricThreshold.metricName")
        metric_threshold.mode: Optional[str] = Field(alias="metricThreshold.mode")
        metric_threshold.operator: Optional[str] = Field(alias="metricThreshold.operator")
        metric_threshold.threshold: Optional[float] = Field(alias="metricThreshold.threshold")
        metric_threshold.units: Optional[str] = Field(alias="metricThreshold.units")
        notifications: list[dict] = Field(alias="notifications")
        notifications.api_token: Optional[str] = Field(alias="notifications.apiToken")
        notifications.channel_name: Optional[str] = Field(alias="notifications.channelName")
        notifications.delay_min: Optional[float] = Field(alias="notifications.delayMin")
        notifications.email_address: Optional[Any] = Field(alias="notifications.emailAddress")
        notifications.email_enabled: Optional[bool] = Field(alias="notifications.emailEnabled")
        notifications.interval_min: Optional[float] = Field(alias="notifications.intervalMin")
        notifications.webhook_secret: Optional[str] = Field(alias="notifications.webhookSecret")
        notifications.webhook_url: Optional[str] = Field(alias="notifications.webhookUrl")
        notifications.webhook_headers_template: Optional[str] = Field(alias="notifications.webhookHeadersTemplate")
        notifications.webhook_body_template: Optional[str] = Field(alias="notifications.webhookBodyTemplate")
        notifications.microsoft_teams_webhook_url: Optional[str] = Field(alias="notifications.microsoftTeamsWebhookUrl")
        notifications.notification_token: Optional[str] = Field(alias="notifications.notificationToken")
        notifications.room_name: Optional[str] = Field(alias="notifications.roomName")
        notifications.service_key: Optional[str] = Field(alias="notifications.serviceKey")
        notifications.sms_enabled: Optional[bool] = Field(alias="notifications.smsEnabled")
        notifications.type_name: str = Field(alias="notifications.typeName")
        notifications.username: Optional[str] = Field(alias="notifications.username")
        threshold: Optional[dict] = Field(alias="threshold")
        threshold.operator: Optional[str] = Field(alias="threshold.operator")
        threshold.threshold: Optional[float] = Field(alias="threshold.threshold")
        tags: Optional[list[str]] = Field(alias="tags")
        type_name: Optional[str] = Field(alias="typeName")
    def create(self,
        path_params: Optional[CreatePathParams],
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """API: Create One Global Alert Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configurations-create-one/
        Description: Create one global alert configuration."""
        return self._request(
            "POST",
            "/globalAlertConfigs",
            path_params,
            query_params,
            body_params,
        )
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        {global_alert_config_id}: str = Field(alias="{GLOBAL-ALERT-CONFIG-ID}")
    class DeleteQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class DeleteBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def delete(self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
        body_params: Optional[DeleteBodyParams],
    ) -> dict[str, Any]:
        """API: Delete One Global Alert Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configurations-delete-one/
        Description: Delete one global alert configuration."""
        return self._request(
            "DELETE",
            "/globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )
    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetAllBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all(self,
        path_params: Optional[GetAllPathParams],
        query_params: Optional[GetAllQueryParams],
        body_params: Optional[GetAllBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Global Alert Configurations
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configurations-get-all/
        Description: Retrieve all global alert configurations."""
        return self._request(
            "GET",
            "/globalAlertConfigs",
            path_params,
            query_params,
            body_params,
        )
    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        {global_alert_config_id}: str = Field(alias="{GLOBAL-ALERT-CONFIG-ID}")
    class GetOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetOneBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_one(self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
        body_params: Optional[GetOneBodyParams],
    ) -> dict[str, Any]:
        """API: Get One Global Alert Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configurations-get-one/
        Description: Retrieve one global alert configuration by its GLOBAL-ALERT-CONFIG-ID."""
        return self._request(
            "GET",
            "/globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )
    class TestGlobalAlertConfigurationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        alert_config_id: str = Field(alias="ALERT-CONFIG-ID")
        notification_id: str = Field(alias="NOTIFICATION-ID")
    class TestGlobalAlertConfigurationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class TestGlobalAlertConfigurationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def test_global_alert_configuration(self,
        path_params: TestGlobalAlertConfigurationPathParams,
        query_params: Optional[TestGlobalAlertConfigurationQueryParams],
        body_params: Optional[TestGlobalAlertConfigurationBodyParams],
    ) -> dict[str, Any]:
        """API: Test Global Alert Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configurations-test-one/
        Description: Triggers a test notification for a specific notification method in a global alert configuration. This endpoint sends a test payload with dummy data and rendered templates to validate your webhook configuration."""
        return self._request(
            "POST",
            "/api/public/v1.0/globalAlertConfigs/{ALERT-CONFIG-ID}/{NOTIFICATION-ID}/test",
            path_params,
            query_params,
            body_params,
        )
    class EnableOrDisablePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        {global_alert_config_id}: str = Field(alias="{GLOBAL-ALERT-CONFIG-ID}")
    class EnableOrDisableQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class EnableOrDisableBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        enabled: bool = Field(alias="enabled")
    def enable_or_disable(self,
        path_params: EnableOrDisablePathParams,
        query_params: Optional[EnableOrDisableQueryParams],
        body_params: EnableOrDisableBodyParams,
    ) -> dict[str, Any]:
        """API: Enable or Disable One Global Alert Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configurations-toggle-one/
        Description: Enable or disable one global alert configuration identified by its GLOBAL-ALERT-CONFIG-ID."""
        return self._request(
            "PATCH",
            "/globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        {global_alert_config_id}: str = Field(alias="{GLOBAL-ALERT-CONFIG-ID}")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        enabled: Optional[bool] = Field(alias="enabled")
        event_type_name: str = Field(alias="eventTypeName")
        for_all_groups: bool = Field(alias="forAllGroups")
        group_ids: Optional[list[str]] = Field(alias="groupIds")
        matchers: Optional[list[dict]] = Field(alias="matchers")
        matchers.field_name: Optional[str] = Field(alias="matchers.fieldName")
        matchers.operator: Optional[str] = Field(alias="matchers.operator")
        matchers.value: Optional[str] = Field(alias="matchers.value")
        metric_threshold: Optional[dict] = Field(alias="metricThreshold")
        metric_threshold.metric_name: Optional[str] = Field(alias="metricThreshold.metricName")
        metric_threshold.mode: Optional[str] = Field(alias="metricThreshold.mode")
        metric_threshold.operator: Optional[str] = Field(alias="metricThreshold.operator")
        metric_threshold.threshold: Optional[float] = Field(alias="metricThreshold.threshold")
        metric_threshold.units: Optional[str] = Field(alias="metricThreshold.units")
        notifications: list[dict] = Field(alias="notifications")
        notifications.api_token: Optional[str] = Field(alias="notifications.apiToken")
        notifications.channel_name: Optional[str] = Field(alias="notifications.channelName")
        notifications.delay_min: Optional[float] = Field(alias="notifications.delayMin")
        notifications.email_address: Optional[Any] = Field(alias="notifications.emailAddress")
        notifications.email_enabled: Optional[bool] = Field(alias="notifications.emailEnabled")
        notifications.interval_min: Optional[float] = Field(alias="notifications.intervalMin")
        notifications.webhook_secret: Optional[str] = Field(alias="notifications.webhookSecret")
        notifications.webhook_url: Optional[str] = Field(alias="notifications.webhookUrl")
        notifications.webhook_headers_template: Optional[str] = Field(alias="notifications.webhookHeadersTemplate")
        notifications.webhook_body_template: Optional[str] = Field(alias="notifications.webhookBodyTemplate")
        notifications.microsoft_teams_webhook_url: Optional[str] = Field(alias="notifications.microsoftTeamsWebhookUrl")
        notifications.notification_token: Optional[str] = Field(alias="notifications.notificationToken")
        notifications.room_name: Optional[str] = Field(alias="notifications.roomName")
        notifications.service_key: Optional[str] = Field(alias="notifications.serviceKey")
        notifications.sms_enabled: Optional[bool] = Field(alias="notifications.smsEnabled")
        notifications.type_name: str = Field(alias="notifications.typeName")
        notifications.username: Optional[str] = Field(alias="notifications.username")
        threshold: Optional[dict] = Field(alias="threshold")
        threshold.operator: Optional[str] = Field(alias="threshold.operator")
        threshold.threshold: Optional[float] = Field(alias="threshold.threshold")
        tags: Optional[list[str]] = Field(alias="tags")
        type_name: Optional[str] = Field(alias="typeName")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: UpdateBodyParams,
    ) -> dict[str, Any]:
        """API: Update One Global Alert Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configurations-update-one/
        Description: Update one global alert configuration identified by its GLOBAL-ALERT-CONFIG-ID."""
        return self._request(
            "PUT",
            "/globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )