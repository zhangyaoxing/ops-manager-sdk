from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class GlobalEventsResource(BaseResource):
    """Client for GlobalEventsResource resource."""
    def get_all(self,
    ) -> dict[str, Any]:
        """API: Get All Global Events
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/events/get-all-events-global/
        Description: No description."""
        return self._request(
            "GET",
            "/globalEvents",
            None,
            None,
            None,
        )
    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        event_id: str = Field("None", serialization_alias="eventId")
    class GetOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_one(self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
    ) -> dict[str, Any]:
        """API: Get One Global Event
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/events/get-one-event-global/
        Description: No description."""
        return self._request(
            "GET",
            "/globalEvents/{eventId}",
            path_params,
            query_params,
            None,
        )