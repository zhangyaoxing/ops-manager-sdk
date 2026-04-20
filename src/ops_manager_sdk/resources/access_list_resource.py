from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class AccessListResource(BaseResource):
    """Client for AccessListResource resource."""
    class AddEntriesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        user_id: str = Field("None", serialization_alias="USER-ID")
    class AddEntriesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class AddEntriesBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        ip_address: str = Field("None", serialization_alias="ipAddress")
    def add_entries(self,
        path_params: AddEntriesPathParams,
        query_params: Optional[AddEntriesQueryParams],
        body_params: list[AddEntriesBodyParams],
    ) -> dict[str, Any]:
        """API: Add Entries to an Access List
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/access-list-add-entries/
        Description: No description."""
        return self._request(
            "POST",
            "/users/{USER-ID}/accessList",
            path_params,
            query_params,
            body_params,
        )
    class DeleteEntryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        user_id: str = Field("None", serialization_alias="USER-ID")
        access_list_entry: str = Field("None", serialization_alias="ACCESS-LIST-ENTRY")
    class DeleteEntryQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def delete_entry(self,
        path_params: DeleteEntryPathParams,
        query_params: Optional[DeleteEntryQueryParams],
    ) -> dict[str, Any]:
        """API: Delete One Entry from One Access List
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/access-list-delete-entry/
        Description: No description."""
        return self._request(
            "DELETE",
            "/users/{USER-ID}/accessList/{ACCESS-LIST-ENTRY}",
            path_params,
            query_params,
            None,
        )
    class GetForCurrentUserPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        user_id: str = Field("None", serialization_alias="USER-ID")
    class GetForCurrentUserQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_for_current_user(self,
        path_params: GetForCurrentUserPathParams,
        query_params: Optional[GetForCurrentUserQueryParams],
    ) -> dict[str, Any]:
        """API: Get Access List for the Current User
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/access-list-get-for-current-user/
        Description: No description."""
        return self._request(
            "GET",
            "/users/{USER-ID}/accessList",
            path_params,
            query_params,
            None,
        )
    class GetForIpAddressPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        user_id: str = Field("None", serialization_alias="USER-ID")
        access_list_entry: str = Field("None", serialization_alias="ACCESS-LIST-ENTRY")
    class GetForIpAddressQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_for_ip_address(self,
        path_params: GetForIpAddressPathParams,
        query_params: Optional[GetForIpAddressQueryParams],
    ) -> dict[str, Any]:
        """API: Get Access List for an IP Address
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/access-list-get-for-ip-address/
        Description: Retrieves an access list entity if the value of IP-ADDRESS equals the value of the entity's ipAddress field. This does not retrieve an object where the value of IP-ADDRESS is contained within the values allowed by the cidrBlock field."""
        return self._request(
            "GET",
            "/users/{USER-ID}/accessList/{ACCESS-LIST-ENTRY}",
            path_params,
            query_params,
            None,
        )