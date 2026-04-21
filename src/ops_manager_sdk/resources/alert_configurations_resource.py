from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class AlertConfigurationsResource(BaseResource):
    """Client for AlertConfigurationsResource resource."""
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        alert_config_id: str = Field("None", serialization_alias="ALERT-CONFIG-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class DeleteQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def delete(self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
    ) -> dict[str, Any]:
        """
        ## Delete an Alert Configuration
        - Document: [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-delete-config/)
        - Resource: `DELETE /groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}`
        - Description: No description."""
        return self._request(
            "DELETE",
            "/groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}",
            path_params,
            query_params,
            None,
        )
    class EnableDisablePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        alert_config_id: str = Field("None", serialization_alias="ALERT-CONFIG-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class EnableDisableQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class EnableDisableBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        enabled: Optional[bool] = Field(serialization_alias="enabled")
    def enable_disable(self,
        path_params: EnableDisablePathParams,
        query_params: Optional[EnableDisableQueryParams],
        body_params: Optional[EnableDisableBodyParams],
    ) -> dict[str, Any]:
        """
        ## Enable/Disable Alert Configuration
        - Document: [Enable/Disable](https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-enable-disable-config/)
        - Resource: `PATCH /groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}`
        - Description: No description."""
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )
    class GetAllForAProjectPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetAllForAProjectQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_all_for_a_project(self,
        path_params: GetAllForAProjectPathParams,
        query_params: Optional[GetAllForAProjectQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Alert Configurations for a Project
        - Document: [Get All for a Project](https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-get-all-configs/)
        - Resource: `GET /groups/{PROJECT-ID}/alertConfigs`
        - Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/alertConfigs",
            path_params,
            query_params,
            None,
        )
    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        alert_config_id: str = Field("None", serialization_alias="ALERT-CONFIG-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_one(self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get an Alert Configuration
        - Document: [Get One](https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-get-config/)
        - Resource: `GET /groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}`
        - Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}",
            path_params,
            query_params,
            None,
        )
    class GetMatchersFieldNamesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_matchers_field_names(self,
        query_params: Optional[GetMatchersFieldNamesQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Alert Configuration Matchers Field Names
        - Document: [Get Matchers Field Names](https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-get-matchers-field-names/)
        - Resource: `GET /alertConfigs/matchers/fieldNames`
        - Description: No description."""
        return self._request(
            "GET",
            "/alertConfigs/matchers/fieldNames",
            None,
            query_params,
            None,
        )
    class GetOpenAlertsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        alert_config_id: str = Field("None", serialization_alias="ALERT-CONFIG-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetOpenAlertsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_open_alerts(self,
        path_params: GetOpenAlertsPathParams,
        query_params: Optional[GetOpenAlertsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Open Alerts for Alert Configuration
        - Document: [Get Open Alerts](https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-get-open-alerts/)
        - Resource: `GET /groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}/alerts`
        - Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}/alerts",
            path_params,
            query_params,
            None,
        )
    class TestProjectAlertConfigurationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        alert_config_id: str = Field("None", serialization_alias="ALERT-CONFIG-ID")
        group_id: str = Field("None", serialization_alias="GROUP-ID")
        notification_id: str = Field("None", serialization_alias="NOTIFICATION-ID")
    def test_project_alert_configuration(self,
        path_params: TestProjectAlertConfigurationPathParams,
    ) -> dict[str, Any]:
        """
        ## Test Project Alert Configuration
        - Document: [Test Project Alert Configuration](https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-test-config/)
        - Resource: `POST /api/public/v1.0/groups/{GROUP-ID}/alertConfigs/{ALERT-CONFIG-ID}/{NOTIFICATION-ID}/test`
        - Description: Triggers a test notification for a specific notification method in a project alert configuration. This endpoint sends a test payload with dummy data and rendered templates to validate your webhook configuration."""
        return self._request(
            "POST",
            "/api/public/v1.0/groups/{GROUP-ID}/alertConfigs/{ALERT-CONFIG-ID}/{NOTIFICATION-ID}/test",
            path_params,
            None,
            None,
        )
    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        enabled: Optional[bool] = Field(serialization_alias="enabled")
        event_type_name: str = Field("None", serialization_alias="eventTypeName")
        class MatchersParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            field_name: Optional[str] = Field("None", serialization_alias="fieldName")
            operator: Optional[str] = Field("None", serialization_alias="operator")
            value: Optional[str] = Field("None", serialization_alias="value")
        matchers: Optional[list[MatchersParams]] = Field(serialization_alias="matchers")
        class MetricthresholdParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            metric_name: Optional[str] = Field("None", serialization_alias="metricName")
            mode: Optional[str] = Field("None", serialization_alias="mode")
            operator: Optional[str] = Field("None", serialization_alias="operator")
            threshold: Optional[float] = Field(serialization_alias="threshold")
            units: Optional[str] = Field("None", serialization_alias="units")
        metric_threshold: Optional[MetricthresholdParams] = Field(serialization_alias="metricThreshold")
        class NotificationsParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            api_token: Optional[str] = Field("None", serialization_alias="apiToken")
            channel_name: Optional[str] = Field("None", serialization_alias="channelName")
            datadog_api_key: Optional[str] = Field("None", serialization_alias="datadogApiKey")
            delay_min: Optional[float] = Field(serialization_alias="delayMin")
            email_address: Optional[str] = Field("None", serialization_alias="emailAddress")
            email_enabled: Optional[bool] = Field(serialization_alias="emailEnabled")
            interval_min: Optional[float] = Field(serialization_alias="intervalMin")
            microsoft_teams_webhook_url: Optional[str] = Field("None", serialization_alias="microsoftTeamsWebhookUrl")
            mobile_number: Optional[str] = Field("None", serialization_alias="mobileNumber")
            notification_token: Optional[str] = Field("None", serialization_alias="notificationToken")
            role: Optional[str] = Field("None", serialization_alias="role")
            room_name: Optional[str] = Field("None", serialization_alias="roomName")
            service_key: Optional[str] = Field("None", serialization_alias="serviceKey")
            sms_enabled: Optional[bool] = Field(serialization_alias="smsEnabled")
            team_id: Optional[str] = Field("None", serialization_alias="teamId")
            type_name: Optional[str] = Field("None", serialization_alias="typeName")
            username: Optional[str] = Field("None", serialization_alias="username")
            webhook_body_template: Optional[str] = Field("None", serialization_alias="webhookBodyTemplate")
            webhook_headers_template: Optional[str] = Field("None", serialization_alias="webhookHeadersTemplate")
            webhook_secret: Optional[str] = Field("None", serialization_alias="webhookSecret")
            webhook_url: Optional[str] = Field("None", serialization_alias="webhookUrl")
        notifications: list[NotificationsParams] = Field(serialization_alias="notifications")
        class ThresholdParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            operator: Optional[str] = Field("None", serialization_alias="operator")
            threshold: Optional[float] = Field(serialization_alias="threshold")
        threshold: Optional[ThresholdParams] = Field(serialization_alias="threshold")
    def create(self,
        path_params: CreatePathParams,
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create an Alert Configuration
        - Document: [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-create-config/)
        - Resource: `POST /groups/{PROJECT-ID}/alertConfigs`
        - Description: No description."""
        return self._request(
            "POST",
            "/groups/{PROJECT-ID}/alertConfigs",
            path_params,
            query_params,
            body_params,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        alert_config_id: str = Field("None", serialization_alias="ALERT-CONFIG-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        enabled: Optional[bool] = Field(serialization_alias="enabled")
        event_type_name: str = Field("None", serialization_alias="eventTypeName")
        class MatchersParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            field_name: Optional[str] = Field("None", serialization_alias="fieldName")
            operator: Optional[str] = Field("None", serialization_alias="operator")
            value: Optional[str] = Field("None", serialization_alias="value")
        matchers: Optional[list[MatchersParams]] = Field(serialization_alias="matchers")
        class MetricthresholdParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            metric_name: Optional[str] = Field("None", serialization_alias="metricName")
            mode: Optional[str] = Field("None", serialization_alias="mode")
            operator: Optional[str] = Field("None", serialization_alias="operator")
            threshold: Optional[float] = Field(serialization_alias="threshold")
            units: Optional[str] = Field("None", serialization_alias="units")
        metric_threshold: Optional[MetricthresholdParams] = Field(serialization_alias="metricThreshold")
        class NotificationsParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            api_token: Optional[str] = Field("None", serialization_alias="apiToken")
            channel_name: Optional[str] = Field("None", serialization_alias="channelName")
            datadog_api_key: Optional[str] = Field("None", serialization_alias="datadogApiKey")
            delay_min: Optional[float] = Field(serialization_alias="delayMin")
            email_address: Optional[str] = Field("None", serialization_alias="emailAddress")
            email_enabled: Optional[bool] = Field(serialization_alias="emailEnabled")
            interval_min: Optional[float] = Field(serialization_alias="intervalMin")
            microsoft_teams_webhook_url: Optional[str] = Field("None", serialization_alias="microsoftTeamsWebhookUrl")
            mobile_number: Optional[str] = Field("None", serialization_alias="mobileNumber")
            notification_token: Optional[str] = Field("None", serialization_alias="notificationToken")
            role: Optional[str] = Field("None", serialization_alias="role")
            room_name: Optional[str] = Field("None", serialization_alias="roomName")
            service_key: Optional[str] = Field("None", serialization_alias="serviceKey")
            sms_enabled: Optional[bool] = Field(serialization_alias="smsEnabled")
            team_id: Optional[str] = Field("None", serialization_alias="teamId")
            type_name: Optional[str] = Field("None", serialization_alias="typeName")
            username: Optional[str] = Field("None", serialization_alias="username")
            webhook_body_template: Optional[str] = Field("None", serialization_alias="webhookBodyTemplate")
            webhook_headers_template: Optional[str] = Field("None", serialization_alias="webhookHeadersTemplate")
            webhook_secret: Optional[str] = Field("None", serialization_alias="webhookSecret")
            webhook_url: Optional[str] = Field("None", serialization_alias="webhookUrl")
        notifications: list[NotificationsParams] = Field(serialization_alias="notifications")
        class ThresholdParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            operator: Optional[str] = Field("None", serialization_alias="operator")
            threshold: Optional[float] = Field(serialization_alias="threshold")
        threshold: Optional[ThresholdParams] = Field(serialization_alias="threshold")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: UpdateBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update an Alert Configuration
        - Document: [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/alert-configurations-update-config/)
        - Resource: `PUT /groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}`
        - Description: No description."""
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )