from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class BlockstoreResource(BaseResource):
    """Client for BlockstoreResource resource."""
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        assignment_enabled: Optional[bool] = Field(serialization_alias="assignmentEnabled")
        encrypted_credentials: Optional[bool] = Field(serialization_alias="encryptedCredentials")
        id: Optional[str] = Field("None", serialization_alias="id")
        labels: Optional[list[str]] = Field(serialization_alias="labels")
        load_factor: Optional[float] = Field(serialization_alias="loadFactor")
        max_capacity_gb: Optional[float] = Field(serialization_alias="maxCapacityGB")
        uri: Optional[str] = Field("None", serialization_alias="uri")
        ssl: Optional[bool] = Field(serialization_alias="ssl")
        write_concern: Optional[str] = Field("None", serialization_alias="writeConcern")
    def create(self,
        query_params: Optional[CreateQueryParams],
        body_params: Optional[CreateBodyParams],
    ) -> dict[str, Any]:
        """API: Create One Blockstore Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/mongoConfigs/create-one-blockstore-configuration/
        Description: Configures one new blockstore."""
        return self._request(
            "POST",
            "/snapshot/mongoConfigs",
            None,
            query_params,
            body_params,
        )
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        blockstore_id: str = Field("None", serialization_alias="BLOCKSTORE-ID")
    class DeleteQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def delete(self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
    ) -> dict[str, Any]:
        """API: Delete One Blockstore Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/mongoConfigs/delete-one-blockstore-configuration/
        Description: Deletes the configuration of one blockstore."""
        return self._request(
            "DELETE",
            "/snapshot/mongoConfigs/{BLOCKSTORE-ID}",
            path_params,
            query_params,
            None,
        )
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        assignable_only: Optional[bool] = Field(serialization_alias="assignableOnly")
    def get_all(self,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """API: Get All Blockstore Configurations
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/mongoConfigs/get-all-blockstore-configurations/
        Description: Retrieves the configurations of all blockstores."""
        return self._request(
            "GET",
            "/snapshot/mongoConfigs",
            None,
            query_params,
            None,
        )
    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        blockstore_id: str = Field("None", serialization_alias="BLOCKSTORE-ID")
    class GetByIdQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_by_id(self,
        path_params: GetByIdPathParams,
        query_params: Optional[GetByIdQueryParams],
    ) -> dict[str, Any]:
        """API: Get One Blockstore Configuration by ID
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/mongoConfigs/get-one-blockstore-configuration-by-id/
        Description: Retrieves the configuration of one blockstore."""
        return self._request(
            "GET",
            "/snapshot/mongoConfigs/{BLOCKSTORE-ID}",
            path_params,
            query_params,
            None,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        blockstore_id: str = Field("None", serialization_alias="BLOCKSTORE-ID")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        assignment_enabled: Optional[bool] = Field(serialization_alias="assignmentEnabled")
        encrypted_credentials: Optional[bool] = Field(serialization_alias="encryptedCredentials")
        labels: Optional[list[str]] = Field(serialization_alias="labels")
        load_factor: Optional[float] = Field(serialization_alias="loadFactor")
        max_capacity_gb: Optional[float] = Field(serialization_alias="maxCapacityGB")
        uri: Optional[str] = Field("None", serialization_alias="uri")
        ssl: Optional[bool] = Field(serialization_alias="ssl")
        write_concern: Optional[str] = Field("None", serialization_alias="writeConcern")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """API: Update One Blockstore Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/mongoConfigs/update-one-blockstore-configuration/
        Description: Updates the configuration of one blockstore."""
        return self._request(
            "PUT",
            "/snapshot/mongoConfigs/{BLOCKSTORE-ID}",
            path_params,
            query_params,
            body_params,
        )