from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class BackupConfigurationsResource(BaseResource):
    """Client for BackupConfigurationsResource resource."""
    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetAllBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all(self,
        path_params: GetAllPathParams,
        query_params: Optional[GetAllQueryParams],
        body_params: Optional[GetAllBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Backup Configurations for One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/get-all-backup-configs-for-group/
        Description: No description found."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/backupConfigs",
            path_params,
            query_params,
            body_params,
        )
    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
        cluster_id: str = Field("None", alias="clusterId")
    class GetOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetOneBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_one(self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
        body_params: Optional[GetOneBodyParams],
    ) -> dict[str, Any]:
        """API: Get One Backup Configuration from One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/get-one-backup-config-by-cluster-id/
        Description: No description found."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}",
            path_params,
            query_params,
            body_params,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="projectId")
        cluster_id: str = Field("None", alias="clusterId")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        auth_mechanism_name: Optional[str] = Field("None", alias="authMechanismName")
        encryption_enabled: Optional[bool] = Field(alias="encryptionEnabled")
        excluded_namespaces: Optional[list[str]] = Field(alias="excludedNamespaces")
        included_namespaces: Optional[list[str]] = Field(alias="includedNamespaces")
        password: Optional[str] = Field("None", alias="password")
        preferred_member: Optional[str] = Field("None", alias="preferredMember")
        provisioned: Optional[bool] = Field(alias="provisioned")
        ssl_enabled: Optional[bool] = Field(alias="sslEnabled")
        status_name: Optional[str] = Field("None", alias="statusName")
        storage_engine_name: Optional[str] = Field("None", alias="storageEngineName")
        sync_source: Optional[str] = Field("None", alias="syncSource")
        username: Optional[str] = Field("None", alias="username")
        snapshot_store: Optional[dict] = Field(alias="snapshotStore")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """API: Update One Backup Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/update-backup-config/
        Description: No description found."""
        return self._request(
            "PATCH",
            "/groups/{projectId}/backupConfigs/{clusterId}",
            path_params,
            query_params,
            body_params,
        )