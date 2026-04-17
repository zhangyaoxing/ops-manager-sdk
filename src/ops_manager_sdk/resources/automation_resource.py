from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class AutomationResource(BaseResource):
    """Client for AutomationResource resource."""
    class GetStatusOfLast50PlansPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field(alias="GROUP-ID")
    class GetStatusOfLast50PlansQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetStatusOfLast50PlansBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_status_of_last_50_plans(self,
        path_params: GetStatusOfLast50PlansPathParams,
        query_params: Optional[GetStatusOfLast50PlansQueryParams],
        body_params: Optional[GetStatusOfLast50PlansBodyParams],
    ) -> dict[str, Any]:
        """API: Get Automation Status of Last 50 Plans
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-status-full/
        Description: No description found."""
        return self._request(
            "GET",
            "/groups/GROUP-ID/automationStatus/full",
            path_params,
            query_params,
            body_params,
        )
    class GetStatusPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
    class GetStatusQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetStatusBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_status(self,
        path_params: GetStatusPathParams,
        query_params: Optional[GetStatusQueryParams],
        body_params: Optional[GetStatusBodyParams],
    ) -> dict[str, Any]:
        """API: Get Automation Status of Latest Plan
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-status/
        Description: No description found."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/automationStatus",
            path_params,
            query_params,
            body_params,
        )