from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class OrganizationAccessListsResource(BaseResource):
    """Client for OrganizationAccessListsResource resource."""
    class CreateEntriesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        api_key_id: str = Field("None", serialization_alias="API-KEY-ID")
        """Unique identifier for the Organization API Key for which you want to create a new access list entry."""
        org_id: str = Field("None", serialization_alias="ORG-ID")
        """Unique identifier for the organization to which the target API Key belongs. Use the /orgs endpoint to retrieve all organizations to which the authenticated user has access."""
    class CreateEntriesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        """None"""
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        """100"""
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        """1"""
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        """false"""
    class CreateEntriesBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        cidr_block: Optional[str] = Field("None", serialization_alias="cidrBlock")
        """Access list entry in CIDR notation to be added for the API key. This field is mutually exclusive with the ipAddress field."""
        ip_address: Optional[str] = Field("None", serialization_alias="ipAddress")
        """IP address to be added to the access list for the API key. This field is mutually exclusive with the cidrBlock field."""
    def create_entries(self,
        path_params: CreateEntriesPathParams,
        query_params: Optional[CreateEntriesQueryParams],
        body_params: list[Optional[CreateEntriesBodyParams]],
    ) -> dict[str, Any]:
        """
        ## Create Access List Entries for One Organization API Key
        - Document: [Create Entries](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/org/create-org-api-key-access-list/)
        - Resource: `POST /orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList`
        - Description: No description."""
        return self._request(
            "POST",
            "/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList",
            path_params,
            query_params,
            body_params,
        )
    class DeleteEntryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        access_list_entry: str = Field("None", serialization_alias="ACCESS-LIST-ENTRY")
        """The IP or CIDR address. If the entry includes a subnet mask, such as 192.0.2.0/24, use the URL-encoded value %2F for the forward slash /."""
        api_key_id: str = Field("None", serialization_alias="API-KEY-ID")
        """Unique identifier for the API key for which you want to retrieve access list entries. Request the /orgs/{ORG-ID}/apiKeys endpoint to retrieve all API keys for the specified organization to which the authenticated user has access."""
        org_id: str = Field("None", serialization_alias="ORG-ID")
        """Unique identifier for the organization to which the target API key belongs. Request the /orgs endpoint to retrieve all organizations to which the authenticated user has access."""
    class DeleteEntryQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        """None"""
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        """100"""
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        """1"""
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        """false"""
    def delete_entry(self,
        path_params: DeleteEntryPathParams,
        query_params: Optional[DeleteEntryQueryParams],
    ) -> dict[str, Any]:
        """
        ## Delete One Access List Entry for an API Key
        - Document: [Delete Entry](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/org/delete-one-org-api-key-access-list/)
        - Resource: `DELETE /orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList/{ACCESS-LIST-ENTRY}`
        - Description: No description."""
        return self._request(
            "DELETE",
            "/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList/{ACCESS-LIST-ENTRY}",
            path_params,
            query_params,
            None,
        )
    class GetAllEntriesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        api_key_id: str = Field("None", serialization_alias="API-KEY-ID")
        """Unique identifier for the API Key for which you want to retrieve access list entries. Request the /orgs/{ORG-ID}/apiKeys endpoint to retrieve all API keys for the specified organization to which the authenticated user has access."""
        org_id: str = Field("None", serialization_alias="ORG-ID")
        """Unique identifier for the organization to which the target API Key belongs. Request the /orgs endpoint to retrieve all organizations to which the authenticated user has access."""
    class GetAllEntriesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        """None"""
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        """100"""
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        """1"""
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        """false"""
    def get_all_entries(self,
        path_params: GetAllEntriesPathParams,
        query_params: Optional[GetAllEntriesQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Access List Entries for One Organization API Key
        - Document: [Get All Entries](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/org/get-all-org-api-key-access-list/)
        - Resource: `GET /orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList`
        - Description: No description."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList",
            path_params,
            query_params,
            None,
        )
    class GetOneEntryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        access_list_entry: str = Field("None", serialization_alias="ACCESS-LIST-ENTRY")
        """The IP or CIDR address. If the entry includes a subnet mask, such as 192.0.2.0/24, use the URL-encoded value %2F for the forward slash /."""
        api_key_id: str = Field("None", serialization_alias="API-KEY-ID")
        """Unique identifier for the API Key for which you want to retrieve access list entries. Request the /orgs/{ORG-ID}/apiKeys endpoint to retrieve all API keys for the specified organization to which the authenticated user has access."""
        org_id: str = Field("None", serialization_alias="ORG-ID")
        """Unique identifier for the organization to which the target API Key belongs. Request the /orgs endpoint to retrieve all organizations to which the authenticated user has access."""
    class GetOneEntryQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        """None"""
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        """100"""
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        """1"""
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        """false"""
    def get_one_entry(self,
        path_params: GetOneEntryPathParams,
        query_params: Optional[GetOneEntryQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Access List Entry for One Organization API Key
        - Document: [Get One Entry](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/org/get-one-org-api-key-access-list/)
        - Resource: `GET /orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList/{ACCESS-LIST-ENTRY}`
        - Description: No description."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList/{ACCESS-LIST-ENTRY}",
            path_params,
            query_params,
            None,
        )