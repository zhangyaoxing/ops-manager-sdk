from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class EventsResource(BaseResource):
    """Client for EventsResource resource."""
    def get_all_organization_(self,
    ) -> dict[str, Any]:
        """
        ## Get All Organization Events
        - Document: [Get All (Organization)](https://www.mongodb.com/docs/ops-manager/current/reference/api/events/get-all-events-for-org/)
        - Resource: `GET /orgs/{orgId}/events`
        - Description: No description."""
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
        """
        ## Get All Project Events
        - Document: [Get All (Project)](https://www.mongodb.com/docs/ops-manager/current/reference/api/events/get-all-events-for-project/)
        - Resource: `GET /groups/{groupId}/events`
        - Description: No description."""
        return self._request(
            "GET",
            "/groups/{groupId}/events",
            path_params,
            None,
            None,
        )
    class GetOneOrganizationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        event_id: str = Field("None", serialization_alias="eventId")
        org_id: str = Field("None", serialization_alias="orgId")
    class GetOneOrganizationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        include_raw: Optional[bool] = Field(serialization_alias="includeRaw")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    def get_one_organization_(self,
        path_params: GetOneOrganizationPathParams,
        query_params: Optional[GetOneOrganizationQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Organization Event
        - Document: [Get One (Organization)](https://www.mongodb.com/docs/ops-manager/current/reference/api/events/get-one-event-for-org/)
        - Resource: `GET /orgs/{orgId}/events/{eventId}`
        - Description: No description."""
        return self._request(
            "GET",
            "/orgs/{orgId}/events/{eventId}",
            path_params,
            query_params,
            None,
        )
    class GetOneProjectPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        event_id: str = Field("None", serialization_alias="eventId")
        group_id: str = Field("None", serialization_alias="groupId")
    class GetOneProjectQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        include_raw: Optional[bool] = Field(serialization_alias="includeRaw")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    def get_one_project_(self,
        path_params: GetOneProjectPathParams,
        query_params: Optional[GetOneProjectQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Project Event
        - Document: [Get One (Project)](https://www.mongodb.com/docs/ops-manager/current/reference/api/events/get-one-event-for-project/)
        - Resource: `GET /groups/{groupId}/events/{eventId}`
        - Description: No description."""
        return self._request(
            "GET",
            "/groups/{groupId}/events/{eventId}",
            path_params,
            query_params,
            None,
        )