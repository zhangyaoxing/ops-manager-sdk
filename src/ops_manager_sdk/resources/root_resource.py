from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class RootResource(BaseResource):
    """Client for RootResource resource."""
    class RootQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def root(self,
        query_params: Optional[RootQueryParams],
    ) -> dict[str, Any]:
        """
        ## Root
        - Document: [Root](https://www.mongodb.com/docs/ops-manager/current/reference/api/root/)
        - Resource: `GET /`
        - Description: The root resource is the starting point for the Ops Manager API. From here, you can traverse the links to reach all other API resources."""
        return self._request(
            "GET",
            "/",
            None,
            query_params,
            None,
        )