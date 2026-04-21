from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class RestoreJobsResource(BaseResource):
    """Client for RestoreJobsResource resource."""
    class CreateClusterPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        cluster_id: str = Field("None", serialization_alias="clusterId")
    class CreateClusterQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def create_cluster_(self,
        path_params: CreateClusterPathParams,
        query_params: Optional[CreateClusterQueryParams],
    ) -> dict[str, Any]:
        """API: Create One Restore Job for One Cluster
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/restorejobs/create-one-restore-job-for-one-cluster/
        Description: No description."""
        return self._request(
            "POST",
            "/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs",
            path_params,
            query_params,
            None,
        )
    class CreateConfigServerPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        host_id: str = Field("None", serialization_alias="HOST-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class CreateConfigServerQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class CreateConfigServerBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        checkpoint_id: Optional[str] = Field("None", serialization_alias="checkpointId")
        class DeliveryParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            expiration_hours: Optional[float] = Field(serialization_alias="expirationHours")
            expires: Optional[str] = Field("None", serialization_alias="expires")
            max_downloads: Optional[float] = Field(serialization_alias="maxDownloads")
            method_name: str = Field("None", serialization_alias="methodName")
            target_cluster_id: Optional[str] = Field("None", serialization_alias="targetClusterId")
            target_group_id: Optional[str] = Field("None", serialization_alias="targetGroupId")
        delivery: DeliveryParams = Field(serialization_alias="delivery")
        oplog_inc: Optional[str] = Field("None", serialization_alias="oplogInc")
        oplog_ts: Optional[str] = Field("None", serialization_alias="oplogTs")
        point_in_time_utc_millis: Optional[int] = Field(serialization_alias="pointInTimeUTCMillis")
        snapshot_id: Optional[str] = Field("None", serialization_alias="snapshotId")
    def create_config_server_(self,
        path_params: CreateConfigServerPathParams,
        query_params: Optional[CreateConfigServerQueryParams],
        body_params: CreateConfigServerBodyParams,
    ) -> dict[str, Any]:
        """API: Create One Restore Job for One Legacy Mirrored Config Server
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/restorejobs/create-one-restore-job-for-one-sccc-config-server/
        Description: No description."""
        return self._request(
            "POST",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/restoreJobs",
            path_params,
            query_params,
            body_params,
        )
    class GetAllClusterPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        cluster_id: str = Field("None", serialization_alias="clusterId")
    class GetAllClusterQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        batch_id: Optional[str] = Field("None", serialization_alias="BATCH-ID")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_all_cluster_(self,
        path_params: GetAllClusterPathParams,
        query_params: Optional[GetAllClusterQueryParams],
    ) -> dict[str, Any]:
        """API: Get All Restore Jobs for One Cluster
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/restorejobs/get-all-restore-jobs-for-one-cluster/
        Description: Get all restore jobs for a cluster. CLUSTER-ID must be the ID of either a replica set or a sharded cluster."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs",
            path_params,
            query_params,
            None,
        )
    class GetAllConfigServerPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        host_id: str = Field("None", serialization_alias="HOST-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetAllConfigServerQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_all_config_server_(self,
        path_params: GetAllConfigServerPathParams,
        query_params: Optional[GetAllConfigServerQueryParams],
    ) -> dict[str, Any]:
        """API: Get All Restore Jobs for One Legacy Mirrored Config Server
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/restorejobs/get-all-restore-jobs-for-one-sccc-config-server/
        Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/restoreJobs",
            path_params,
            query_params,
            None,
        )
    class GetOneClusterPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        job_id: str = Field("None", serialization_alias="JOB-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        cluster_id: str = Field("None", serialization_alias="clusterId")
    class GetOneClusterQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_one_cluster_(self,
        path_params: GetOneClusterPathParams,
        query_params: Optional[GetOneClusterQueryParams],
    ) -> dict[str, Any]:
        """API: Get One Restore Job for One Cluster
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/restorejobs/get-one-single-restore-job-for-one-cluster/
        Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs/{JOB-ID}",
            path_params,
            query_params,
            None,
        )
    class GetOneConfigServerPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        host_id: str = Field("None", serialization_alias="HOST-ID")
        job_id: str = Field("None", serialization_alias="JOB-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetOneConfigServerQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_one_config_server_(self,
        path_params: GetOneConfigServerPathParams,
        query_params: Optional[GetOneConfigServerQueryParams],
    ) -> dict[str, Any]:
        """API: Get One Restore Job for One Legacy Mirrored Config Server
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/restorejobs/get-one-single-restore-job-for-one-sccc-config-server/
        Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/restoreJobs/{JOB-ID}",
            path_params,
            query_params,
            None,
        )