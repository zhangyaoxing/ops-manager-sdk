from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource


class ApiKeysOnProjectsResource(BaseResource):
    """Client for ApiKeysOnProjectsResource resource."""

    class AssignPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        api_key_id: str = Field("None", serialization_alias="API-KEY-ID")
        """Unique identifier for the API key you want to update. Request the /groups/{PROJECT-ID}/apiKeys endpoint to retrieve all API keys to which the authenticated user has access for the specified organization.
        """

        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        """Unique identifier for the Project whose API keys you want to update. Use the /groups endpoint to retrieve all organizations to which the authenticated user has access.
        """

    class AssignQueryParams(BaseModel):
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

    class AssignBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        roles: list[Any] = Field(serialization_alias="roles")
        """List of roles that the API Key should be granted. A minimum of one role must be provided. Any roles provided must be valid for the assigned Project:

Role Value in API
	
Role



GROUP_AUTOMATION_ADMIN

	

Project Automation Admin




GROUP_BACKUP_ADMIN

	

Project Backup Admin




GROUP_DATA_ACCESS_ADMIN

	

Project Data Access Admin




GROUP_DATA_ACCESS_READ_ONLY

	

Project Data Access Read Only




GROUP_DATA_ACCESS_READ_WRITE

	

Project Data Access Read/Write




GROUP_MONITORING_ADMIN

	

Project Monitoring Admin




GROUP_OWNER

	

Project Owner




GROUP_READ_ONLY

	

Project Read Only




GROUP_USER_ADMIN

	

Project User Admin
        """

    def assign(
        self,
        path_params: AssignPathParams,
        query_params: Optional[AssignQueryParams],
        body_params: AssignBodyParams,
    ) -> dict[str, Any]:
        """
        ## Assign One Organization API Key to One Project
        - Document: [Assign](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/project/assign-one-org-apiKey-to-one-project/)
        - Resource: `PATCH /groups/{PROJECT-ID}/apiKeys/{API-KEY-ID}`
        - Description: No description.
        """
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/apiKeys/{API-KEY-ID}",
            path_params,
            query_params,
            body_params,
        )

    class CreateAssignPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        """Unique identifier for the Project whose API keys you want to retrieve. Use the /groups endpoint to retrieve all organizations to which the authenticated user has access.
        """

    class CreateAssignQueryParams(BaseModel):
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

    class CreateAssignBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        desc: Optional[str] = Field("None", serialization_alias="desc")
        """Description of the API key. Must be between 1 and 250 characters in length.
        """

        roles: Optional[list[str]] = Field(serialization_alias="roles")
        """List of roles that the API Key needs to have. If the roles array is provided:

Provide at least one role

Make sure all roles must be valid for the Project

Project roles include:

Role Value in API
	
Role



GROUP_AUTOMATION_ADMIN

	

Project Automation Admin




GROUP_BACKUP_ADMIN

	

Project Backup Admin




GROUP_DATA_ACCESS_ADMIN

	

Project Data Access Admin




GROUP_DATA_ACCESS_READ_ONLY

	

Project Data Access Read Only




GROUP_DATA_ACCESS_READ_WRITE

	

Project Data Access Read/Write




GROUP_MONITORING_ADMIN

	

Project Monitoring Admin




GROUP_OWNER

	

Project Owner




GROUP_READ_ONLY

	

Project Read Only




GROUP_USER_ADMIN

	

Project User Admin
        """

    def create_assign(
        self,
        path_params: CreateAssignPathParams,
        query_params: Optional[CreateAssignQueryParams],
        body_params: Optional[CreateAssignBodyParams],
    ) -> dict[str, Any]:
        """
        ## Create and Assign One Organization API Key to One Project
        - Document: [Create & Assign](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/project/create-one-apiKey-in-one-project/)
        - Resource: `POST /groups/{PROJECT-ID}/apiKeys`
        - Description: No description.
        """
        return self._request(
            "POST",
            "/groups/{PROJECT-ID}/apiKeys",
            path_params,
            query_params,
            body_params,
        )

    class UnassignPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        api_key_id: str = Field("None", serialization_alias="API-KEY-ID")
        """Unique identifier for the API key you want to update. Request the /groups/{PROJECT-ID}/apiKeys endpoint to retrieve all API keys to which the authenticated user has access for the specified organization.
        """

        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        """Unique identifier for the Project you wish to unassign from the API key. Use the /groups endpoint to retrieve all organizations to which the authenticated user has access.
        """

    class UnassignQueryParams(BaseModel):
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

    def unassign(
        self,
        path_params: UnassignPathParams,
        query_params: Optional[UnassignQueryParams],
    ) -> dict[str, Any]:
        """
        ## Unassign One Organization API Key from One Project
        - Document: [Unassign](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/project/delete-one-apiKey-in-one-project/)
        - Resource: `DELETE /orgs/{PROJECT-ID}/apiKeys/{API-KEY-ID}`
        - Description: No description.
        """
        return self._request(
            "DELETE",
            "/orgs/{PROJECT-ID}/apiKeys/{API-KEY-ID}",
            path_params,
            query_params,
            None,
        )

    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        """Unique identifier for the Project from which you want to retrieve its assigned Organization API keys. Use the /groups endpoint to retrieve all Projects to which the authenticated user has access.
        """

    class GetAllQueryParams(BaseModel):
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

    def get_all(
        self,
        path_params: GetAllPathParams,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Organization API Keys Assigned to One Project
        - Document: [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/project/get-all-apiKeys-in-one-project/)
        - Resource: `GET /groups/{PROJECT-ID}/apiKeys`
        - Description: No description.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/apiKeys",
            path_params,
            query_params,
            None,
        )

    class ModifyRolesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        api_key_id: str = Field("None", serialization_alias="API-KEY-ID")
        """Unique identifier for the API key you want to update. Request the /groups/{PROJECT-ID}/apiKeys endpoint to retrieve all API keys to which the authenticated user has access for the specified organization.
        """

        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        """Unique identifier for the Project whose API keys you want to update. Use the /groups endpoint to retrieve all organizations to which the authenticated user has access.
        """

    class ModifyRolesQueryParams(BaseModel):
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

    class ModifyRolesBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        roles: list[str] = Field(serialization_alias="roles")
        """List of roles that the API Key should be granted. A minimum of one role must be provided. Any roles provided must be valid for the assigned Project:

Role Value in API
	
Role



GROUP_AUTOMATION_ADMIN

	

Project Automation Admin




GROUP_BACKUP_ADMIN

	

Project Backup Admin




GROUP_DATA_ACCESS_ADMIN

	

Project Data Access Admin




GROUP_DATA_ACCESS_READ_ONLY

	

Project Data Access Read Only




GROUP_DATA_ACCESS_READ_WRITE

	

Project Data Access Read/Write




GROUP_MONITORING_ADMIN

	

Project Monitoring Admin




GROUP_OWNER

	

Project Owner




GROUP_READ_ONLY

	

Project Read Only




GROUP_USER_ADMIN

	

Project User Admin

Include all roles that you want this API Key to have. Any roles not in this array are removed.
        """

    def modify_roles(
        self,
        path_params: ModifyRolesPathParams,
        query_params: Optional[ModifyRolesQueryParams],
        body_params: ModifyRolesBodyParams,
    ) -> dict[str, Any]:
        """
        ## Modify Roles of One Organization API Key to One Project
        - Document: [Modify Roles](https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/project/update-one-apiKey-in-one-project/)
        - Resource: `PATCH /groups/{PROJECT-ID}/apiKeys/{API-KEY-ID}`
        - Description: No description.
        """
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/apiKeys/{API-KEY-ID}",
            path_params,
            query_params,
            body_params,
        )
