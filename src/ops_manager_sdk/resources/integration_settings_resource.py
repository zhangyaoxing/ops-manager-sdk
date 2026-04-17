from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class IntegrationSettingsResource(BaseResource):
    """Client for IntegrationSettingsResource resource."""
    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
        integration_type: str = Field(alias="INTEGRATION-TYPE")
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pager_duty: Optional[Any] = Field(alias="PagerDuty")
        slack: Optional[Any] = Field(alias="Slack")
        datadog: Optional[Any] = Field(alias="Datadog")
        hip_chat: Optional[Any] = Field(alias="HipChat")
        opsgenie: Optional[Any] = Field(alias="Opsgenie")
        victor_ops: Optional[Any] = Field(alias="VictorOps")
        webhook _settings: Optional[Any] = Field(alias="Webhook Settings")
        microsoft _teams: Optional[Any] = Field(alias="Microsoft Teams")
        prometheus: Optional[Any] = Field(alias="Prometheus")
    def create(self,
        path_params: CreatePathParams,
        query_params: Optional[CreateQueryParams],
        body_params: Optional[CreateBodyParams],
    ) -> dict[str, Any]:
        """API: Create a Configuration for a Third-Party Service Integration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/third-party-integration-settings-create/
        Description: No description found."""
        return self._request(
            "POST",
            "/groups/{GROUP-ID}/integrations/{INTEGRATION-TYPE}",
            path_params,
            query_params,
            body_params,
        )
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
        integration_type: str = Field(alias="INTEGRATION-TYPE")
    class DeleteQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class DeleteBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def delete(self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
        body_params: Optional[DeleteBodyParams],
    ) -> dict[str, Any]:
        """API: Delete a Configuration for a Third-Party Service Integration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/third-party-integration-settings-delete/
        Description: No description found."""
        return self._request(
            "DELETE",
            "/groups/{GROUP-ID}/integrations/{INTEGRATION-TYPE}",
            path_params,
            query_params,
            body_params,
        )
    class ReturnLatestPrometheusTargetsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
    class ReturnLatestPrometheusTargetsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class ReturnLatestPrometheusTargetsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def return_latest_prometheus_targets(self,
        path_params: ReturnLatestPrometheusTargetsPathParams,
        query_params: Optional[ReturnLatestPrometheusTargetsQueryParams],
        body_params: Optional[ReturnLatestPrometheusTargetsBodyParams],
    ) -> dict[str, Any]:
        """API: Return the Latest Targets for Prometheus
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/third-party-integration-settings-discovery/
        Description: No description found."""
        return self._request(
            "GET",
            "/groups/{GROUP-ID}/discovery",
            path_params,
            query_params,
            body_params,
        )
    class GetAllConfigurationsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
    class GetAllConfigurationsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetAllConfigurationsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all_configurations(self,
        path_params: GetAllConfigurationsPathParams,
        query_params: Optional[GetAllConfigurationsQueryParams],
        body_params: Optional[GetAllConfigurationsBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Configurations for Third-Party Service Integrations
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/third-party-integration-settings-get-all/
        Description: No description found."""
        return self._request(
            "GET",
            "/api/public/v1.0/groups/{GROUP-ID}/integrations",
            path_params,
            query_params,
            body_params,
        )
    class GetOneConfigurationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
        integration_type: str = Field(alias="INTEGRATION-TYPE")
    class GetOneConfigurationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetOneConfigurationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_one_configuration(self,
        path_params: GetOneConfigurationPathParams,
        query_params: Optional[GetOneConfigurationQueryParams],
        body_params: Optional[GetOneConfigurationBodyParams],
    ) -> dict[str, Any]:
        """API: Get the Configuration of a Third-Party Service Integration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/third-party-integration-settings-get-one/
        Description: No description found."""
        return self._request(
            "GET",
            "/groups/{GROUP-ID}/integrations/{INTEGRATION-TYPE}",
            path_params,
            query_params,
            body_params,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
        integration_type: str = Field(alias="INTEGRATION-TYPE")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pager_duty: Optional[Any] = Field(alias="PagerDuty")
        slack: Optional[Any] = Field(alias="Slack")
        datadog: Optional[Any] = Field(alias="Datadog")
        hip_chat: Optional[Any] = Field(alias="HipChat")
        opsgenie: Optional[Any] = Field(alias="Opsgenie")
        victor_ops: Optional[Any] = Field(alias="VictorOps")
        webhook _settings: Optional[Any] = Field(alias="Webhook Settings")
        microsoft _teams: Optional[Any] = Field(alias="Microsoft Teams")
        prometheus: Optional[Any] = Field(alias="Prometheus")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """API: Update a Configuration for a Third-Party Service Integration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/third-party-integration-settings-update/
        Description: No description found."""
        return self._request(
            "PUT",
            "/groups/{GROUP-ID}/integrations/{INTEGRATION-TYPE}",
            path_params,
            query_params,
            body_params,
        )