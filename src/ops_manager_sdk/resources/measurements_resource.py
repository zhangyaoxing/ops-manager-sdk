from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class MeasurementsResource(BaseResource):
    """Client for MeasurementsResource resource."""
    class DatabasePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        database_name: str = Field("None", serialization_alias="DATABASE-NAME")
        """Unique identifier of the database on which the MongoDB process is stored."""
        host_id: str = Field("None", serialization_alias="HOST-ID")
        """Unique identifier of the host that serves the MongoDB process."""
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns the host."""
    def database(self,
        path_params: DatabasePathParams,
    ) -> dict[str, Any]:
        """
        ## Get Database Measurements
        - Document: [Database](https://www.mongodb.com/docs/ops-manager/current/reference/api/measures/get-database-measurements/)
        - Resource: `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/databases/{DATABASE-NAME}/measurements`
        - Description: Database measurements provide statistics on database performance and storage. The Monitoring collects database measurements through the dbStats command."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/databases/{DATABASE-NAME}/measurements",
            path_params,
            None,
            None,
        )
    class DiskPartitionPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        host_id: str = Field("None", serialization_alias="HOST-ID")
        """Unique identifier of the host that serves the MongoDB process."""
        partition_name: str = Field("None", serialization_alias="PARTITION-NAME")
        """Name of the disk partition on which the MongoDB process is stored."""
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns the host."""
    def disk_partition(self,
        path_params: DiskPartitionPathParams,
    ) -> dict[str, Any]:
        """
        ## Get Disk Partition Measurements
        - Document: [Disk Partition](https://www.mongodb.com/docs/ops-manager/current/reference/api/measures/get-disk-measurements/)
        - Resource: `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/disks/{PARTITION-NAME}/measurements`
        - Description: Disk measurements provide data on IOPS, disk use, and disk latency on the disk partitions for hosts running MongoDB that the Automations collect. You must run Ops Manager Automation to retrieve disk measurements."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/disks/{PARTITION-NAME}/measurements",
            path_params,
            None,
            None,
        )
    class HostPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        host_id: str = Field("None", serialization_alias="HOST-ID")
        """Unique identifier of the host that serves the MongoDB process."""
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns the host."""
    def host(self,
        path_params: HostPathParams,
    ) -> dict[str, Any]:
        """
        ## Get Host, Process, System Measurements
        - Document: [Host](https://www.mongodb.com/docs/ops-manager/current/reference/api/measures/get-host-process-system-measurements/)
        - Resource: `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/measurements?granularity={ISO-8601-PERIOD}&period={ISO-8601-PERIOD}`
        - Description: Host measurements provide data on the state of the MongoDB process. The Monitoring collects host measurements through the MongoDB serverStatus and dbStats commands."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/measurements?granularity={ISO-8601-PERIOD}&period={ISO-8601-PERIOD}",
            path_params,
            None,
            None,
        )
    class GetTypesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        host_id: str = Field("None", serialization_alias="HOST-ID")
        """Unique identifier of the host that serves the MongoDB process."""
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        """Unique identifier of the project that owns the host."""
    def get_types(self,
        path_params: GetTypesPathParams,
    ) -> dict[str, Any]:
        """
        ## Get Measurement Types
        - Document: [Get Types](https://www.mongodb.com/docs/ops-manager/current/reference/api/measures/get-measurement-types/)
        - Resource: `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/measurements`
        - Description: To retrieve the Measurement Types that apply to a specific measurement without returning a large document, issue the following GET command with a value of PT5M for both the granularity and period. This returns a document with only one data point for each measurement."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/measurements",
            path_params,
            None,
            None,
        )