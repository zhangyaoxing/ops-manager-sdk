from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class BackupDaemonResource(BaseResource):
    """Client for BackupDaemonResource resource."""
    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        machine: str = Field(alias="MACHINE")
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        assignment_enabled: Optional[bool] = Field(alias="assignmentEnabled")
        backup_jobs_enabled: Optional[bool] = Field(alias="backupJobsEnabled")
        configured: Optional[bool] = Field(alias="configured")
        garbage_collection_enabled: Optional[bool] = Field(alias="garbageCollectionEnabled")
        head_disk_type: Optional[str] = Field(alias="headDiskType")
        labels: Optional[list[str]] = Field(alias="labels")
        machine: dict = Field(alias="machine")
        machine.head_root_directory: Optional[str] = Field(alias="machine.headRootDirectory")
        machine.machine: str = Field(alias="machine.machine")
        num_workers: Optional[float] = Field(alias="numWorkers")
        resource_usage_enabled: Optional[bool] = Field(alias="resourceUsageEnabled")
        restore_queryable_jobs_enabled: Optional[bool] = Field(alias="restoreQueryableJobsEnabled")
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
        machine: str = Field(alias="MACHINE")
        head_root_directory: str = Field(alias="HEAD-ROOT-DIRECTORY")
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
        """API: Delete One Backup Daemon Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/daemonConfigs/delete-one-backup-daemon-configuration/
        Description: Deletes the configuration of one backup daemon."""
        return self._request(
            "DELETE",
            "/daemon/configs/{MACHINE}/{HEAD-ROOT-DIRECTORY}",
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
        backup_jobs_enabled_only: Optional[bool] = Field(True, alias="backupJobsEnabledOnly")
    class GetAllBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all(self,
        path_params: Optional[GetAllPathParams],
        query_params: Optional[GetAllQueryParams],
        body_params: Optional[GetAllBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Backup Daemon Configurations
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/daemonConfigs/get-all-backup-daemon-configurations/
        Description: Retrieves the configurations of all backup daemons."""
        return self._request(
            "GET",
            "/daemon/configs",
            path_params,
            query_params,
            body_params,
        )
    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        machine: str = Field(alias="MACHINE")
        head_root_directory: str = Field(alias="HEAD-ROOT-DIRECTORY")
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
        """API: Get One Backup Daemon Configuration by ID
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/daemonConfigs/get-one-backup-daemon-configuration-by-host/
        Description: Retrieves the configuration of one backup daemon."""
        return self._request(
            "GET",
            "/daemon/configs/{MACHINE}/{HEAD-ROOT-DIRECTORY}",
            path_params,
            query_params,
            body_params,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        machine: str = Field(alias="MACHINE")
        head_root_directory: str = Field(alias="HEAD-ROOT-DIRECTORY")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        assignment_enabled: Optional[bool] = Field(alias="assignmentEnabled")
        backup_jobs_enabled: Optional[bool] = Field(alias="backupJobsEnabled")
        configured: Optional[bool] = Field(alias="configured")
        garbage_collection_enabled: Optional[bool] = Field(alias="garbageCollectionEnabled")
        head_disk_type: Optional[str] = Field(alias="headDiskType")
        labels: Optional[list[str]] = Field(alias="labels")
        machine: dict = Field(alias="machine")
        machine.head_root_directory: Optional[str] = Field(alias="machine.headRootDirectory")
        machine.machine: str = Field(alias="machine.machine")
        num_workers: Optional[float] = Field(alias="numWorkers")
        resource_usage_enabled: Optional[bool] = Field(alias="resourceUsageEnabled")
        restore_queryable_jobs_enabled: Optional[bool] = Field(alias="restoreQueryableJobsEnabled")
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