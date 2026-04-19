from typing import Any, Optional
from datetime import datetime
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
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
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
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        host_id: str = Field("None", serialization_alias="HOST-ID")
    class CreateConfigServerQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class CreateConfigServerBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        checkpoint_id: Optional[str] = Field("None", serialization_alias="checkpointId")
        delivery: dict = Field(serialization_alias="delivery")
        oplog_ts: Optional[str] = Field("None", serialization_alias="oplogTs")
        oplog_inc: Optional[str] = Field("None", serialization_alias="oplogInc")
        point_in_time_utc_millis: Optional[int] = Field(serialization_alias="pointInTimeUTCMillis")
        snapshot_id: Optional[str] = Field("None", serialization_alias="snapshotId")
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
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        cluster_id: str = Field("None", serialization_alias="clusterId")
    class GetAllClusterQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        batch_id: Optional[str] = Field("None", serialization_alias="BATCH-ID")
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
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        host_id: str = Field("None", serialization_alias="HOST-ID")
    class GetAllConfigServerQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
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
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        cluster_id: str = Field("None", serialization_alias="clusterId")
        job_id: str = Field("None", serialization_alias="JOB-ID")
    class GetOneClusterQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
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
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        host_id: str = Field("None", serialization_alias="HOST-ID")
        job_id: str = Field("None", serialization_alias="JOB-ID")
    class GetOneConfigServerQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
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