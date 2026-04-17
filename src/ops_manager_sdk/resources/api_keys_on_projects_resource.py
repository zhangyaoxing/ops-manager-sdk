from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class ApiKeysOnProjectsResource(BaseResource):
    """Client for ApiKeysOnProjectsResource resource."""
    class AssignPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
        api_key_id: str = Field(alias="API-KEY-ID")
    class AssignQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(alias="pageNum")
        items_per_page: Optional[float] = Field(alias="itemsPerPage")
        pretty: Optional[bool] = Field(alias="pretty")
        envelope: Optional[bool] = Field(alias="envelope")
    class AssignBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        roles: list[Any] = Field(alias="roles")
    def assign(self,
        path_params: AssignPathParams,
        query_params: Optional[AssignQueryParams],
        body_params: AssignBodyParams,
    ) -> dict[str, Any]:
        """API: Assign One Organization API Key to One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/project/assign-one-org-apiKey-to-one-project/
        Description: No description found."""
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/apiKeys/{API-KEY-ID}",
            path_params,
            query_params,
            body_params,
        )
    class CreateAssignPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
    class CreateAssignQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(alias="pageNum")
        items_per_page: Optional[float] = Field(alias="itemsPerPage")
        pretty: Optional[bool] = Field(alias="pretty")
        envelope: Optional[bool] = Field(alias="envelope")
    class CreateAssignBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        desc: Optional[str] = Field(alias="desc")
        roles: Optional[list[str]] = Field(alias="roles")
    def create_assign(self,
        path_params: CreateAssignPathParams,
        query_params: Optional[CreateAssignQueryParams],
        body_params: Optional[CreateAssignBodyParams],
    ) -> dict[str, Any]:
        """API: Create and Assign One Organization API Key to One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/project/create-one-apiKey-in-one-project/
        Description: No description found."""
        return self._request(
            "POST",
            "/groups/{PROJECT-ID}/apiKeys",
            path_params,
            query_params,
            body_params,
        )
    class UnassignPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
        api_key_id: str = Field(alias="API-KEY-ID")
    class UnassignQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(alias="pageNum")
        items_per_page: Optional[float] = Field(alias="itemsPerPage")
        pretty: Optional[bool] = Field(alias="pretty")
        envelope: Optional[bool] = Field(alias="envelope")
    class UnassignBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def unassign(self,
        path_params: UnassignPathParams,
        query_params: Optional[UnassignQueryParams],
        body_params: Optional[UnassignBodyParams],
    ) -> dict[str, Any]:
        """API: Unassign One Organization API Key from One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/project/delete-one-apiKey-in-one-project/
        Description: No description found."""
        return self._request(
            "DELETE",
            "/orgs/{PROJECT-ID}/apiKeys/{API-KEY-ID}",
            path_params,
            query_params,
            body_params,
        )
    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(alias="pageNum")
        items_per_page: Optional[float] = Field(alias="itemsPerPage")
        pretty: Optional[bool] = Field(alias="pretty")
        envelope: Optional[bool] = Field(alias="envelope")
    class GetAllBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all(self,
        path_params: GetAllPathParams,
        query_params: Optional[GetAllQueryParams],
        body_params: Optional[GetAllBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Organization API Keys Assigned to One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/project/get-all-apiKeys-in-one-project/
        Description: No description found."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/apiKeys",
            path_params,
            query_params,
            body_params,
        )
    class ModifyRolesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
        api_key_id: str = Field(alias="API-KEY-ID")
    class ModifyRolesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(alias="pageNum")
        items_per_page: Optional[float] = Field(alias="itemsPerPage")
        pretty: Optional[bool] = Field(alias="pretty")
        envelope: Optional[bool] = Field(alias="envelope")
    class ModifyRolesBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        roles: list[str] = Field(alias="roles")
    def modify_roles(self,
        path_params: ModifyRolesPathParams,
        query_params: Optional[ModifyRolesQueryParams],
        body_params: ModifyRolesBodyParams,
    ) -> dict[str, Any]:
        """API: Modify Roles of One Organization API Key to One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/project/update-one-apiKey-in-one-project/
        Description: No description found."""
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/apiKeys/{API-KEY-ID}",
            path_params,
            query_params,
            body_params,
        )