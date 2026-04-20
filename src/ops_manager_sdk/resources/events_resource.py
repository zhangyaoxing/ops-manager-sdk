from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class EventsResource(BaseResource):
    """Client for EventsResource resource."""
    def get_all_organization_(self,
    ) -> dict[str, Any]:
        """API: Get All Organization Events
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/events/get-all-events-for-org/
        Description: No description."""
        return self._request(
            "GET",
            "/orgs/{orgId}/events",
            None,
            None,
            None,
        )
    class GetAllProjectPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="groupId")
    def get_all_project_(self,
        path_params: GetAllProjectPathParams,
    ) -> dict[str, Any]:
        """API: Get All Project Events
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/events/get-all-events-for-project/
        Description: No description."""
        return self._request(
            "GET",
            "/groups/{groupId}/events",
            path_params,
            None,
            None,
        )
    class GetOneOrganizationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="orgId")
        event_id: str = Field("None", serialization_alias="eventId")
    class GetOneOrganizationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        include_raw: Optional[bool] = Field(serialization_alias="includeRaw")
    def get_one_organization_(self,
        path_params: GetOneOrganizationPathParams,
        query_params: Optional[GetOneOrganizationQueryParams],
    ) -> dict[str, Any]:
        """API: Get One Organization Event
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/events/get-one-event-for-org/
        Description: No description."""
        return self._request(
            "GET",
            "/orgs/{orgId}/events/{eventId}",
            path_params,
            query_params,
            None,
        )
    class GetOneProjectPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="groupId")
        event_id: str = Field("None", serialization_alias="eventId")
    class GetOneProjectQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        include_raw: Optional[bool] = Field(serialization_alias="includeRaw")
    def get_one_project_(self,
        path_params: GetOneProjectPathParams,
        query_params: Optional[GetOneProjectQueryParams],
    ) -> dict[str, Any]:
        """API: Get One Project Event
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/events/get-one-event-for-project/
        Description: No description."""
        return self._request(
            "GET",
            "/groups/{groupId}/events/{eventId}",
            path_params,
            query_params,
            None,
        )