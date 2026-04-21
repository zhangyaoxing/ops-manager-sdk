from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class SnapshotsResource(BaseResource):
    """Client for SnapshotsResource resource."""
    class ChangeExpiryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        snapshot_id: str = Field("None", serialization_alias="SNAPSHOT-ID")
        cluster_id: str = Field("None", serialization_alias="clusterId")
    class ChangeExpiryQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class ChangeExpiryBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        do_not_delete: Optional[bool] = Field(serialization_alias="doNotDelete")
        expires: Optional[datetime] = Field(serialization_alias="expires")
    def change_expiry(self,
        path_params: ChangeExpiryPathParams,
        query_params: Optional[ChangeExpiryQueryParams],
        body_params: Optional[ChangeExpiryBodyParams],
    ) -> dict[str, Any]:
        """API: Change the Expiry of One Snapshot
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/snapshots/change-expiry-for-one-snapshot/
        Description: No description."""
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/snapshots/{SNAPSHOT-ID}",
            path_params,
            query_params,
            body_params,
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
        """API: Get All Snapshots for One Config Server
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/snapshots/get-all-snapshots-for-config-server/
        Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/snapshots",
            path_params,
            query_params,
            None,
        )
    class GetAllClusterPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        cluster_id: str = Field("None", serialization_alias="clusterId")
    class GetAllClusterQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        completed: Optional[str] = Field("true", serialization_alias="completed")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_all_cluster_(self,
        path_params: GetAllClusterPathParams,
        query_params: Optional[GetAllClusterQueryParams],
    ) -> dict[str, Any]:
        """API: Get All Snapshots for One Cluster
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/snapshots/get-all-snapshots-for-one-cluster/
        Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/snapshots",
            path_params,
            query_params,
            None,
        )
    class GetOneConfigServerPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        snapshot_id: str = Field("None", serialization_alias="SNAPSHOT-ID")
        cluster_id: str = Field("None", serialization_alias="clusterId")
    class GetOneConfigServerQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_one_config_server_(self,
        path_params: GetOneConfigServerPathParams,
        query_params: Optional[GetOneConfigServerQueryParams],
    ) -> dict[str, Any]:
        """API: Get One Snapshot for One Config Server
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/snapshots/get-one-snapshot-for-config-server/
        Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/snapshots/{SNAPSHOT-ID}",
            path_params,
            query_params,
            None,
        )
    class GetOneClusterPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        snapshot_id: str = Field("None", serialization_alias="SNAPSHOT-ID")
        cluster_id: str = Field("None", serialization_alias="clusterId")
    class GetOneClusterQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_one_cluster_(self,
        path_params: GetOneClusterPathParams,
        query_params: Optional[GetOneClusterQueryParams],
    ) -> dict[str, Any]:
        """API: Get One Snapshot for One Cluster
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/snapshots/get-one-snapshot-for-one-cluster/
        Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/snapshots/{SNAPSHOT-ID}",
            path_params,
            query_params,
            None,
        )
    class RemoveOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        snapshot_id: str = Field("None", serialization_alias="SNAPSHOT-ID")
        cluster_id: str = Field("None", serialization_alias="clusterId")
    class RemoveOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def remove_one(self,
        path_params: RemoveOnePathParams,
        query_params: Optional[RemoveOneQueryParams],
    ) -> dict[str, Any]:
        """API: Remove One Snapshot from a Cluster
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/snapshots/remove-one-snapshot-from-one-cluster/
        Description: No description."""
        return self._request(
            "DELETE",
            "/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/snapshots/{SNAPSHOT-ID}",
            path_params,
            query_params,
            None,
        )
    class CreateOneOnDemandClusterPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="GROUP-ID")
        cluster_id: str = Field("None", serialization_alias="clusterId")
    class CreateOneOnDemandClusterQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        retention_days: float = Field(15.0, serialization_alias="retentionDays")
    def create_one_on_demand_cluster_(self,
        path_params: CreateOneOnDemandClusterPathParams,
        query_params: CreateOneOnDemandClusterQueryParams,
    ) -> dict[str, Any]:
        """API: Create an On-Demand Snapshot
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/snapshots/take-an-on-demand-snapshot/
        Description: No description."""
        return self._request(
            "POST",
            "/groups/{groupId}/clusters/{clusterId}/snapshots/onDemandSnapshot",
            path_params,
            query_params,
            None,
        )