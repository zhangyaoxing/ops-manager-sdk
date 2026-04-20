from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class OrganizationApiKeysResource(BaseResource):
    """Client for OrganizationApiKeysResource resource."""
    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        desc: Optional[str] = Field("None", serialization_alias="desc")
        roles: Optional[list[str]] = Field(serialization_alias="roles")
    def create(self,
        path_params: CreatePathParams,
        query_params: Optional[CreateQueryParams],
        body_params: Optional[CreateBodyParams],
    ) -> dict[str, Any]:
        """API: Create an API Key
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/org/create-one-org-api-key/
        Description: No description."""
        return self._request(
            "POST",
            "/orgs/{ORG-ID}/apiKeys",
            path_params,
            query_params,
            body_params,
        )
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
        api_key_id: str = Field("None", serialization_alias="API-KEY-ID")
    class DeleteQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
    def delete(self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
    ) -> dict[str, Any]:
        """API: Delete One API Key
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/org/delete-one-api-key/
        Description: No description."""
        return self._request(
            "DELETE",
            "/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}",
            path_params,
            query_params,
            None,
        )
    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
    def get_all(self,
        path_params: GetAllPathParams,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """API: Get All API Keys
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/org/get-all-org-api-keys/
        Description: No description."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/apiKeys",
            path_params,
            query_params,
            None,
        )
    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
        api_key_id: str = Field("None", serialization_alias="API-KEY-ID")
    class GetOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
    def get_one(self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
    ) -> dict[str, Any]:
        """API: Get One API Key
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/org/get-one-org-api-key/
        Description: No description."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}",
            path_params,
            query_params,
            None,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
        api_key_id: str = Field("None", serialization_alias="API-KEY-ID")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        desc: Optional[str] = Field("None", serialization_alias="desc")
        roles: Optional[list[str]] = Field(serialization_alias="roles")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """API: Update an API Key
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/org/update-one-org-api-key/
        Description: No description."""
        return self._request(
            "PATCH",
            "/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}",
            path_params,
            query_params,
            body_params,
        )