from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class EventsResource(BaseResource):
    """Client for EventsResource resource."""
    class GetAllOrganizationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class GetAllOrganizationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class GetAllOrganizationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all_organization_(self,
        path_params: Optional[GetAllOrganizationPathParams],
        query_params: Optional[GetAllOrganizationQueryParams],
        body_params: Optional[GetAllOrganizationBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Organization Events
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/events/get-all-events-for-org/
        Description: No description found."""
        return self._request(
            "GET",
            "/orgs/{orgId}/events",
            path_params,
            query_params,
            body_params,
        )
    class GetAllProjectPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="groupId")
    class GetAllProjectQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class GetAllProjectBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all_project_(self,
        path_params: GetAllProjectPathParams,
        query_params: Optional[GetAllProjectQueryParams],
        body_params: Optional[GetAllProjectBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Project Events
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/events/get-all-events-for-project/
        Description: No description found."""
        return self._request(
            "GET",
            "/groups/{groupId}/events",
            path_params,
            query_params,
            body_params,
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
    class GetOneOrganizationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_one_organization_(self,
        path_params: GetOneOrganizationPathParams,
        query_params: Optional[GetOneOrganizationQueryParams],
        body_params: Optional[GetOneOrganizationBodyParams],
    ) -> dict[str, Any]:
        """API: Get One Organization Event
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/events/get-one-event-for-org/
        Description: No description found."""
        return self._request(
            "GET",
            "/orgs/{orgId}/events/{eventId}",
            path_params,
            query_params,
            body_params,
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
    class GetOneProjectBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_one_project_(self,
        path_params: GetOneProjectPathParams,
        query_params: Optional[GetOneProjectQueryParams],
        body_params: Optional[GetOneProjectBodyParams],
    ) -> dict[str, Any]:
        """API: Get One Project Event
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/events/get-one-event-for-project/
        Description: No description found."""
        return self._request(
            "GET",
            "/groups/{groupId}/events/{eventId}",
            path_params,
            query_params,
            body_params,
        )