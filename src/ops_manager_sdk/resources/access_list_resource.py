from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class AccessListResource(BaseResource):
    """Client for AccessListResource resource."""
    class AddEntriesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        user_id: str = Field(alias="USER-ID")
    class AddEntriesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class AddEntriesBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        ip_address: str = Field(alias="ipAddress")
    def add_entries(self,
        path_params: AddEntriesPathParams,
        query_params: Optional[AddEntriesQueryParams],
        body_params: AddEntriesBodyParams,
    ) -> dict[str, Any]:
        """API: Add Entries to an Access List
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/access-list-add-entries/
        Description: No description found."""
        return self._request(
            "POST",
            "/users/{USER-ID}/accessList",
            path_params,
            query_params,
            body_params,
        )
    class DeleteEntryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        user_id: str = Field(alias="USER-ID")
        access_list_entry: str = Field(alias="ACCESS-LIST-ENTRY")
    class DeleteEntryQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class DeleteEntryBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def delete_entry(self,
        path_params: DeleteEntryPathParams,
        query_params: Optional[DeleteEntryQueryParams],
        body_params: Optional[DeleteEntryBodyParams],
    ) -> dict[str, Any]:
        """API: Delete One Entry from One Access List
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/access-list-delete-entry/
        Description: No description found."""
        return self._request(
            "DELETE",
            "/users/{USER-ID}/accessList/{ACCESS-LIST-ENTRY}",
            path_params,
            query_params,
            body_params,
        )
    class GetForCurrentUserPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        user_id: str = Field(alias="USER-ID")
    class GetForCurrentUserQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetForCurrentUserBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_for_current_user(self,
        path_params: GetForCurrentUserPathParams,
        query_params: Optional[GetForCurrentUserQueryParams],
        body_params: Optional[GetForCurrentUserBodyParams],
    ) -> dict[str, Any]:
        """API: Get Access List for the Current User
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/access-list-get-for-current-user/
        Description: No description found."""
        return self._request(
            "GET",
            "/users/{USER-ID}/accessList",
            path_params,
            query_params,
            body_params,
        )
    class GetForIpAddressPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        user_id: str = Field(alias="USER-ID")
        access_list_entry: str = Field(alias="ACCESS-LIST-ENTRY")
    class GetForIpAddressQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetForIpAddressBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_for_ip_address(self,
        path_params: GetForIpAddressPathParams,
        query_params: Optional[GetForIpAddressQueryParams],
        body_params: Optional[GetForIpAddressBodyParams],
    ) -> dict[str, Any]:
        """API: Get Access List for an IP Address
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/access-list-get-for-ip-address/
        Description: Retrieves an access list entity if the value of IP-ADDRESS equals the value of the entity's ipAddress field. This does not retrieve an object where the value of IP-ADDRESS is contained within the values allowed by the cidrBlock field."""
        return self._request(
            "GET",
            "/users/{USER-ID}/accessList/{ACCESS-LIST-ENTRY}",
            path_params,
            query_params,
            body_params,
        )