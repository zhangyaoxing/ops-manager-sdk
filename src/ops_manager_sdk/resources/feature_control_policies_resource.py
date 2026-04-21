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
        """
        ## Retrieve All Feature Policies
        - Document: [Retrieve All](https://www.mongodb.com/docs/ops-manager/current/reference/api/controlled-features/get-all-feature-control-policies/)
        - Resource: `GET /groups/availablePolicies`
        - Description: No description."""
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
        """
        ## Retrieve Feature Policies for One Project
        - Document: [Retrieve for One Project](https://www.mongodb.com/docs/ops-manager/current/reference/api/controlled-features/get-controlled-features-for-one-project/)
        - Resource: `GET /groups/{PROJECT-ID}/controlledFeature`
        - Description: No description."""
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
        class ExternalmanagementsystemParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            name: Optional[str] = Field("None", serialization_alias="name")
            system_id: Optional[str] = Field("None", serialization_alias="systemId")
            version: Optional[str] = Field("None", serialization_alias="version")
        external_management_system: Optional[ExternalmanagementsystemParams] = Field(serialization_alias="externalManagementSystem")
        class PoliciesParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            disabled_params: Optional[list[Any]] = Field(serialization_alias="disabledParams")
            policy: Optional[dict] = Field(serialization_alias="policy")
        policies: Optional[list[PoliciesParams]] = Field(serialization_alias="policies")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """
        ## Update Feature Policies for One Project
        - Document: [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/controlled-features/update-controlled-features-for-one-project/)
        - Resource: `PUT /groups/{PROJECT-ID}/controlledFeature`
        - Description: No description."""
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}/controlledFeature",
            path_params,
            query_params,
            body_params,
        )