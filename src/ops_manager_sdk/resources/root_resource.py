from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class RootResource(BaseResource):
    """Client for RootResource resource."""
    class RootPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class RootQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class RootBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def root(self,
        path_params: Optional[RootPathParams],
        query_params: Optional[RootQueryParams],
        body_params: Optional[RootBodyParams],
    ) -> dict[str, Any]:
        """API: Root
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/root/
        Description: The root resource is the starting point for the Ops Manager API. From here, you can traverse the links to reach all other API resources."""
        return self._request(
            "GET",
            "/",
            path_params,
            query_params,
            body_params,
        )