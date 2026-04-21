from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource


class GlobalEventsResource(BaseResource):
    """Client for GlobalEventsResource resource."""

    def get_all(
        self,
    ) -> dict[str, Any]:
        """
        ## Get All Global Events
        - Document: [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/events/get-all-events-global/)
        - Resource: `GET /globalEvents`
        - Description: No description.
        """
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
        """Unique identifier of the desired event.
        """

    class GetOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        """Flag that indicates whether or not to wrap the response in an envelope.

Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query.

For endpoints that return one result, the response body includes:

Name
	
Description



status

	

HTTP response code




content

	

Expected response body
        """

        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        """Flag indicating whether the response body should be in a prettyprint format.
        """

    def get_one(
        self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Global Event
        - Document: [Get One](https://www.mongodb.com/docs/ops-manager/current/reference/api/events/get-one-event-global/)
        - Resource: `GET /globalEvents/{eventId}`
        - Description: No description.
        """
        return self._request(
            "GET",
            "/globalEvents/{eventId}",
            path_params,
            query_params,
            None,
        )
