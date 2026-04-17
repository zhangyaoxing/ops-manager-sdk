from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class ClustersResource(BaseResource):
    """Client for ClustersResource resource."""
    class GetAllFromAllProjectsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class GetAllFromAllProjectsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetAllFromAllProjectsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all_from_all_projects(self,
        path_params: Optional[GetAllFromAllProjectsPathParams],
        query_params: Optional[GetAllFromAllProjectsQueryParams],
        body_params: Optional[GetAllFromAllProjectsBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Clusters in All Projects
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/clusters/clusters-get-all-key/
        Description: Get details for all clusters in all projects available to the programmatic API key making the request."""
        return self._request(
            "GET",
            "/api/public/v1.0/clusters",
            path_params,
            query_params,
            body_params,
        )
    class GetAllFromOneProjectPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
    class GetAllFromOneProjectQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetAllFromOneProjectBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all_from_one_project(self,
        path_params: GetAllFromOneProjectPathParams,
        query_params: Optional[GetAllFromOneProjectQueryParams],
        body_params: Optional[GetAllFromOneProjectBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Clusters in One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/clusters/clusters-get-all/
        Description: Retrieve details for all clusters in one project."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/clusters",
            path_params,
            query_params,
            body_params,
        )
    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
        cluster_id: str = Field("None", alias="clusterId")
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
        """API: Get One Cluster in One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/clusters/clusters-get-one/
        Description: Retrieve details for one cluster in one project."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}",
            path_params,
            query_params,
            body_params,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
        cluster_id: str = Field("None", alias="clusterId")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        cluster_name: str = Field("None", alias="clusterName")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: UpdateBodyParams,
    ) -> dict[str, Any]:
        """API: Update One Cluster
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/clusters/clusters-update-one/
        Description: Update one cluster in one project."""
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}",
            path_params,
            query_params,
            body_params,
        )