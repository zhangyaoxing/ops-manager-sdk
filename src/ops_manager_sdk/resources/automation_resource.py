from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class AutomationResource(BaseResource):
    """Client for AutomationResource resource."""
    class GetStatusOfLast50PlansPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="GROUP-ID")
    class GetStatusOfLast50PlansQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_status_of_last_50_plans(self,
        path_params: GetStatusOfLast50PlansPathParams,
        query_params: Optional[GetStatusOfLast50PlansQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Automation Status of Last 50 Plans
        - Document: [Get Status of Last 50 Plans](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-status-full/)
        - Resource: `GET /groups/GROUP-ID/automationStatus/full`
        - Description: No description."""
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
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_status(self,
        path_params: GetStatusPathParams,
        query_params: Optional[GetStatusQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Automation Status of Latest Plan
        - Document: [Get Status](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-status/)
        - Resource: `GET /groups/{PROJECT-ID}/automationStatus`
        - Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/automationStatus",
            path_params,
            query_params,
            None,
        )