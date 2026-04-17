from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class FileSystemStoreResource(BaseResource):
    """Client for FileSystemStoreResource resource."""
    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        assignment_enabled: Optional[bool] = Field(alias="assignmentEnabled")
        id: str = Field(alias="id")
        labels: Optional[list[str]] = Field(alias="labels")
        load_factor: Optional[float] = Field(alias="loadFactor")
        mmapv1_compression_setting: Optional[str] = Field(alias="mmapv1CompressionSetting")
        store_path: str = Field(alias="storePath")
        wt_compression_setting: Optional[str] = Field(alias="wtCompressionSetting")
    def create(self,
        path_params: Optional[CreatePathParams],
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """API: Create One File System Store Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/fileSystemConfigs/create-one-file-system-store-configuration/
        Description: Configures one new file system store."""
        return self._request(
            "POST",
            "/snapshot/fileSystemConfigs",
            path_params,
            query_params,
            body_params,
        )
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        file_system_config_id: str = Field(alias="FILE-SYSTEM-CONFIG-ID")
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
        """API: Delete One File System Store Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/fileSystemConfigs/delete-one-file-system-store-configuration/
        Description: Deletes the configuration of one file system store."""
        return self._request(
            "DELETE",
            "/snapshot/fileSystemConfigs/{FILE-SYSTEM-CONFIG-ID}",
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
        assignable_only: Optional[bool] = Field(True, alias="assignableOnly")
    class GetAllBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all(self,
        path_params: Optional[GetAllPathParams],
        query_params: Optional[GetAllQueryParams],
        body_params: Optional[GetAllBodyParams],
    ) -> dict[str, Any]:
        """API: Get All File System Store Configurations
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/fileSystemConfigs/get-all-file-system-store-configurations/
        Description: Retrieves the configurations of all file system stores."""
        return self._request(
            "GET",
            "/snapshot/fileSystemConfigs",
            path_params,
            query_params,
            body_params,
        )
    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        file_system_config_id: str = Field(alias="FILE-SYSTEM-CONFIG-ID")
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
        """API: Get One File System Store Configuration by ID
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/fileSystemConfigs/get-one-file-system-store-configuration-by-id/
        Description: Retrieves the configuration of one file system store."""
        return self._request(
            "GET",
            "/snapshot/fileSystemConfigs/{FILE-SYSTEM-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        file_system_config_id: str = Field(alias="FILE-SYSTEM-CONFIG-ID")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        assignment_enabled: Optional[bool] = Field(alias="assignmentEnabled")
        labels: Optional[list[str]] = Field(alias="labels")
        load_factor: Optional[float] = Field(alias="loadFactor")
        mmapv1_compression_setting: Optional[str] = Field(alias="mmapv1CompressionSetting")
        store_path: str = Field(alias="storePath")
        wt_compression_setting: Optional[str] = Field(alias="wtCompressionSetting")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: UpdateBodyParams,
    ) -> dict[str, Any]:
        """API: Update One File System Store Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/fileSystemConfigs/update-one-file-system-store-configuration/
        Description: Updates the configuration of one file system store."""
        return self._request(
            "PUT",
            "/snapshot/fileSystemConfigs/{FILE-SYSTEM-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )