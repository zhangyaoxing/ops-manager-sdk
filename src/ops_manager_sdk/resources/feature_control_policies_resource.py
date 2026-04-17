from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class FeatureControlPoliciesResource(BaseResource):
    """Client for FeatureControlPoliciesResource resource."""
    class RetrieveAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class RetrieveAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(alias="pageNum")
        items_per_page: Optional[float] = Field(alias="itemsPerPage")
        pretty: Optional[bool] = Field(alias="pretty")
        envelope: Optional[bool] = Field(alias="envelope")
    class RetrieveAllBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def retrieve_all(self,
        path_params: Optional[RetrieveAllPathParams],
        query_params: Optional[RetrieveAllQueryParams],
        body_params: Optional[RetrieveAllBodyParams],
    ) -> dict[str, Any]:
        """API: Retrieve All Feature Policies
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/controlled-features/get-all-feature-control-policies/
        Description: No description found."""
        return self._request(
            "GET",
            "/groups/availablePolicies",
            path_params,
            query_params,
            body_params,
        )
    class RetrieveForOneProjectPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
    class RetrieveForOneProjectQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(alias="pageNum")
        items_per_page: Optional[float] = Field(alias="itemsPerPage")
        pretty: Optional[bool] = Field(alias="pretty")
        envelope: Optional[bool] = Field(alias="envelope")
    class RetrieveForOneProjectBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def retrieve_for_one_project(self,
        path_params: RetrieveForOneProjectPathParams,
        query_params: Optional[RetrieveForOneProjectQueryParams],
        body_params: Optional[RetrieveForOneProjectBodyParams],
    ) -> dict[str, Any]:
        """API: Retrieve Feature Policies for One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/controlled-features/get-controlled-features-for-one-project/
        Description: No description found."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/controlledFeature",
            path_params,
            query_params,
            body_params,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(alias="pageNum")
        items_per_page: Optional[float] = Field(alias="itemsPerPage")
        pretty: Optional[bool] = Field(alias="pretty")
        envelope: Optional[bool] = Field(alias="envelope")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        external_management_system: Optional[dict] = Field(alias="externalManagementSystem")
        external_management_system.name: Optional[str] = Field(alias="externalManagementSystem.name")
        external_management_system.system_id: Optional[str] = Field(alias="externalManagementSystem.systemId")
        external_management_system.version: Optional[str] = Field(alias="externalManagementSystem.version")
        policies: Optional[list[Any]] = Field(alias="policies")
        policies.policy[n]: Optional[dict] = Field(alias="policies.policy[n]")
        policies[n].disabled_params: Optional[list[Any]] = Field(alias="policies[n].disabledParams")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """API: Update Feature Policies for One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/controlled-features/update-controlled-features-for-one-project/
        Description: No description found."""
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}/controlledFeature",
            path_params,
            query_params,
            body_params,
        )