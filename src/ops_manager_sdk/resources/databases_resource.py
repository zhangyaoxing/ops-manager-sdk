from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class DatabasesResource(BaseResource):
    """Client for DatabasesResource resource."""
    class GetByNamePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        database_name: str = Field("None", serialization_alias="DATABASE-NAME")
        host_id: str = Field("None", serialization_alias="HOST-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetByNameQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_by_name(self,
        path_params: GetByNamePathParams,
        query_params: Optional[GetByNameQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get a Database by Name
        - Document: [Get by Name](https://www.mongodb.com/docs/ops-manager/current/reference/api/database-get-by-name/)
        - Resource: `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/databases/{DATABASE-NAME}`
        - Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/databases/{DATABASE-NAME}",
            path_params,
            query_params,
            None,
        )
    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        host_id: str = Field("None", serialization_alias="HOST-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_all(self,
        path_params: GetAllPathParams,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Databases on One Host
        - Document: [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/databases-get-all-on-host/)
        - Resource: `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/databases`
        - Description: Retrieve all databases running on the specified host."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/databases",
            path_params,
            query_params,
            None,
        )