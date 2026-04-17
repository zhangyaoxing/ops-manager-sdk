from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class OplogStoreResource(BaseResource):
    """Client for OplogStoreResource resource."""
    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        assignment_enabled: Optional[bool] = Field(alias="assignmentEnabled")
        encrypted_credentials: Optional[bool] = Field(alias="encryptedCredentials")
        id: Optional[str] = Field(alias="id")
        labels: Optional[list[str]] = Field(alias="labels")
        max_capacity_gb: Optional[float] = Field(alias="maxCapacityGB")
        uri: Optional[str] = Field(alias="uri")
        ssl: Optional[bool] = Field(alias="ssl")
        write_concern: Optional[str] = Field(alias="writeConcern")
    def create(self,
        path_params: Optional[CreatePathParams],
        query_params: Optional[CreateQueryParams],
        body_params: Optional[CreateBodyParams],
    ) -> dict[str, Any]:
        """API: Create One Oplog Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/oplog/mongoConfigs/create-one-oplog-configuration/
        Description: Configures one new oplog store."""
        return self._request(
            "POST",
            "/oplog/mongoConfigs",
            path_params,
            query_params,
            body_params,
        )
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        oplog_config_id: str = Field(alias="OPLOG-CONFIG-ID")
    class DeleteQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class DeleteBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def delete(self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
        body_params: Optional[DeleteBodyParams],
    ) -> dict[str, Any]:
        """API: Delete One Oplog Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/oplog/mongoConfigs/delete-one-oplog-configuration/
        Description: Deletes the configuration of one oplog store."""
        return self._request(
            "DELETE",
            "/oplog/mongoConfigs/{OPLOG-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )
    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
        assignable_only: Optional[bool] = Field(alias="assignableOnly")
    class GetAllBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all(self,
        path_params: Optional[GetAllPathParams],
        query_params: Optional[GetAllQueryParams],
        body_params: Optional[GetAllBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Oplog Configurations
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/oplog/mongoConfigs/get-all-oplog-configurations/
        Description: Retrieves the configurations of all oplog stores."""
        return self._request(
            "GET",
            "/oplog/mongoConfigs",
            path_params,
            query_params,
            body_params,
        )
    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        oplog_config_id: str = Field(alias="OPLOG-CONFIG-ID")
    class GetByIdQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetByIdBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_by_id(self,
        path_params: GetByIdPathParams,
        query_params: Optional[GetByIdQueryParams],
        body_params: Optional[GetByIdBodyParams],
    ) -> dict[str, Any]:
        """API: Get One Oplog Configuration by ID
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/oplog/mongoConfigs/get-one-oplog-configuration-by-id/
        Description: Retrieves the configuration of one oplog store."""
        return self._request(
            "GET",
            "/oplog/mongoConfigs/{OPLOG-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        oplog_config_id: str = Field(alias="OPLOG-CONFIG-ID")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        assignment_enabled: Optional[bool] = Field(alias="assignmentEnabled")
        encrypted_credentials: Optional[bool] = Field(alias="encryptedCredentials")
        labels: Optional[list[str]] = Field(alias="labels")
        max_capacity_gb: Optional[float] = Field(alias="maxCapacityGB")
        uri: Optional[str] = Field(alias="uri")
        ssl: Optional[bool] = Field(alias="ssl")
        write_concern: Optional[str] = Field(alias="writeConcern")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """API: Update One Oplog Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/oplog/mongoConfigs/update-one-oplog-configuration/
        Description: Updates the configuration of one oplog store."""
        return self._request(
            "PUT",
            "/oplog/mongoConfigs/{OPLOG-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )