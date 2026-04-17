from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class GlobalAlertsResource(BaseResource):
    """Client for GlobalAlertsResource resource."""
    class AcknowledgeOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        alert_id: str = Field(alias="ALERT-ID")
    class AcknowledgeOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class AcknowledgeOneBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        acknowledged_until: str = Field(alias="acknowledgedUntil")
        acknowledgement_comment: Optional[str] = Field(alias="acknowledgementComment")
    def acknowledge_one(self,
        path_params: AcknowledgeOnePathParams,
        query_params: Optional[AcknowledgeOneQueryParams],
        body_params: AcknowledgeOneBodyParams,
    ) -> dict[str, Any]:
        """API: Acknowledge One Global Alert
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alerts-ack-one/
        Description: You can acknowledge one alert until the time and date you specify. You can also un-acknowledge an alert by specifying a date and time in the past."""
        return self._request(
            "PATCH",
            "/globalAlerts/{ALERT-ID}",
            path_params,
            query_params,
            body_params,
        )
    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
        status: Optional[str] = Field(None, alias="status")
        created_on_or_after: Optional[datetime] = Field(None, alias="createdOnOrAfter")
        created_on_or_before: Optional[datetime] = Field(None, alias="createdOnOrBefore")
    class GetAllBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all(self,
        path_params: Optional[GetAllPathParams],
        query_params: Optional[GetAllQueryParams],
        body_params: Optional[GetAllBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Global Alerts
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alerts-get-all/
        Description: Retrieve all global alerts."""
        return self._request(
            "GET",
            "/globalAlerts",
            path_params,
            query_params,
            body_params,
        )
    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        alert_id: str = Field(alias="ALERT-ID")
    class GetOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetOneBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_one(self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
        body_params: Optional[GetOneBodyParams],
    ) -> dict[str, Any]:
        """API: Get One Global Alert
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alerts-get-one/
        Description: Retrieve one alert by its ALERT-ID."""
        return self._request(
            "GET",
            "/globalAlerts/{ALERT-ID}",
            path_params,
            query_params,
            body_params,
        )