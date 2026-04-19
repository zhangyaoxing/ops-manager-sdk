from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class GlobalAlertConfigurationsResource(BaseResource):
    """Client for GlobalAlertConfigurationsResource resource."""
    class GetAllOpenAlertsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        global_alert_config_id: str = Field("None", serialization_alias="GLOBAL-ALERT-CONFIG-ID")
    class GetAllOpenAlertsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
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
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        enabled: Optional[bool] = Field(serialization_alias="enabled")
        event_type_name: str = Field("None", serialization_alias="eventTypeName")
        for_all_groups: bool = Field(serialization_alias="forAllGroups")
        group_ids: Optional[list[str]] = Field(serialization_alias="groupIds")
        matchers: Optional[list[dict]] = Field(serialization_alias="matchers")
        metric_threshold: Optional[dict] = Field(serialization_alias="metricThreshold")
        notifications: list[dict] = Field(serialization_alias="notifications")
        threshold: Optional[dict] = Field(serialization_alias="threshold")
        tags: Optional[list[str]] = Field(serialization_alias="tags")
        type_name: Optional[str] = Field("None", serialization_alias="typeName")
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
        global_alert_config_id: str = Field("None", serialization_alias="GLOBAL-ALERT-CONFIG-ID")
    class DeleteQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
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
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
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
        global_alert_config_id: str = Field("None", serialization_alias="GLOBAL-ALERT-CONFIG-ID")
    class GetOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
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
        alert_config_id: str = Field("None", serialization_alias="ALERT-CONFIG-ID")
        notification_id: str = Field("None", serialization_alias="NOTIFICATION-ID")
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
        global_alert_config_id: str = Field("None", serialization_alias="GLOBAL-ALERT-CONFIG-ID")
    class EnableOrDisableQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class EnableOrDisableBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        enabled: bool = Field(serialization_alias="enabled")
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
        global_alert_config_id: str = Field("None", serialization_alias="GLOBAL-ALERT-CONFIG-ID")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        enabled: Optional[bool] = Field(serialization_alias="enabled")
        event_type_name: str = Field("None", serialization_alias="eventTypeName")
        for_all_groups: bool = Field(serialization_alias="forAllGroups")
        group_ids: Optional[list[str]] = Field(serialization_alias="groupIds")
        matchers: Optional[list[dict]] = Field(serialization_alias="matchers")
        metric_threshold: Optional[dict] = Field(serialization_alias="metricThreshold")
        notifications: list[dict] = Field(serialization_alias="notifications")
        threshold: Optional[dict] = Field(serialization_alias="threshold")
        tags: Optional[list[str]] = Field(serialization_alias="tags")
        type_name: Optional[str] = Field("None", serialization_alias="typeName")
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