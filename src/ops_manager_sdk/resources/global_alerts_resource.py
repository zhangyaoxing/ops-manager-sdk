from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class GlobalAlertsResource(BaseResource):
    """Client for GlobalAlertsResource resource."""
    class AcknowledgeOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        alert_id: str = Field("None", serialization_alias="ALERT-ID")
    class AcknowledgeOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class AcknowledgeOneBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        acknowledged_until: str = Field("None", serialization_alias="acknowledgedUntil")
        acknowledgement_comment: Optional[str] = Field("None", serialization_alias="acknowledgementComment")
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
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        created_on_or_after: Optional[datetime] = Field(None, serialization_alias="createdOnOrAfter")
        created_on_or_before: Optional[datetime] = Field(None, serialization_alias="createdOnOrBefore")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        status: Optional[str] = Field("None", serialization_alias="status")
    def get_all(self,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """API: Get All Global Alerts
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alerts-get-all/
        Description: Retrieve all global alerts."""
        return self._request(
            "GET",
            "/globalAlerts",
            None,
            query_params,
            None,
        )
    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        alert_id: str = Field("None", serialization_alias="ALERT-ID")
    class GetOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_one(self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
    ) -> dict[str, Any]:
        """API: Get One Global Alert
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alerts-get-one/
        Description: Retrieve one alert by its ALERT-ID."""
        return self._request(
            "GET",
            "/globalAlerts/{ALERT-ID}",
            path_params,
            query_params,
            None,
        )