from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class DatabasesResource(BaseResource):
    """Client for DatabasesResource resource."""
    class GetByNamePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
        host_id: str = Field(alias="HOST-ID")
        database_name: str = Field(alias="DATABASE-NAME")
    class GetByNameQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetByNameBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_by_name(self,
        path_params: GetByNamePathParams,
        query_params: Optional[GetByNameQueryParams],
        body_params: Optional[GetByNameBodyParams],
    ) -> dict[str, Any]:
        """API: Get a Database by Name
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/database-get-by-name/
        Description: No description found."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/databases/{DATABASE-NAME}",
            path_params,
            query_params,
            body_params,
        )
    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
        host_id: str = Field(alias="HOST-ID")
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
        """API: Get All Databases on One Host
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/databases-get-all-on-host/
        Description: Retrieve all databases running on the specified host."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/databases",
            path_params,
            query_params,
            body_params,
        )