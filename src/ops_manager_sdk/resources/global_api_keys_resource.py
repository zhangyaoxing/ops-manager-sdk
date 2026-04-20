from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class GlobalApiKeysResource(BaseResource):
    """Client for GlobalApiKeysResource resource."""
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        desc: str = Field("None", serialization_alias="desc")
        roles: list[str] = Field(serialization_alias="roles")
    def create(self,
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """API: Create One Global API Key
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/create-one-global-api-key/
        Description: Create one Global API Key for Ops Manager."""
        return self._request(
            "POST",
            "/admin/apiKeys",
            None,
            query_params,
            body_params,
        )
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        api_key_id: str = Field("None", serialization_alias="API-KEY-ID")
    class DeleteQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def delete(self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
    ) -> dict[str, Any]:
        """API: Delete One Global API Key
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/delete-one-global-api-key/
        Description: Delete one Global API Key from Ops Manager using the unique identifier for that Key."""
        return self._request(
            "DELETE",
            "/admin/apiKeys/{API-KEY-ID}",
            path_params,
            query_params,
            None,
        )
    class GetAllRolesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
    def get_all_roles(self,
        query_params: Optional[GetAllRolesQueryParams],
    ) -> dict[str, Any]:
        """API: Get All Roles for Global API Keys
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/get-all-global-api-key-roles/
        Description: Return a list of acceptable Global Roles for Global API Keys."""
        return self._request(
            "GET",
            "/admin/apiKeys/roles",
            None,
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
        """API: Get All Global API Keys
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/get-all-global-api-keys/
        Description: Return all Global API Keys for Ops Manager."""
        return self._request(
            "GET",
            "/admin/apiKeys",
            None,
            query_params,
            None,
        )
    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        api_key_id: str = Field("None", serialization_alias="API-KEY-ID")
    class GetOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_one(self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
    ) -> dict[str, Any]:
        """API: Get One Global API Key
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/get-one-global-api-key/
        Description: Return one Global API Key for Ops Manager using the unique identifier for that Key."""
        return self._request(
            "GET",
            "/admin/apiKeys/{API-KEY-ID}",
            path_params,
            query_params,
            None,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        api_key_id: str = Field("None", serialization_alias="API-KEY-ID")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        desc: Optional[str] = Field("None", serialization_alias="desc")
        roles: Optional[list[str]] = Field(serialization_alias="roles")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """API: Update One Global API Key
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/update-one-global-api-key/
        Description: Update values of one Global API Key from Ops Manager using the unique identifier for that Key."""
        return self._request(
            "PATCH",
            "/admin/apiKeys/{API-KEY-ID}",
            path_params,
            query_params,
            body_params,
        )