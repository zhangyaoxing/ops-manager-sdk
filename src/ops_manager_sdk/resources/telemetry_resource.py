from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class TelemetryResource(BaseResource):
    """Client for TelemetryResource resource."""
    def retrieve_telemetry_data(self,
    ) -> dict[str, Any]:
        """API: Retrieve Telemetry Data
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/telemetry/get-data/
        Description: Retrieve telemetry collection status and configuration details for your Ops Manager installation."""
        return self._request(
            "GET",
            "/collection/details",
            None,
            None,
            None,
        )
    class ToggleTelemetryStatusBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        enabled: bool = Field(serialization_alias="enabled")
    def toggle_telemetry_status(self,
        body_params: ToggleTelemetryStatusBodyParams,
    ) -> dict[str, Any]:
        """API: Toggle Telemetry Status
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/telemetry/toggle-status/
        Description: Enable or disable telemetry collection for your Ops Manager installation."""
        return self._request(
            "PATCH",
            "/collection/status",
            None,
            None,
            body_params,
        )