from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class AlertConfigurationsResource(BaseResource):
    """Client for AlertConfigurationsResource resource."""
    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        enabled: Optional[bool] = Field(alias="enabled")
        event_type_name: str = Field(alias="eventTypeName")
        matchers.field_name: Optional[str] = Field(alias="matchers.fieldName")
        matchers.operator: Optional[str] = Field(alias="matchers.operator")
        matchers.value: Optional[str] = Field(alias="matchers.value")
        matchers: Optional[list[dict]] = Field(alias="matchers")
        metric_threshold.metric_name: Optional[str] = Field(alias="metricThreshold.metricName")
        metric_threshold.mode: Optional[str] = Field(alias="metricThreshold.mode")
        metric_threshold.operator: Optional[str] = Field(alias="metricThreshold.operator")
        metric_threshold.threshold: Optional[float] = Field(alias="metricThreshold.threshold")
        metric_threshold.units: Optional[str] = Field(alias="metricThreshold.units")
        metric_threshold: Optional[dict] = Field(alias="metricThreshold")
        notifications.api_token: Optional[str] = Field(alias="notifications.apiToken")
        notifications.channel_name: Optional[str] = Field(alias="notifications.channelName")
        notifications.datadog_api_key: Optional[str] = Field(alias="notifications.datadogApiKey")
        notifications.delay_min: Optional[float] = Field(alias="notifications.delayMin")
        notifications.email_address: Optional[str] = Field(alias="notifications.emailAddress")
        notifications.email_enabled: Optional[bool] = Field(alias="notifications.emailEnabled")
        notifications.interval_min: Optional[float] = Field(alias="notifications.intervalMin")
        notifications.webhook_secret: Optional[str] = Field(alias="notifications.webhookSecret")
        notifications.webhook_url: Optional[str] = Field(alias="notifications.webhookUrl")
        notifications.webhook_headers_template: Optional[str] = Field(alias="notifications.webhookHeadersTemplate")
        notifications.webhook_body_template: Optional[str] = Field(alias="notifications.webhookBodyTemplate")
        notifications.microsoft_teams_webhook_url: Optional[str] = Field(alias="notifications.microsoftTeamsWebhookUrl")
        notifications.mobile_number: Optional[str] = Field(alias="notifications.mobileNumber")
        notifications.notification_token: Optional[str] = Field(alias="notifications.notificationToken")
        notifications.role: Optional[str] = Field(alias="notifications.role")
        notifications.room_name: Optional[str] = Field(alias="notifications.roomName")
        notifications.service_key: Optional[str] = Field(alias="notifications.serviceKey")
        notifications.sms_enabled: Optional[bool] = Field(alias="notifications.smsEnabled")
        notifications.team_id: Optional[str] = Field(alias="notifications.teamId")
        notifications.type_name: Optional[str] = Field(alias="notifications.typeName")
        notifications.username: Optional[str] = Field(alias="notifications.username")
        notifications: list[dict] = Field(alias="notifications")
        threshold.operator: Optional[str] = Field(alias="threshold.operator")
        threshold.threshold: Optional[float] = Field(alias="threshold.threshold")
        threshold: Optional[dict] = Field(alias="threshold")
    def create(self,
        path_params: CreatePathParams,
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """API: Create an Alert Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-create-config/
        Description: No description found."""
        return self._request(
            "POST",
            "/groups/{PROJECT-ID}/alertConfigs",
            path_params,
            query_params,
            body_params,
        )
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
        alert_config_id: str = Field(alias="ALERT-CONFIG-ID")
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
        """API: Delete an Alert Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-delete-config/
        Description: No description found."""
        return self._request(
            "DELETE",
            "/groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )
    class EnableDisablePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
        alert_config_id: str = Field(alias="ALERT-CONFIG-ID")
    class EnableDisableQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class EnableDisableBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        enabled: Optional[bool] = Field(alias="enabled")
    def enable_disable(self,
        path_params: EnableDisablePathParams,
        query_params: Optional[EnableDisableQueryParams],
        body_params: Optional[EnableDisableBodyParams],
    ) -> dict[str, Any]:
        """API: Enable/Disable Alert Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-enable-disable-config/
        Description: No description found."""
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )
    class GetAllForAProjectPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
    class GetAllForAProjectQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetAllForAProjectBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all_for_a_project(self,
        path_params: GetAllForAProjectPathParams,
        query_params: Optional[GetAllForAProjectQueryParams],
        body_params: Optional[GetAllForAProjectBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Alert Configurations for a Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-get-all-configs/
        Description: No description found."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/alertConfigs",
            path_params,
            query_params,
            body_params,
        )
    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
        alert_config_id: str = Field(alias="ALERT-CONFIG-ID")
    class GetOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetOneBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_one(self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
        body_params: Optional[GetOneBodyParams],
    ) -> dict[str, Any]:
        """API: Get an Alert Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-get-config/
        Description: No description found."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )
    class GetMatchersFieldNamesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class GetMatchersFieldNamesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetMatchersFieldNamesBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_matchers_field_names(self,
        path_params: Optional[GetMatchersFieldNamesPathParams],
        query_params: Optional[GetMatchersFieldNamesQueryParams],
        body_params: Optional[GetMatchersFieldNamesBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Alert Configuration Matchers Field Names
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-get-matchers-field-names/
        Description: No description found."""
        return self._request(
            "GET",
            "/alertConfigs/matchers/fieldNames",
            path_params,
            query_params,
            body_params,
        )
    class GetOpenAlertsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
        alert_config_id: str = Field(alias="ALERT-CONFIG-ID")
    class GetOpenAlertsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetOpenAlertsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_open_alerts(self,
        path_params: GetOpenAlertsPathParams,
        query_params: Optional[GetOpenAlertsQueryParams],
        body_params: Optional[GetOpenAlertsBodyParams],
    ) -> dict[str, Any]:
        """API: Get Open Alerts for Alert Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-get-open-alerts/
        Description: No description found."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}/alerts",
            path_params,
            query_params,
            body_params,
        )
    class TestProjectAlertConfigurationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field(alias="GROUP-ID")
        alert_config_id: str = Field(alias="ALERT-CONFIG-ID")
        notification_id: str = Field(alias="NOTIFICATION-ID")
    class TestProjectAlertConfigurationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class TestProjectAlertConfigurationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def test_project_alert_configuration(self,
        path_params: TestProjectAlertConfigurationPathParams,
        query_params: Optional[TestProjectAlertConfigurationQueryParams],
        body_params: Optional[TestProjectAlertConfigurationBodyParams],
    ) -> dict[str, Any]:
        """API: Test Project Alert Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-test-config/
        Description: Triggers a test notification for a specific notification method in a project alert configuration. This endpoint sends a test payload with dummy data and rendered templates to validate your webhook configuration."""
        return self._request(
            "POST",
            "/api/public/v1.0/groups/{GROUP-ID}/alertConfigs/{ALERT-CONFIG-ID}/{NOTIFICATION-ID}/test",
            path_params,
            query_params,
            body_params,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
        alert_config_id: str = Field(alias="ALERT-CONFIG-ID")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        enabled: Optional[bool] = Field(alias="enabled")
        event_type_name: str = Field(alias="eventTypeName")
        matchers.field_name: Optional[str] = Field(alias="matchers.fieldName")
        matchers.operator: Optional[str] = Field(alias="matchers.operator")
        matchers.value: Optional[str] = Field(alias="matchers.value")
        matchers: Optional[list[dict]] = Field(alias="matchers")
        metric_threshold.metric_name: Optional[str] = Field(alias="metricThreshold.metricName")
        metric_threshold.mode: Optional[str] = Field(alias="metricThreshold.mode")
        metric_threshold.operator: Optional[str] = Field(alias="metricThreshold.operator")
        metric_threshold.threshold: Optional[float] = Field(alias="metricThreshold.threshold")
        metric_threshold.units: Optional[str] = Field(alias="metricThreshold.units")
        metric_threshold: Optional[dict] = Field(alias="metricThreshold")
        notifications.api_token: Optional[str] = Field(alias="notifications.apiToken")
        notifications.channel_name: Optional[str] = Field(alias="notifications.channelName")
        notifications.datadog_api_key: Optional[str] = Field(alias="notifications.datadogApiKey")
        notifications.delay_min: Optional[float] = Field(alias="notifications.delayMin")
        notifications.email_address: Optional[str] = Field(alias="notifications.emailAddress")
        notifications.email_enabled: Optional[bool] = Field(alias="notifications.emailEnabled")
        notifications.interval_min: Optional[float] = Field(alias="notifications.intervalMin")
        notifications.webhook_secret: Optional[str] = Field(alias="notifications.webhookSecret")
        notifications.webhook_url: Optional[str] = Field(alias="notifications.webhookUrl")
        notifications.webhook_headers_template: Optional[str] = Field(alias="notifications.webhookHeadersTemplate")
        notifications.webhook_body_template: Optional[str] = Field(alias="notifications.webhookBodyTemplate")
        notifications.microsoft_teams_webhook_url: Optional[str] = Field(alias="notifications.microsoftTeamsWebhookUrl")
        notifications.mobile_number: Optional[str] = Field(alias="notifications.mobileNumber")
        notifications.notification_token: Optional[str] = Field(alias="notifications.notificationToken")
        notifications.role: Optional[str] = Field(alias="notifications.role")
        notifications.room_name: Optional[str] = Field(alias="notifications.roomName")
        notifications.service_key: Optional[str] = Field(alias="notifications.serviceKey")
        notifications.sms_enabled: Optional[bool] = Field(alias="notifications.smsEnabled")
        notifications.team_id: Optional[str] = Field(alias="notifications.teamId")
        notifications.type_name: Optional[str] = Field(alias="notifications.typeName")
        notifications.username: Optional[str] = Field(alias="notifications.username")
        notifications: list[dict] = Field(alias="notifications")
        threshold.operator: Optional[str] = Field(alias="threshold.operator")
        threshold.threshold: Optional[float] = Field(alias="threshold.threshold")
        threshold: Optional[dict] = Field(alias="threshold")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: UpdateBodyParams,
    ) -> dict[str, Any]:
        """API: Update an Alert Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-update-config/
        Description: No description found."""
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )