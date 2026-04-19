from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class GlobalAccessListResource(BaseResource):
    """Client for GlobalAccessListResource resource."""
    class CreateEntryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class CreateEntryQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class CreateEntryBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        description: str = Field("None", serialization_alias="description")
        cidr_block: str = Field("None", serialization_alias="cidrBlock")
    def create_entry(self,
        path_params: Optional[CreateEntryPathParams],
        query_params: Optional[CreateEntryQueryParams],
        body_params: CreateEntryBodyParams,
    ) -> dict[str, Any]:
        """API: Create One Global Access List Entry
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/create-one-global-access-list/
        Description: Create one Global Access List Entry for Ops Manager."""
        return self._request(
            "POST",
            "/admin/accessList",
            path_params,
            query_params,
            body_params,
        )
    class DeleteEntryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        access_list_id: str = Field("None", serialization_alias="ACCESS-LIST-ID")
    class DeleteEntryQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class DeleteEntryBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def delete_entry(self,
        path_params: DeleteEntryPathParams,
        query_params: Optional[DeleteEntryQueryParams],
        body_params: Optional[DeleteEntryBodyParams],
    ) -> dict[str, Any]:
        """API: Delete One Access List Entry for a Global API Key
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/delete-one-global-access-list/
        Description: Delete one Global Access List Entry from Ops Manager using the unique identifier for the desired IP address."""
        return self._request(
            "DELETE",
            "/admin/accessList/{ACCESS-LIST-ID}",
            path_params,
            query_params,
            body_params,
        )
    class GetAllEntriesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class GetAllEntriesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class GetAllEntriesBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all_entries(self,
        path_params: Optional[GetAllEntriesPathParams],
        query_params: Optional[GetAllEntriesQueryParams],
        body_params: Optional[GetAllEntriesBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Access List Entries for a Global API Key
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/get-all-global-access-list/
        Description: Return all Global Access List Entries for Ops Manager."""
        return self._request(
            "GET",
            "/admin/accessList",
            path_params,
            query_params,
            body_params,
        )
    class GetOneEntryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        access_list_id: str = Field("None", serialization_alias="ACCESS-LIST-ID")
    class GetOneEntryQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class GetOneEntryBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_one_entry(self,
        path_params: GetOneEntryPathParams,
        query_params: Optional[GetOneEntryQueryParams],
        body_params: Optional[GetOneEntryBodyParams],
    ) -> dict[str, Any]:
        """API: Get One Global Access List Entry
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/get-one-global-access-list/
        Description: Return one Global Access List Entry using the unique identifier for the desired IP address."""
        return self._request(
            "GET",
            "/admin/accessList/{ACCESS-LIST-ID}",
            path_params,
            query_params,
            body_params,
        )
    class UpdateEntryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        access_list_id: str = Field("None", serialization_alias="ACCESS-LIST-ID")
    class UpdateEntryQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class UpdateEntryBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def update_entry(self,
        path_params: UpdateEntryPathParams,
        query_params: Optional[UpdateEntryQueryParams],
        body_params: Optional[UpdateEntryBodyParams],
    ) -> dict[str, Any]:
        """API: Update One Global Access List Entry
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/update-one-global-access-list/
        Description: Update the values of one Global Access List Entry using the unique identifier for the desired IP address."""
        return self._request(
            "PATCH",
            "/admin/accessList/{ACCESS-LIST-ID}",
            path_params,
            query_params,
            body_params,
        )