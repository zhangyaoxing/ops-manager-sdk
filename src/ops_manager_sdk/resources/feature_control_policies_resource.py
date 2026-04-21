from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class FeatureControlPoliciesResource(BaseResource):
    """Client for FeatureControlPoliciesResource resource."""
    class RetrieveAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    def retrieve_all(self,
        query_params: Optional[RetrieveAllQueryParams],
    ) -> dict[str, Any]:
        """API: Retrieve All Feature Policies
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/controlled-features/get-all-feature-control-policies/
        Description: No description."""
        return self._request(
            "GET",
            "/groups/availablePolicies",
            None,
            query_params,
            None,
        )
    class RetrieveForOneProjectPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class RetrieveForOneProjectQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    def retrieve_for_one_project(self,
        path_params: RetrieveForOneProjectPathParams,
        query_params: Optional[RetrieveForOneProjectQueryParams],
    ) -> dict[str, Any]:
        """API: Retrieve Feature Policies for One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/controlled-features/get-controlled-features-for-one-project/
        Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/controlledFeature",
            path_params,
            query_params,
            None,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        external_management_system: Optional[dict] = Field(serialization_alias="externalManagementSystem")
        policies: Optional[list[Any]] = Field(serialization_alias="policies")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """API: Update Feature Policies for One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/controlled-features/update-controlled-features-for-one-project/
        Description: No description."""
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}/controlledFeature",
            path_params,
            query_params,
            body_params,
        )