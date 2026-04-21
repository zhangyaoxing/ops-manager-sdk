from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class ClustersResource(BaseResource):
    """Client for ClustersResource resource."""
    class GetAllFromAllProjectsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_all_from_all_projects(self,
        query_params: Optional[GetAllFromAllProjectsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Clusters in All Projects
        - Document: [Get All from All Projects](https://www.mongodb.com/docs/ops-manager/current/reference/api/clusters/clusters-get-all-key/)
        - Resource: `GET /api/public/v1.0/clusters`
        - Description: Get details for all clusters in all projects available to the programmatic API key making the request."""
        return self._request(
            "GET",
            "/api/public/v1.0/clusters",
            None,
            query_params,
            None,
        )
    class GetAllFromOneProjectPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetAllFromOneProjectQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_all_from_one_project(self,
        path_params: GetAllFromOneProjectPathParams,
        query_params: Optional[GetAllFromOneProjectQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Clusters in One Project
        - Document: [Get All from One Project](https://www.mongodb.com/docs/ops-manager/current/reference/api/clusters/clusters-get-all/)
        - Resource: `GET /groups/{PROJECT-ID}/clusters`
        - Description: Retrieve details for all clusters in one project."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/clusters",
            path_params,
            query_params,
            None,
        )
    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        cluster_id: str = Field("None", serialization_alias="clusterId")
    class GetOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_one(self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Cluster in One Project
        - Document: [Get One](https://www.mongodb.com/docs/ops-manager/current/reference/api/clusters/clusters-get-one/)
        - Resource: `GET /groups/{PROJECT-ID}/clusters/{CLUSTER-ID}`
        - Description: Retrieve details for one cluster in one project."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}",
            path_params,
            query_params,
            None,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        cluster_id: str = Field("None", serialization_alias="clusterId")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        cluster_name: str = Field("None", serialization_alias="clusterName")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: UpdateBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update One Cluster
        - Document: [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/clusters/clusters-update-one/)
        - Resource: `PATCH /groups/{PROJECT-ID}/clusters/{CLUSTER-ID}`
        - Description: Update one cluster in one project."""
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}",
            path_params,
            query_params,
            body_params,
        )