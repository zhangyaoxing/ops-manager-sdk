from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class ProjectBackupJobResource(BaseResource):
    """Client for ProjectBackupJobResource resource."""
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_all(self,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """API: Get All Project Backup Jobs Configurations
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/groups/get-all-backup-group-configurations/
        Description: Retrieves the configurations of all project's backup jobs."""
        return self._request(
            "GET",
            "/groups",
            None,
            query_params,
            None,
        )
    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetByIdQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_by_id(self,
        path_params: GetByIdPathParams,
        query_params: Optional[GetByIdQueryParams],
    ) -> dict[str, Any]:
        """API: Get One Project Backup Jobs Configuration by ID
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/groups/get-one-backup-group-configuration-by-id/
        Description: Retrieves the configuration of one project's backup jobs."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}",
            path_params,
            query_params,
            None,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        daemon_filter: Optional[list[dict]] = Field(serialization_alias="daemonFilter")
        id: Optional[str] = Field("None", serialization_alias="id")
        kmip_client_cert_password: Optional[str] = Field("None", serialization_alias="kmipClientCertPassword")
        kmip_client_cert_path: Optional[str] = Field("None", serialization_alias="kmipClientCertPath")
        label_filter: Optional[list[str]] = Field(serialization_alias="labelFilter")
        oplog_store_filter: Optional[list[dict]] = Field(serialization_alias="oplogStoreFilter")
        snapshot_store_filter: Optional[list[dict]] = Field(serialization_alias="snapshotStoreFilter")
        sync_store_filter: Optional[list[str]] = Field(serialization_alias="syncStoreFilter")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """API: Update One Project Backup Jobs Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/groups/update-one-backup-group-configuration/
        Description: Updates the configuration of one project's backup jobs."""
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}",
            path_params,
            query_params,
            body_params,
        )