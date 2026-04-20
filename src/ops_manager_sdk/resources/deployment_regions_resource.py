from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class DeploymentRegionsResource(BaseResource):
    """Client for DeploymentRegionsResource resource."""
    class AssignPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        cluster_id: str = Field("None", serialization_alias="clusterId")
    class AssignQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class AssignBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        deployment_configs: list[dict] = Field(serialization_alias="deploymentConfigs")
        multi_region_backup_enabled: bool = Field(serialization_alias="multiRegionBackupEnabled")
    def assign(self,
        path_params: AssignPathParams,
        query_params: Optional[AssignQueryParams],
        body_params: AssignBodyParams,
    ) -> dict[str, Any]:
        """API: Assign Deployment Region to One Shard
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/assign-deployment-region/
        Description: No description."""
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}",
            path_params,
            query_params,
            body_params,
        )
    class CreateByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        deployment_id: str = Field("None", serialization_alias="DEPLOYMENT-ID")
    class CreateByIdQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class CreateByIdBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        assignment_enabled: Optional[bool] = Field(serialization_alias="assignmentEnabled")
        bq_proxy_endpoint: str = Field("None", serialization_alias="bqProxyEndpoint")
        deployment_description: str = Field("None", serialization_alias="deploymentDescription")
        ingestion_endpoint: Optional[str] = Field("None", serialization_alias="ingestionEndpoint")
        restore_endpoint: str = Field("None", serialization_alias="restoreEndpoint")
    def create_by_id(self,
        path_params: CreateByIdPathParams,
        query_params: Optional[CreateByIdQueryParams],
        body_params: CreateByIdBodyParams,
    ) -> dict[str, Any]:
        """API: Create One Deployment Region by ID
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/create-one-deployment-region-by-id/
        Description: No description."""
        return self._request(
            "PUT",
            "/admin/backup/backupDeployments/{DEPLOYMENT-ID}",
            path_params,
            query_params,
            body_params,
        )
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        assignment_enabled: Optional[bool] = Field(serialization_alias="assignmentEnabled")
        bq_proxy_endpoint: str = Field("None", serialization_alias="bqProxyEndpoint")
        deployment_description: str = Field("None", serialization_alias="deploymentDescription")
        id: Optional[str] = Field("None", serialization_alias="id")
        ingestion_endpoint: Optional[str] = Field("None", serialization_alias="ingestionEndpoint")
        restore_endpoint: str = Field("None", serialization_alias="restoreEndpoint")
    def create(self,
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """API: Create One Deployment Region
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/create-one-deployment-region/
        Description: No description."""
        return self._request(
            "POST",
            "/admin/backup/backupDeployments",
            None,
            query_params,
            body_params,
        )
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        deployment_id: str = Field("None", serialization_alias="DEPLOYMENT-ID")
    class DeleteQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def delete(self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
    ) -> dict[str, Any]:
        """API: Delete One Deployment Region by ID
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/delete-one-deployment-region-by-id/
        Description: No description."""
        return self._request(
            "DELETE",
            "/admin/backup/backupDeployments/{DEPLOYMENT-ID}",
            path_params,
            query_params,
            None,
        )
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_all(self,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """API: Get All Deployment Regions
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/get-all-deployment-regions/
        Description: No description."""
        return self._request(
            "GET",
            "/admin/backup/backupDeployments",
            None,
            query_params,
            None,
        )
    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        deployment_id: str = Field("None", serialization_alias="DEPLOYMENT-ID")
    class GetOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_one(self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
    ) -> dict[str, Any]:
        """API: Get One Deployment Region
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/get-one-deployment-region-by-id/
        Description: No description."""
        return self._request(
            "GET",
            "/admin/backup/backupDeployments/{DEPLOYMENT-ID}",
            path_params,
            query_params,
            None,
        )