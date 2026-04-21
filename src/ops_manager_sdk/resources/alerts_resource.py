from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class AlertsResource(BaseResource):
    """Client for AlertsResource resource."""
    class AcknowledgeOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        alert_id: str = Field("None", serialization_alias="ALERT-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class AcknowledgeOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class AcknowledgeOneBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        acknowledged_until: Optional[str] = Field("None", serialization_alias="acknowledgedUntil")
        acknowledgement_comment: Optional[str] = Field("None", serialization_alias="acknowledgementComment")
    def acknowledge_one(self,
        path_params: AcknowledgeOnePathParams,
        query_params: Optional[AcknowledgeOneQueryParams],
        body_params: Optional[AcknowledgeOneBodyParams],
    ) -> dict[str, Any]:
        """
        ## Acknowledge One Alert
        - Document: [Acknowledge One](https://www.mongodb.com/docs/ops-manager/current/reference/api/alerts-acknowledge-alert/)
        - Resource: `PATCH /groups/{PROJECT-ID}/alerts/{ALERT-ID}`
        - Description: No description."""
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/alerts/{ALERT-ID}",
            path_params,
            query_params,
            body_params,
        )
    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        alert_id: str = Field("None", serialization_alias="ALERT-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_one(self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Alert
        - Document: [Get One](https://www.mongodb.com/docs/ops-manager/current/reference/api/alerts-get-alert/)
        - Resource: `GET /groups/{PROJECT-ID}/alerts/{ALERT-ID}`
        - Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/alerts/{ALERT-ID}",
            path_params,
            query_params,
            None,
        )
    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        status: Optional[str] = Field("None", serialization_alias="status")
    def get_all(self,
        path_params: GetAllPathParams,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Alerts
        - Document: [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/alerts-get-all-alerts/)
        - Resource: `GET /groups/{PROJECT-ID}/alerts`
        - Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/alerts",
            path_params,
            query_params,
            None,
        )