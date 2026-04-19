from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class MeasurementsResource(BaseResource):
    """Client for MeasurementsResource resource."""
    class DatabasePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        host_id: str = Field("None", serialization_alias="HOST-ID")
        database_name: str = Field("None", serialization_alias="DATABASE-NAME")
    class DatabaseQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class DatabaseBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def database(self,
        path_params: DatabasePathParams,
        query_params: Optional[DatabaseQueryParams],
        body_params: Optional[DatabaseBodyParams],
    ) -> dict[str, Any]:
        """API: Get Database Measurements
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/measures/get-database-measurements/
        Description: Database measurements provide statistics on database performance and storage. The Monitoring collects database measurements through the dbStats command."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/databases/{DATABASE-NAME}/measurements",
            path_params,
            query_params,
            body_params,
        )
    class DiskPartitionPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        host_id: str = Field("None", serialization_alias="HOST-ID")
        partition_name: str = Field("None", serialization_alias="PARTITION-NAME")
    class DiskPartitionQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class DiskPartitionBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def disk_partition(self,
        path_params: DiskPartitionPathParams,
        query_params: Optional[DiskPartitionQueryParams],
        body_params: Optional[DiskPartitionBodyParams],
    ) -> dict[str, Any]:
        """API: Get Disk Partition Measurements
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/measures/get-disk-measurements/
        Description: Disk measurements provide data on IOPS, disk use, and disk latency on the disk partitions for hosts running MongoDB that the Automations collect. You must run Ops Manager Automation to retrieve disk measurements."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/disks/{PARTITION-NAME}/measurements",
            path_params,
            query_params,
            body_params,
        )
    class HostPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        host_id: str = Field("None", serialization_alias="HOST-ID")
    class HostQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class HostBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def host(self,
        path_params: HostPathParams,
        query_params: Optional[HostQueryParams],
        body_params: Optional[HostBodyParams],
    ) -> dict[str, Any]:
        """API: Get Host, Process, System Measurements
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/measures/get-host-process-system-measurements/
        Description: Host measurements provide data on the state of the MongoDB process. The Monitoring collects host measurements through the MongoDB serverStatus and dbStats commands."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/measurements?granularity={ISO-8601-PERIOD}&period={ISO-8601-PERIOD}",
            path_params,
            query_params,
            body_params,
        )
    class GetTypesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        host_id: str = Field("None", serialization_alias="HOST-ID")
    class GetTypesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class GetTypesBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_types(self,
        path_params: GetTypesPathParams,
        query_params: Optional[GetTypesQueryParams],
        body_params: Optional[GetTypesBodyParams],
    ) -> dict[str, Any]:
        """API: Get Measurement Types
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/measures/get-measurement-types/
        Description: To retrieve the Measurement Types that apply to a specific measurement without returning a large document, issue the following GET command with a value of PT5M for both the granularity and period. This returns a document with only one data point for each measurement."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/measurements",
            path_params,
            query_params,
            body_params,
        )