from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class DatabasesResource(BaseResource):
    """Client for DatabasesResource resource."""
    class GetByNamePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        host_id: str = Field("None", serialization_alias="HOST-ID")
        database_name: str = Field("None", serialization_alias="DATABASE-NAME")
    class GetByNameQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_by_name(self,
        path_params: GetByNamePathParams,
        query_params: Optional[GetByNameQueryParams],
    ) -> dict[str, Any]:
        """API: Get a Database by Name
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/database-get-by-name/
        Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/databases/{DATABASE-NAME}",
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
        """API: Get All Databases on One Host
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/databases-get-all-on-host/
        Description: Retrieve all databases running on the specified host."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/databases",
            path_params,
            query_params,
            None,
        )