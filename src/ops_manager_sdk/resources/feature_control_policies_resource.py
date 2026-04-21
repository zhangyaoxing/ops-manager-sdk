from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource


class FeatureControlPoliciesResource(BaseResource):
    """Client for FeatureControlPoliciesResource resource."""

    class RetrieveAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(serialization_alias="envelope")
        """None
        """

        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        """100
        """

        page_num: Optional[float] = Field(serialization_alias="pageNum")
        """1
        """

        pretty: Optional[bool] = Field(serialization_alias="pretty")
        """false
        """

    def retrieve_all(
        self,
        query_params: Optional[RetrieveAllQueryParams],
    ) -> dict[str, Any]:
        """
        ## Retrieve All Feature Policies
        - Document: [Retrieve All](https://www.mongodb.com/docs/ops-manager/current/reference/api/controlled-features/get-all-feature-control-policies/)
        - Resource: `GET /groups/availablePolicies`
        - Description: No description.
        """
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
        """Unique identifier of the project that has the controlled features.
        """

    class RetrieveForOneProjectQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(serialization_alias="envelope")
        """None
        """

        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        """100
        """

        page_num: Optional[float] = Field(serialization_alias="pageNum")
        """1
        """

        pretty: Optional[bool] = Field(serialization_alias="pretty")
        """false
        """

    def retrieve_for_one_project(
        self,
        path_params: RetrieveForOneProjectPathParams,
        query_params: Optional[RetrieveForOneProjectQueryParams],
    ) -> dict[str, Any]:
        """
        ## Retrieve Feature Policies for One Project
        - Document: [Retrieve for One Project](https://www.mongodb.com/docs/ops-manager/current/reference/api/controlled-features/get-controlled-features-for-one-project/)
        - Resource: `GET /groups/{PROJECT-ID}/controlledFeature`
        - Description: No description.
        """
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
        """Unique identifier of the project that has the controlled features.
        """

    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        envelope: Optional[bool] = Field(serialization_alias="envelope")
        """None
        """

        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        """100
        """

        page_num: Optional[float] = Field(serialization_alias="pageNum")
        """1
        """

        pretty: Optional[bool] = Field(serialization_alias="pretty")
        """false
        """

    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        class ExternalmanagementsystemParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            name: Optional[str] = Field("None", serialization_alias="name")
            """Identifying label for the external system that manages this Ops Manager Project.
            """

            system_id: Optional[str] = Field("None", serialization_alias="systemId")
            """Unique identifier of the external system that manages this Ops Manager Project.
            """

            version: Optional[str] = Field("None", serialization_alias="version")
            """Active release of the external system that manages this Ops Manager Project.
            """

        external_management_system: Optional[ExternalmanagementsystemParams] = Field(
            serialization_alias="externalManagementSystem"
        )
        """Identifying parameters for the external system that manages this Ops Manager Project.
        """

        class PoliciesParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)

            disabled_params: Optional[list[Any]] = Field(
                serialization_alias="disabledParams"
            )
            """List of mongod settings to disable when you apply the DISABLE_SET_MONGOD_CONFIG policy. Automation doesn't support all MongoDB options, which can result in failed import attempts. To learn more, see MongoDB Settings and Automation Support.
            """

            policy: Optional[dict] = Field(serialization_alias="policy")
            """Single policy set for this Ops Manager Project. This parameter can be set one or more times in the policies array.

Accepted values are:

Value
	
Purpose



EXTERNALLY_MANAGED_LOCK

	

Users can't use Ops Manager to manage other settings given in the policies.policy[n] array. These same users may use a configured external system, like the Kubernetes Operator to manage these settings.




DISABLE_USER_MANAGEMENT

	

Users can't manage users or roles.



DISABLE_AUTHENTICATION_
MECHANISMS
	

Users can't change authentication settings.



DISABLE_SET_MONGOD_
CONFIG
	

Users can't change any mongod settings listed in the policies[n].disabledParams array.



DISABLE_SET_MONGOD_
VERSION
	

Users can't change the version of any mongod or mongos.




DISABLE_BACKUP_AGENT

	

Users can't enable or disable the Backup agent.



DISABLE_MONGOD_LOG_
MANAGEMENT
	

Users can't change log management settings.



DISABLE_IMPORT_TO_
AUTOMATION
	

Users can't manage deployments using Automation.



DISABLE_AGENT_API_KEY_
MANAGEMENT
	

Users can't create or update Agent API keys.



DISABLE_MONGOD_HOST_
MANAGEMENT
	

Users can't change the server type of hosts.
            """

        policies: Optional[list[PoliciesParams]] = Field(serialization_alias="policies")
        """List of policies that the external system applies to this Ops Manager Project.
        """

    def update(
        self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """
        ## Update Feature Policies for One Project
        - Document: [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/controlled-features/update-controlled-features-for-one-project/)
        - Resource: `PUT /groups/{PROJECT-ID}/controlledFeature`
        - Description: No description.
        """
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}/controlledFeature",
            path_params,
            query_params,
            body_params,
        )
