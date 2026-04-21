from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class BackupDaemonResource(BaseResource):
    """Client for BackupDaemonResource resource."""
    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        machine: str = Field("None", serialization_alias="MACHINE")
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        assignment_enabled: Optional[bool] = Field(serialization_alias="assignmentEnabled")
        backup_jobs_enabled: Optional[bool] = Field(serialization_alias="backupJobsEnabled")
        configured: Optional[bool] = Field(serialization_alias="configured")
        garbage_collection_enabled: Optional[bool] = Field(serialization_alias="garbageCollectionEnabled")
        head_disk_type: Optional[str] = Field("None", serialization_alias="headDiskType")
        labels: Optional[list[str]] = Field(serialization_alias="labels")
        class MachineParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            head_root_directory: Optional[str] = Field("None", serialization_alias="headRootDirectory")
            machine: str = Field("None", serialization_alias="machine")
        machine: MachineParams = Field(serialization_alias="machine")
        num_workers: Optional[float] = Field(serialization_alias="numWorkers")
        resource_usage_enabled: Optional[bool] = Field(serialization_alias="resourceUsageEnabled")
        restore_queryable_jobs_enabled: Optional[bool] = Field(serialization_alias="restoreQueryableJobsEnabled")
    def create(self,
        path_params: CreatePathParams,
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """API: Create One Backup Daemon Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/daemonConfigs/create-one-backup-daemon-configuration/
        Description: Configures a new Backup Daemon."""
        return self._request(
            "PUT",
            "/daemon/configs/{MACHINE}",
            path_params,
            query_params,
            body_params,
        )
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        head_root_directory: str = Field("None", serialization_alias="HEAD-ROOT-DIRECTORY")
        machine: str = Field("None", serialization_alias="MACHINE")
    class DeleteQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def delete(self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
    ) -> dict[str, Any]:
        """API: Delete One Backup Daemon Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/daemonConfigs/delete-one-backup-daemon-configuration/
        Description: Deletes the configuration of one backup daemon."""
        return self._request(
            "DELETE",
            "/daemon/configs/{MACHINE}/{HEAD-ROOT-DIRECTORY}",
            path_params,
            query_params,
            None,
        )
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        backup_jobs_enabled_only: Optional[bool] = Field(True, serialization_alias="backupJobsEnabledOnly")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_all(self,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """API: Get All Backup Daemon Configurations
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/daemonConfigs/get-all-backup-daemon-configurations/
        Description: Retrieves the configurations of all backup daemons."""
        return self._request(
            "GET",
            "/daemon/configs",
            None,
            query_params,
            None,
        )
    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        head_root_directory: str = Field("None", serialization_alias="HEAD-ROOT-DIRECTORY")
        machine: str = Field("None", serialization_alias="MACHINE")
    class GetByIdQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_by_id(self,
        path_params: GetByIdPathParams,
        query_params: Optional[GetByIdQueryParams],
    ) -> dict[str, Any]:
        """API: Get One Backup Daemon Configuration by ID
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/daemonConfigs/get-one-backup-daemon-configuration-by-host/
        Description: Retrieves the configuration of one backup daemon."""
        return self._request(
            "GET",
            "/daemon/configs/{MACHINE}/{HEAD-ROOT-DIRECTORY}",
            path_params,
            query_params,
            None,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        head_root_directory: str = Field("None", serialization_alias="HEAD-ROOT-DIRECTORY")
        machine: str = Field("None", serialization_alias="MACHINE")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        assignment_enabled: Optional[bool] = Field(serialization_alias="assignmentEnabled")
        backup_jobs_enabled: Optional[bool] = Field(serialization_alias="backupJobsEnabled")
        configured: Optional[bool] = Field(serialization_alias="configured")
        garbage_collection_enabled: Optional[bool] = Field(serialization_alias="garbageCollectionEnabled")
        head_disk_type: Optional[str] = Field("None", serialization_alias="headDiskType")
        labels: Optional[list[str]] = Field(serialization_alias="labels")
        class MachineParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            head_root_directory: Optional[str] = Field("None", serialization_alias="headRootDirectory")
            machine: str = Field("None", serialization_alias="machine")
        machine: MachineParams = Field(serialization_alias="machine")
        num_workers: Optional[float] = Field(serialization_alias="numWorkers")
        resource_usage_enabled: Optional[bool] = Field(serialization_alias="resourceUsageEnabled")
        restore_queryable_jobs_enabled: Optional[bool] = Field(serialization_alias="restoreQueryableJobsEnabled")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: UpdateBodyParams,
    ) -> dict[str, Any]:
        """API: Update One Backup Daemon Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/daemonConfigs/update-one-backup-daemon-configuration/
        Description: Updates the configuration of one Backup Daemon."""
        return self._request(
            "PUT",
            "/daemon/configs/{MACHINE}/{HEAD-ROOT-DIRECTORY}",
            path_params,
            query_params,
            body_params,
        )