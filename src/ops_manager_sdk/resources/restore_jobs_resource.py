from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class RestoreJobsResource(BaseResource):
    """Client for RestoreJobsResource resource."""
    class CreateClusterPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
        cluster_id: str = Field(alias="clusterId")
    class CreateClusterQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class CreateClusterBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def create_cluster_(self,
        path_params: CreateClusterPathParams,
        query_params: Optional[CreateClusterQueryParams],
        body_params: Optional[CreateClusterBodyParams],
    ) -> dict[str, Any]:
        """API: Create One Restore Job for One Cluster
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/restorejobs/create-one-restore-job-for-one-cluster/
        Description: No description found."""
        return self._request(
            "POST",
            "/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs",
            path_params,
            query_params,
            body_params,
        )
    class CreateConfigServerPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
        host_id: str = Field(alias="HOST-ID")
    class CreateConfigServerQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class CreateConfigServerBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        checkpoint_id: Optional[str] = Field(alias="checkpointId")
        delivery: dict = Field(alias="delivery")
        delivery.expires: Optional[str] = Field(alias="delivery.expires")
        delivery.expiration_hours: Optional[float] = Field(alias="delivery.expirationHours")
        delivery.max_downloads: Optional[float] = Field(alias="delivery.maxDownloads")
        delivery.method_name: str = Field(alias="delivery.methodName")
        delivery.target_cluster_id: Optional[str] = Field(alias="delivery.targetClusterId")
        delivery.target_group_id: Optional[str] = Field(alias="delivery.targetGroupId")
        oplog_ts: Optional[str] = Field(alias="oplogTs")
        oplog_inc: Optional[str] = Field(alias="oplogInc")
        point_in_time_utc_millis: Optional[int] = Field(alias="pointInTimeUTCMillis")
        snapshot_id: Optional[str] = Field(alias="snapshotId")
    def create_config_server_(self,
        path_params: CreateConfigServerPathParams,
        query_params: Optional[CreateConfigServerQueryParams],
        body_params: CreateConfigServerBodyParams,
    ) -> dict[str, Any]:
        """API: Create One Restore Job for One Legacy Mirrored Config Server
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/restorejobs/create-one-restore-job-for-one-sccc-config-server/
        Description: No description found."""
        return self._request(
            "POST",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/restoreJobs",
            path_params,
            query_params,
            body_params,
        )
    class GetAllClusterPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
        cluster_id: str = Field(alias="clusterId")
    class GetAllClusterQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
        batch_id: Optional[str] = Field(alias="BATCH-ID")
    class GetAllClusterBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all_cluster_(self,
        path_params: GetAllClusterPathParams,
        query_params: Optional[GetAllClusterQueryParams],
        body_params: Optional[GetAllClusterBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Restore Jobs for One Cluster
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/restorejobs/get-all-restore-jobs-for-one-cluster/
        Description: Get all restore jobs for a cluster. CLUSTER-ID must be the ID of either a replica set or a sharded cluster."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs",
            path_params,
            query_params,
            body_params,
        )
    class GetAllConfigServerPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
        host_id: str = Field(alias="HOST-ID")
    class GetAllConfigServerQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetAllConfigServerBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all_config_server_(self,
        path_params: GetAllConfigServerPathParams,
        query_params: Optional[GetAllConfigServerQueryParams],
        body_params: Optional[GetAllConfigServerBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Restore Jobs for One Legacy Mirrored Config Server
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/restorejobs/get-all-restore-jobs-for-one-sccc-config-server/
        Description: No description found."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/restoreJobs",
            path_params,
            query_params,
            body_params,
        )
    class GetOneClusterPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
        cluster_id: str = Field(alias="clusterId")
        job_id: str = Field(alias="JOB-ID")
    class GetOneClusterQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetOneClusterBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_one_cluster_(self,
        path_params: GetOneClusterPathParams,
        query_params: Optional[GetOneClusterQueryParams],
        body_params: Optional[GetOneClusterBodyParams],
    ) -> dict[str, Any]:
        """API: Get One Restore Job for One Cluster
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/restorejobs/get-one-single-restore-job-for-one-cluster/
        Description: No description found."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs/{JOB-ID}",
            path_params,
            query_params,
            body_params,
        )
    class GetOneConfigServerPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
        host_id: str = Field(alias="HOST-ID")
        job_id: str = Field(alias="JOB-ID")
    class GetOneConfigServerQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetOneConfigServerBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_one_config_server_(self,
        path_params: GetOneConfigServerPathParams,
        query_params: Optional[GetOneConfigServerQueryParams],
        body_params: Optional[GetOneConfigServerBodyParams],
    ) -> dict[str, Any]:
        """API: Get One Restore Job for One Legacy Mirrored Config Server
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/restorejobs/get-one-single-restore-job-for-one-sccc-config-server/
        Description: No description found."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/restoreJobs/{JOB-ID}",
            path_params,
            query_params,
            body_params,
        )