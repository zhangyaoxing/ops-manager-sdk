from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class IntegrationSettingsResource(BaseResource):
    """Client for IntegrationSettingsResource resource."""
    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        integration_type: str = Field("None", serialization_alias="INTEGRATION-TYPE")
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pager_duty: Optional[Any] = Field(serialization_alias="PagerDuty")
        slack: Optional[Any] = Field(serialization_alias="Slack")
        datadog: Optional[Any] = Field(serialization_alias="Datadog")
        hip_chat: Optional[Any] = Field(serialization_alias="HipChat")
        opsgenie: Optional[Any] = Field(serialization_alias="Opsgenie")
        victor_ops: Optional[Any] = Field(serialization_alias="VictorOps")
        webhook_settings: Optional[Any] = Field(serialization_alias="Webhook Settings")
        microsoft_teams: Optional[Any] = Field(serialization_alias="Microsoft Teams")
        prometheus: Optional[Any] = Field(serialization_alias="Prometheus")
    def create(self,
        path_params: CreatePathParams,
        query_params: Optional[CreateQueryParams],
        body_params: Optional[CreateBodyParams],
    ) -> dict[str, Any]:
        """API: Create a Configuration for a Third-Party Service Integration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/third-party-integration-settings-create/
        Description: No description."""
        return self._request(
            "POST",
            "/groups/{GROUP-ID}/integrations/{INTEGRATION-TYPE}",
            path_params,
            query_params,
            body_params,
        )
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        integration_type: str = Field("None", serialization_alias="INTEGRATION-TYPE")
    class DeleteQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def delete(self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
    ) -> dict[str, Any]:
        """API: Delete a Configuration for a Third-Party Service Integration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/third-party-integration-settings-delete/
        Description: No description."""
        return self._request(
            "DELETE",
            "/groups/{GROUP-ID}/integrations/{INTEGRATION-TYPE}",
            path_params,
            query_params,
            None,
        )
    class ReturnLatestPrometheusTargetsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class ReturnLatestPrometheusTargetsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def return_latest_prometheus_targets(self,
        path_params: ReturnLatestPrometheusTargetsPathParams,
        query_params: Optional[ReturnLatestPrometheusTargetsQueryParams],
    ) -> dict[str, Any]:
        """API: Return the Latest Targets for Prometheus
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/third-party-integration-settings-discovery/
        Description: No description."""
        return self._request(
            "GET",
            "/groups/{GROUP-ID}/discovery",
            path_params,
            query_params,
            None,
        )
    class GetAllConfigurationsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetAllConfigurationsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_all_configurations(self,
        path_params: GetAllConfigurationsPathParams,
        query_params: Optional[GetAllConfigurationsQueryParams],
    ) -> dict[str, Any]:
        """API: Get All Configurations for Third-Party Service Integrations
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/third-party-integration-settings-get-all/
        Description: No description."""
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{GROUP-ID}/integrations",
            path_params,
            query_params,
            None,
        )
    class GetOneConfigurationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        integration_type: str = Field("None", serialization_alias="INTEGRATION-TYPE")
    class GetOneConfigurationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_one_configuration(self,
        path_params: GetOneConfigurationPathParams,
        query_params: Optional[GetOneConfigurationQueryParams],
    ) -> dict[str, Any]:
        """API: Get the Configuration of a Third-Party Service Integration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/third-party-integration-settings-get-one/
        Description: No description."""
        return self._request(
            "GET",
            "/groups/{GROUP-ID}/integrations/{INTEGRATION-TYPE}",
            path_params,
            query_params,
            None,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        integration_type: str = Field("None", serialization_alias="INTEGRATION-TYPE")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pager_duty: Optional[Any] = Field(serialization_alias="PagerDuty")
        slack: Optional[Any] = Field(serialization_alias="Slack")
        datadog: Optional[Any] = Field(serialization_alias="Datadog")
        hip_chat: Optional[Any] = Field(serialization_alias="HipChat")
        opsgenie: Optional[Any] = Field(serialization_alias="Opsgenie")
        victor_ops: Optional[Any] = Field(serialization_alias="VictorOps")
        webhook_settings: Optional[Any] = Field(serialization_alias="Webhook Settings")
        microsoft_teams: Optional[Any] = Field(serialization_alias="Microsoft Teams")
        prometheus: Optional[Any] = Field(serialization_alias="Prometheus")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """API: Update a Configuration for a Third-Party Service Integration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/third-party-integration-settings-update/
        Description: No description."""
        return self._request(
            "PUT",
            "/groups/{GROUP-ID}/integrations/{INTEGRATION-TYPE}",
            path_params,
            query_params,
            body_params,
        )