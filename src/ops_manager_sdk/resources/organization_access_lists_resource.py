from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class OrganizationAccessListsResource(BaseResource):
    """Client for OrganizationAccessListsResource resource."""
    class CreateEntriesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
        api_key_id: str = Field("None", serialization_alias="API-KEY-ID")
    class CreateEntriesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
    def create_entries(self,
        path_params: CreateEntriesPathParams,
        query_params: Optional[CreateEntriesQueryParams],
    ) -> dict[str, Any]:
        """API: Create Access List Entries for One Organization API Key
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/org/create-org-api-key-access-list/
        Description: No description."""
        return self._request(
            "POST",
            "/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList",
            path_params,
            query_params,
            None,
        )
    class DeleteEntryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
        api_key_id: str = Field("None", serialization_alias="API-KEY-ID")
        access_list_entry: str = Field("None", serialization_alias="ACCESS-LIST-ENTRY")
    class DeleteEntryQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
    def delete_entry(self,
        path_params: DeleteEntryPathParams,
        query_params: Optional[DeleteEntryQueryParams],
    ) -> dict[str, Any]:
        """API: Delete One Access List Entry for an API Key
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/org/delete-one-org-api-key-access-list/
        Description: No description."""
        return self._request(
            "DELETE",
            "/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList/{ACCESS-LIST-ENTRY}",
            path_params,
            query_params,
            None,
        )
    class GetAllEntriesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
        api_key_id: str = Field("None", serialization_alias="API-KEY-ID")
    class GetAllEntriesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
    def get_all_entries(self,
        path_params: GetAllEntriesPathParams,
        query_params: Optional[GetAllEntriesQueryParams],
    ) -> dict[str, Any]:
        """API: Get All Access List Entries for One Organization API Key
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/org/get-all-org-api-key-access-list/
        Description: No description."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList",
            path_params,
            query_params,
            None,
        )
    class GetOneEntryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
        api_key_id: str = Field("None", serialization_alias="API-KEY-ID")
        access_list_entry: str = Field("None", serialization_alias="ACCESS-LIST-ENTRY")
    class GetOneEntryQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
    def get_one_entry(self,
        path_params: GetOneEntryPathParams,
        query_params: Optional[GetOneEntryQueryParams],
    ) -> dict[str, Any]:
        """API: Get One Access List Entry for One Organization API Key
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/org/get-one-org-api-key-access-list/
        Description: No description."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList/{ACCESS-LIST-ENTRY}",
            path_params,
            query_params,
            None,
        )