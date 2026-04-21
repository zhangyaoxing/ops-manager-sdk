from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class GlobalAlertConfigurationsResource(BaseResource):
    """Client for GlobalAlertConfigurationsResource resource."""
    class GetAllOpenAlertsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        global_alert_config_id: str = Field("None", serialization_alias="GLOBAL-ALERT-CONFIG-ID")
    class GetAllOpenAlertsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_all_open_alerts(self,
        path_params: GetAllOpenAlertsPathParams,
        query_params: Optional[GetAllOpenAlertsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Open Alerts Triggered by One Global Alert Configuration
        - Document: [Get All Open Alerts](https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configuration-get-all-open-alerts-triggered/)
        - Resource: `GET /globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}/alerts`
        - Description: Retrieve all open alerts triggered by a global alert configuration identified by its GLOBAL-ALERT-CONFIG-ID."""
        return self._request(
            "GET",
            "/globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}/alerts",
            path_params,
            query_params,
            None,
        )
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        enabled: Optional[bool] = Field(serialization_alias="enabled")
        event_type_name: str = Field("None", serialization_alias="eventTypeName")
        for_all_groups: bool = Field(serialization_alias="forAllGroups")
        group_ids: Optional[list[str]] = Field(serialization_alias="groupIds")
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
            delay_min: Optional[float] = Field(serialization_alias="delayMin")
            email_address: Optional[Any] = Field(serialization_alias="emailAddress")
            email_enabled: Optional[bool] = Field(serialization_alias="emailEnabled")
            interval_min: Optional[float] = Field(serialization_alias="intervalMin")
            microsoft_teams_webhook_url: Optional[str] = Field("None", serialization_alias="microsoftTeamsWebhookUrl")
            notification_token: Optional[str] = Field("None", serialization_alias="notificationToken")
            room_name: Optional[str] = Field("None", serialization_alias="roomName")
            service_key: Optional[str] = Field("None", serialization_alias="serviceKey")
            sms_enabled: Optional[bool] = Field(serialization_alias="smsEnabled")
            type_name: str = Field("None", serialization_alias="typeName")
            username: Optional[str] = Field("None", serialization_alias="username")
            webhook_body_template: Optional[str] = Field("None", serialization_alias="webhookBodyTemplate")
            webhook_headers_template: Optional[str] = Field("None", serialization_alias="webhookHeadersTemplate")
            webhook_secret: Optional[str] = Field("None", serialization_alias="webhookSecret")
            webhook_url: Optional[str] = Field("None", serialization_alias="webhookUrl")
        notifications: list[NotificationsParams] = Field(serialization_alias="notifications")
        tags: Optional[list[str]] = Field(serialization_alias="tags")
        class ThresholdParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            operator: Optional[str] = Field("None", serialization_alias="operator")
            threshold: Optional[float] = Field(serialization_alias="threshold")
        threshold: Optional[ThresholdParams] = Field(serialization_alias="threshold")
        type_name: Optional[str] = Field("None", serialization_alias="typeName")
    def create(self,
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create One Global Alert Configuration
        - Document: [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configurations-create-one/)
        - Resource: `POST /globalAlertConfigs`
        - Description: Create one global alert configuration."""
        return self._request(
            "POST",
            "/globalAlertConfigs",
            None,
            query_params,
            body_params,
        )
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        global_alert_config_id: str = Field("None", serialization_alias="GLOBAL-ALERT-CONFIG-ID")
    class DeleteQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def delete(self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
    ) -> dict[str, Any]:
        """
        ## Delete One Global Alert Configuration
        - Document: [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configurations-delete-one/)
        - Resource: `DELETE /globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}`
        - Description: Delete one global alert configuration."""
        return self._request(
            "DELETE",
            "/globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}",
            path_params,
            query_params,
            None,
        )
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_all(self,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Global Alert Configurations
        - Document: [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configurations-get-all/)
        - Resource: `GET /globalAlertConfigs`
        - Description: Retrieve all global alert configurations."""
        return self._request(
            "GET",
            "/globalAlertConfigs",
            None,
            query_params,
            None,
        )
    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        global_alert_config_id: str = Field("None", serialization_alias="GLOBAL-ALERT-CONFIG-ID")
    class GetOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_one(self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Global Alert Configuration
        - Document: [Get One](https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configurations-get-one/)
        - Resource: `GET /globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}`
        - Description: Retrieve one global alert configuration by its GLOBAL-ALERT-CONFIG-ID."""
        return self._request(
            "GET",
            "/globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}",
            path_params,
            query_params,
            None,
        )
    class TestGlobalAlertConfigurationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        alert_config_id: str = Field("None", serialization_alias="ALERT-CONFIG-ID")
        notification_id: str = Field("None", serialization_alias="NOTIFICATION-ID")
    def test_global_alert_configuration(self,
        path_params: TestGlobalAlertConfigurationPathParams,
    ) -> dict[str, Any]:
        """
        ## Test Global Alert Configuration
        - Document: [Test Global Alert Configuration](https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configurations-test-one/)
        - Resource: `POST /api/public/v1.0/globalAlertConfigs/{ALERT-CONFIG-ID}/{NOTIFICATION-ID}/test`
        - Description: Triggers a test notification for a specific notification method in a global alert configuration. This endpoint sends a test payload with dummy data and rendered templates to validate your webhook configuration."""
        return self._request(
            "POST",
            "/api/public/v1.0/globalAlertConfigs/{ALERT-CONFIG-ID}/{NOTIFICATION-ID}/test",
            path_params,
            None,
            None,
        )
    class EnableOrDisablePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        global_alert_config_id: str = Field("None", serialization_alias="GLOBAL-ALERT-CONFIG-ID")
    class EnableOrDisableQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class EnableOrDisableBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        enabled: bool = Field(serialization_alias="enabled")
    def enable_or_disable(self,
        path_params: EnableOrDisablePathParams,
        query_params: Optional[EnableOrDisableQueryParams],
        body_params: EnableOrDisableBodyParams,
    ) -> dict[str, Any]:
        """
        ## Enable or Disable One Global Alert Configuration
        - Document: [Enable or Disable](https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configurations-toggle-one/)
        - Resource: `PATCH /globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}`
        - Description: Enable or disable one global alert configuration identified by its GLOBAL-ALERT-CONFIG-ID."""
        return self._request(
            "PATCH",
            "/globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        global_alert_config_id: str = Field("None", serialization_alias="GLOBAL-ALERT-CONFIG-ID")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        enabled: Optional[bool] = Field(serialization_alias="enabled")
        event_type_name: str = Field("None", serialization_alias="eventTypeName")
        for_all_groups: bool = Field(serialization_alias="forAllGroups")
        group_ids: Optional[list[str]] = Field(serialization_alias="groupIds")
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
            delay_min: Optional[float] = Field(serialization_alias="delayMin")
            email_address: Optional[Any] = Field(serialization_alias="emailAddress")
            email_enabled: Optional[bool] = Field(serialization_alias="emailEnabled")
            interval_min: Optional[float] = Field(serialization_alias="intervalMin")
            microsoft_teams_webhook_url: Optional[str] = Field("None", serialization_alias="microsoftTeamsWebhookUrl")
            notification_token: Optional[str] = Field("None", serialization_alias="notificationToken")
            room_name: Optional[str] = Field("None", serialization_alias="roomName")
            service_key: Optional[str] = Field("None", serialization_alias="serviceKey")
            sms_enabled: Optional[bool] = Field(serialization_alias="smsEnabled")
            type_name: str = Field("None", serialization_alias="typeName")
            username: Optional[str] = Field("None", serialization_alias="username")
            webhook_body_template: Optional[str] = Field("None", serialization_alias="webhookBodyTemplate")
            webhook_headers_template: Optional[str] = Field("None", serialization_alias="webhookHeadersTemplate")
            webhook_secret: Optional[str] = Field("None", serialization_alias="webhookSecret")
            webhook_url: Optional[str] = Field("None", serialization_alias="webhookUrl")
        notifications: list[NotificationsParams] = Field(serialization_alias="notifications")
        tags: Optional[list[str]] = Field(serialization_alias="tags")
        class ThresholdParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            operator: Optional[str] = Field("None", serialization_alias="operator")
            threshold: Optional[float] = Field(serialization_alias="threshold")
        threshold: Optional[ThresholdParams] = Field(serialization_alias="threshold")
        type_name: Optional[str] = Field("None", serialization_alias="typeName")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: UpdateBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update One Global Alert Configuration
        - Document: [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alert-configurations-update-one/)
        - Resource: `PUT /globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}`
        - Description: Update one global alert configuration identified by its GLOBAL-ALERT-CONFIG-ID."""
        return self._request(
            "PUT",
            "/globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )