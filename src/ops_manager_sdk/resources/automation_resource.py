from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class AutomationResource(BaseResource):
    """Client for AutomationResource resource."""
    class GetStatusOfLast50PlansPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="GROUP-ID")
    class GetStatusOfLast50PlansQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_status_of_last_50_plans(self,
        path_params: GetStatusOfLast50PlansPathParams,
        query_params: Optional[GetStatusOfLast50PlansQueryParams],
    ) -> dict[str, Any]:
        """API: Get Automation Status of Last 50 Plans
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-status-full/
        Description: No description."""
        return self._request(
            "GET",
            "/groups/GROUP-ID/automationStatus/full",
            path_params,
            query_params,
            None,
        )
    class GetStatusPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetStatusQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_status(self,
        path_params: GetStatusPathParams,
        query_params: Optional[GetStatusQueryParams],
    ) -> dict[str, Any]:
        """API: Get Automation Status of Latest Plan
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-status/
        Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/automationStatus",
            path_params,
            query_params,
            None,
        )