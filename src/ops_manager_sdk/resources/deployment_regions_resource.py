from typing import Any, Optional
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
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class AssignBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        class DeploymentconfigsParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            deployment_id: str = Field("None", serialization_alias="deploymentId")
            rs_id: str = Field("None", serialization_alias="rsId")
        deployment_configs: list[DeploymentconfigsParams] = Field(serialization_alias="deploymentConfigs")
        multi_region_backup_enabled: bool = Field(serialization_alias="multiRegionBackupEnabled")
    def assign(self,
        path_params: AssignPathParams,
        query_params: Optional[AssignQueryParams],
        body_params: AssignBodyParams,
    ) -> dict[str, Any]:
        """
        ## Assign Deployment Region to One Shard
        - Document: [Assign](https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/assign-deployment-region/)
        - Resource: `PATCH /groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}`
        - Description: No description."""
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
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
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
        """
        ## Create One Deployment Region by ID
        - Document: [Create by ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/create-one-deployment-region-by-id/)
        - Resource: `PUT /admin/backup/backupDeployments/{DEPLOYMENT-ID}`
        - Description: No description."""
        return self._request(
            "PUT",
            "/admin/backup/backupDeployments/{DEPLOYMENT-ID}",
            path_params,
            query_params,
            body_params,
        )
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
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
        """
        ## Create One Deployment Region
        - Document: [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/create-one-deployment-region/)
        - Resource: `POST /admin/backup/backupDeployments`
        - Description: No description."""
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
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def delete(self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
    ) -> dict[str, Any]:
        """
        ## Delete One Deployment Region by ID
        - Document: [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/delete-one-deployment-region-by-id/)
        - Resource: `DELETE /admin/backup/backupDeployments/{DEPLOYMENT-ID}`
        - Description: No description."""
        return self._request(
            "DELETE",
            "/admin/backup/backupDeployments/{DEPLOYMENT-ID}",
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
        ## Get All Deployment Regions
        - Document: [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/get-all-deployment-regions/)
        - Resource: `GET /admin/backup/backupDeployments`
        - Description: No description."""
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
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_one(self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Deployment Region
        - Document: [Get One](https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/get-one-deployment-region-by-id/)
        - Resource: `GET /admin/backup/backupDeployments/{DEPLOYMENT-ID}`
        - Description: No description."""
        return self._request(
            "GET",
            "/admin/backup/backupDeployments/{DEPLOYMENT-ID}",
            path_params,
            query_params,
            None,
        )