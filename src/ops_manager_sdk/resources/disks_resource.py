from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class DisksResource(BaseResource):
    """Client for DisksResource resource."""
    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        host_id: str = Field("None", serialization_alias="HOST-ID")
        partition_name: str = Field("None", serialization_alias="PARTITION-NAME")
    class GetOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_one(self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
    ) -> dict[str, Any]:
        """API: Get a Disk Partition
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/disk-get-one/
        Description: Retrieves a disk partition."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/disks/{PARTITION-NAME}",
            path_params,
            query_params,
            None,
        )
    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        host_id: str = Field("None", serialization_alias="HOST-ID")
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_all(self,
        path_params: GetAllPathParams,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """API: Get all Disk Partitions
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/disks-get-all/
        Description: Retrieves all disk partitions on the specified host."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/disks",
            path_params,
            query_params,
            None,
        )