from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class GlobalAccessListResource(BaseResource):
    """Client for GlobalAccessListResource resource."""
    class CreateEntryQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class CreateEntryBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        cidr_block: str = Field("None", serialization_alias="cidrBlock")
        description: str = Field("None", serialization_alias="description")
    def create_entry(self,
        query_params: Optional[CreateEntryQueryParams],
        body_params: CreateEntryBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create One Global Access List Entry
        - Document: [Create Entry](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/create-one-global-access-list/)
        - Resource: `POST /admin/accessList`
        - Description: Create one Global Access List Entry for Ops Manager."""
        return self._request(
            "POST",
            "/admin/accessList",
            None,
            query_params,
            body_params,
        )
    class DeleteEntryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        access_list_id: str = Field("None", serialization_alias="ACCESS-LIST-ID")
    class DeleteEntryQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def delete_entry(self,
        path_params: DeleteEntryPathParams,
        query_params: Optional[DeleteEntryQueryParams],
    ) -> dict[str, Any]:
        """
        ## Delete One Access List Entry for a Global API Key
        - Document: [Delete Entry](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/delete-one-global-access-list/)
        - Resource: `DELETE /admin/accessList/{ACCESS-LIST-ID}`
        - Description: Delete one Global Access List Entry from Ops Manager using the unique identifier for the desired IP address."""
        return self._request(
            "DELETE",
            "/admin/accessList/{ACCESS-LIST-ID}",
            path_params,
            query_params,
            None,
        )
    class GetAllEntriesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_all_entries(self,
        query_params: Optional[GetAllEntriesQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Access List Entries for a Global API Key
        - Document: [Get All Entries](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/get-all-global-access-list/)
        - Resource: `GET /admin/accessList`
        - Description: Return all Global Access List Entries for Ops Manager."""
        return self._request(
            "GET",
            "/admin/accessList",
            None,
            query_params,
            None,
        )
    class GetOneEntryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        access_list_id: str = Field("None", serialization_alias="ACCESS-LIST-ID")
    class GetOneEntryQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_one_entry(self,
        path_params: GetOneEntryPathParams,
        query_params: Optional[GetOneEntryQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Global Access List Entry
        - Document: [Get One Entry](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/get-one-global-access-list/)
        - Resource: `GET /admin/accessList/{ACCESS-LIST-ID}`
        - Description: Return one Global Access List Entry using the unique identifier for the desired IP address."""
        return self._request(
            "GET",
            "/admin/accessList/{ACCESS-LIST-ID}",
            path_params,
            query_params,
            None,
        )
    class UpdateEntryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        access_list_id: str = Field("None", serialization_alias="ACCESS-LIST-ID")
    class UpdateEntryQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def update_entry(self,
        path_params: UpdateEntryPathParams,
        query_params: Optional[UpdateEntryQueryParams],
    ) -> dict[str, Any]:
        """
        ## Update One Global Access List Entry
        - Document: [Update Entry](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/update-one-global-access-list/)
        - Resource: `PATCH /admin/accessList/{ACCESS-LIST-ID}`
        - Description: Update the values of one Global Access List Entry using the unique identifier for the desired IP address."""
        return self._request(
            "PATCH",
            "/admin/accessList/{ACCESS-LIST-ID}",
            path_params,
            query_params,
            None,
        )