from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class ApiKeysOnProjectsResource(BaseResource):
    """Client for ApiKeysOnProjectsResource resource."""
    class AssignPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        api_key_id: str = Field("None", serialization_alias="API-KEY-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class AssignQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    class AssignBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        roles: list[Any] = Field(serialization_alias="roles")
    def assign(self,
        path_params: AssignPathParams,
        query_params: Optional[AssignQueryParams],
        body_params: AssignBodyParams,
    ) -> dict[str, Any]:
        """
        ## Assign One Organization API Key to One Project
        - Document: [Assign](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/project/assign-one-org-apiKey-to-one-project/)
        - Resource: `PATCH /groups/{PROJECT-ID}/apiKeys/{API-KEY-ID}`
        - Description: No description."""
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/apiKeys/{API-KEY-ID}",
            path_params,
            query_params,
            body_params,
        )
    class CreateAssignPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class CreateAssignQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    class CreateAssignBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        desc: Optional[str] = Field("None", serialization_alias="desc")
        roles: Optional[list[str]] = Field(serialization_alias="roles")
    def create_assign(self,
        path_params: CreateAssignPathParams,
        query_params: Optional[CreateAssignQueryParams],
        body_params: Optional[CreateAssignBodyParams],
    ) -> dict[str, Any]:
        """
        ## Create and Assign One Organization API Key to One Project
        - Document: [Create & Assign](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/project/create-one-apiKey-in-one-project/)
        - Resource: `POST /groups/{PROJECT-ID}/apiKeys`
        - Description: No description."""
        return self._request(
            "POST",
            "/groups/{PROJECT-ID}/apiKeys",
            path_params,
            query_params,
            body_params,
        )
    class UnassignPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        api_key_id: str = Field("None", serialization_alias="API-KEY-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class UnassignQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    def unassign(self,
        path_params: UnassignPathParams,
        query_params: Optional[UnassignQueryParams],
    ) -> dict[str, Any]:
        """
        ## Unassign One Organization API Key from One Project
        - Document: [Unassign](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/project/delete-one-apiKey-in-one-project/)
        - Resource: `DELETE /orgs/{PROJECT-ID}/apiKeys/{API-KEY-ID}`
        - Description: No description."""
        return self._request(
            "DELETE",
            "/orgs/{PROJECT-ID}/apiKeys/{API-KEY-ID}",
            path_params,
            query_params,
            None,
        )
    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    def get_all(self,
        path_params: GetAllPathParams,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Organization API Keys Assigned to One Project
        - Document: [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/project/get-all-apiKeys-in-one-project/)
        - Resource: `GET /groups/{PROJECT-ID}/apiKeys`
        - Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/apiKeys",
            path_params,
            query_params,
            None,
        )
    class ModifyRolesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        api_key_id: str = Field("None", serialization_alias="API-KEY-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class ModifyRolesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    class ModifyRolesBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        roles: list[str] = Field(serialization_alias="roles")
    def modify_roles(self,
        path_params: ModifyRolesPathParams,
        query_params: Optional[ModifyRolesQueryParams],
        body_params: ModifyRolesBodyParams,
    ) -> dict[str, Any]:
        """
        ## Modify Roles of One Organization API Key to One Project
        - Document: [Modify Roles](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/project/update-one-apiKey-in-one-project/)
        - Resource: `PATCH /groups/{PROJECT-ID}/apiKeys/{API-KEY-ID}`
        - Description: No description."""
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/apiKeys/{API-KEY-ID}",
            path_params,
            query_params,
            body_params,
        )