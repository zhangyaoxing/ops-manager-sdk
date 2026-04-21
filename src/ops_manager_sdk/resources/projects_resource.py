from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class ProjectsResource(BaseResource):
    """Client for ProjectsResource resource."""
    class AddExistingUsersPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class AddExistingUsersQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class AddExistingUsersBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        id: Optional[str] = Field("None", serialization_alias="id")
        class RolesParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            group_id: Optional[str] = Field("None", serialization_alias="groupId")
            role_name: Optional[str] = Field("None", serialization_alias="roleName")
        roles: Optional[list[RolesParams]] = Field(serialization_alias="roles")
    def add_existing_users(self,
        path_params: AddExistingUsersPathParams,
        query_params: Optional[AddExistingUsersQueryParams],
        body_params: Optional[AddExistingUsersBodyParams],
    ) -> dict[str, Any]:
        """
        ## Add Existing Users to One Project
        - Document: [Add Existing Users](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/add-users-to-one-group/)
        - Resource: `POST /groups/{PROJECT-ID}/users`
        - Description: This resource adds users who exist in Ops Manager to another project. It does not create new users and add them to a project. By default, users first receive an invitation to the project. You can add users directly to a project only if you set the mms.user.bypassInviteForExistingUsers setting to true."""
        return self._request(
            "POST",
            "/groups/{PROJECT-ID}/users",
            path_params,
            query_params,
            body_params,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        ldap_group_mappings: Optional[list[dict]] = Field(serialization_alias="ldapGroupMappings")
        name: Optional[str] = Field("None", serialization_alias="name")
        tags: Optional[list[str]] = Field(serialization_alias="tags")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """
        ## Update One Project
        - Document: [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/change-one-group-name/)
        - Resource: `PATCH /groups/{PROJECT-ID}`
        - Description: Use this endpoint to make any of the following changes to one project:"""
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}",
            path_params,
            query_params,
            body_params,
        )
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        name: str = Field("None", serialization_alias="name")
        org_id: str = Field("None", serialization_alias="orgId")
    def create(self,
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create One Project
        - Document: [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/create-one-group/)
        - Resource: `POST /groups`
        - Description: No description."""
        return self._request(
            "POST",
            "/groups",
            None,
            query_params,
            body_params,
        )
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class DeleteQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def delete(self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
    ) -> dict[str, Any]:
        """
        ## Delete One Project
        - Document: [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/delete-one-group/)
        - Resource: `DELETE /groups/{PROJECT-ID}`
        - Description: No description."""
        return self._request(
            "DELETE",
            "/groups/{PROJECT-ID}",
            path_params,
            query_params,
            None,
        )
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_all(self,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Projects for the Current User
        - Document: [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/get-all-groups-for-current-user/)
        - Resource: `GET /groups`
        - Description: No description."""
        return self._request(
            "GET",
            "/groups",
            None,
            query_params,
            None,
        )
    class GetBySpecificTagsForTheCurrentUserQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        tag: Optional[str] = Field("None", serialization_alias="tag")
    def get_by_specific_tags_for_the_current_user(self,
        query_params: Optional[GetBySpecificTagsForTheCurrentUserQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Projects with Specific Tags for the Current User
        - Document: [Get by Specific Tags for the Current User](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/get-all-groups-with-specific-tags-for-current-user/)
        - Resource: `GET /groups`
        - Description: No description."""
        return self._request(
            "GET",
            "/groups",
            None,
            query_params,
            None,
        )
    class GetAllUsersPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetAllUsersQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        flatten_teams: Optional[bool] = Field(serialization_alias="flattenTeams")
        include_org_users: Optional[bool] = Field(serialization_alias="includeOrgUsers")
    def get_all_users(self,
        path_params: GetAllUsersPathParams,
        query_params: Optional[GetAllUsersQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Users in One Project
        - Document: [Get All Users](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/get-all-users-in-one-group/)
        - Resource: `GET /groups/{PROJECT-ID}/users`
        - Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/users",
            path_params,
            query_params,
            None,
        )
    class GetByAgentApiKeyPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        agent_api_key: str = Field("None", serialization_alias="AGENT-API-KEY")
    class GetByAgentApiKeyQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_by_agent_api_key(self,
        path_params: GetByAgentApiKeyPathParams,
        query_params: Optional[GetByAgentApiKeyQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Project by Agent API Key
        - Document: [Get by Agent API Key](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/get-one-group-by-agent-api-key/)
        - Resource: `GET /groups/byAgentApiKey/{AGENT-API-KEY}`
        - Description: No description."""
        return self._request(
            "GET",
            "/groups/byAgentApiKey/{AGENT-API-KEY}",
            path_params,
            query_params,
            None,
        )
    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetByIdQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_by_id(self,
        path_params: GetByIdPathParams,
        query_params: Optional[GetByIdQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Project by ID
        - Document: [Get by ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/get-one-group-by-id/)
        - Resource: `GET /groups/{PROJECT-ID}`
        - Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}",
            path_params,
            query_params,
            None,
        )
    class GetByNamePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_name: str = Field("None", serialization_alias="GROUP-NAME")
    class GetByNameQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_by_name(self,
        path_params: GetByNamePathParams,
        query_params: Optional[GetByNameQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Project by Name
        - Document: [Get by Name](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/get-one-group-by-name/)
        - Resource: `GET /groups/byName/{GROUP-NAME}`
        - Description: No description."""
        return self._request(
            "GET",
            "/groups/byName/{GROUP-NAME}",
            path_params,
            query_params,
            None,
        )
    class AddTeamsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class AddTeamsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class AddTeamsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        role_names: Optional[list[Any]] = Field(serialization_alias="roleNames")
        team_id: Optional[str] = Field("None", serialization_alias="teamId")
    def add_teams(self,
        path_params: AddTeamsPathParams,
        query_params: Optional[AddTeamsQueryParams],
        body_params: list[Optional[AddTeamsBodyParams]],
    ) -> dict[str, Any]:
        """
        ## Add Teams to a Project
        - Document: [Add Teams](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/project-add-team/)
        - Resource: `POST /groups/{PROJECT-ID}/teams`
        - Description: No description."""
        return self._request(
            "POST",
            "/groups/{PROJECT-ID}/teams",
            path_params,
            query_params,
            body_params,
        )
    class GetAllTeamsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetAllTeamsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_all_teams(self,
        path_params: GetAllTeamsPathParams,
        query_params: Optional[GetAllTeamsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Teams in One Project
        - Document: [Get All Teams](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/project-get-teams/)
        - Resource: `GET /groups/{PROJECT-ID}/teams`
        - Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/teams",
            path_params,
            query_params,
            None,
        )
    class RemoveUserPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        user_id: str = Field("None", serialization_alias="USER-ID")
    class RemoveUserQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def remove_user(self,
        path_params: RemoveUserPathParams,
        query_params: Optional[RemoveUserQueryParams],
    ) -> dict[str, Any]:
        """
        ## Remove One User from One Project
        - Document: [Remove User](https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/remove-one-user-from-one-group/)
        - Resource: `DELETE /groups/{PROJECT-ID}/users/{USER-ID}`
        - Description: No description."""
        return self._request(
            "DELETE",
            "/groups/{PROJECT-ID}/users/{USER-ID}",
            path_params,
            query_params,
            None,
        )
    class CreateInvitationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="GROUP-ID")
    class CreateInvitationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class CreateInvitationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        roles: Optional[list[str]] = Field(serialization_alias="roles")
        username: Optional[str] = Field("None", serialization_alias="username")
    def create_invitation(self,
        path_params: CreateInvitationPathParams,
        query_params: Optional[CreateInvitationQueryParams],
        body_params: Optional[CreateInvitationBodyParams],
    ) -> dict[str, Any]:
        """
        ## Create One Project Invitation
        - Document: [Create Invitation](https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/projects/create-one-invitation/)
        - Resource: `POST /groups/{GROUP-ID}/invites/`
        - Description: Retrieve details for one pending invitation to the specified Ops Manager project."""
        return self._request(
            "POST",
            "/groups/{GROUP-ID}/invites/",
            path_params,
            query_params,
            body_params,
        )
    class DeleteInvitationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="GROUP-ID")
        invitation_id: str = Field("None", serialization_alias="INVITATION-ID")
    class DeleteInvitationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def delete_invitation(self,
        path_params: DeleteInvitationPathParams,
        query_params: Optional[DeleteInvitationQueryParams],
    ) -> dict[str, Any]:
        """
        ## Delete One Project Invitation
        - Document: [Delete Invitation](https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/projects/delete-one-invitation/)
        - Resource: `DELETE /groups/{GROUP-ID}/invites/{INVITATION-ID}`
        - Description: Deletes one pending invitation to the Ops Manager project that you specify. You can't delete an invitation that a user has accepted."""
        return self._request(
            "DELETE",
            "/groups/{GROUP-ID}/invites/{INVITATION-ID}",
            path_params,
            query_params,
            None,
        )
    class GetAllInvitationsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="GROUP-ID")
    class GetAllInvitationsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        username: Optional[str] = Field("None", serialization_alias="username")
    def get_all_invitations(self,
        path_params: GetAllInvitationsPathParams,
        query_params: Optional[GetAllInvitationsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Project Invitations
        - Document: [Get All Invitations](https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/projects/get-all-invitations/)
        - Resource: `GET /groups/{GROUP-ID}/invites`
        - Description: Retrieves all pending invitations to the specified Ops Manager project."""
        return self._request(
            "GET",
            "/groups/{GROUP-ID}/invites",
            path_params,
            query_params,
            None,
        )
    class GetOneInvitationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="GROUP-ID")
        invitation_id: str = Field("None", serialization_alias="INVITATION-ID")
    class GetOneInvitationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_one_invitation(self,
        path_params: GetOneInvitationPathParams,
        query_params: Optional[GetOneInvitationQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Project Invitation
        - Document: [Get One Invitation](https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/projects/get-one-invitation/)
        - Resource: `GET /groups/{GROUP-ID}/invites/{INVITATION-ID}`
        - Description: Retrieve details for one pending invitation to the specified Ops Manager project."""
        return self._request(
            "GET",
            "/groups/{GROUP-ID}/invites/{INVITATION-ID}",
            path_params,
            query_params,
            None,
        )
    class UpdateInvitationByInvitationIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="GROUP-ID")
        invitation_id: str = Field("None", serialization_alias="INVITATION-ID")
    class UpdateInvitationByInvitationIdQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class UpdateInvitationByInvitationIdBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        roles: list[str] = Field(serialization_alias="roles")
    def update_invitation_by_invitation_id(self,
        path_params: UpdateInvitationByInvitationIdPathParams,
        query_params: Optional[UpdateInvitationByInvitationIdQueryParams],
        body_params: UpdateInvitationByInvitationIdBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update One Project Invitation by Invitation ID
        - Document: [Update Invitation by Invitation ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/projects/update-one-invitation-by-id/)
        - Resource: `PATCH /groups/{GROUP-ID}/invites/{INVITATION-ID}`
        - Description: Updates one pending invitation by {INVITATION-ID} to the Ops Manager project that you specify."""
        return self._request(
            "PATCH",
            "/groups/{GROUP-ID}/invites/{INVITATION-ID}",
            path_params,
            query_params,
            body_params,
        )
    class UpdateInvitationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="GROUP-ID")
    class UpdateInvitationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class UpdateInvitationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        roles: list[str] = Field(serialization_alias="roles")
        username: str = Field("None", serialization_alias="username")
    def update_invitation(self,
        path_params: UpdateInvitationPathParams,
        query_params: Optional[UpdateInvitationQueryParams],
        body_params: UpdateInvitationBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update One Project Invitation
        - Document: [Update Invitation](https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/projects/update-one-invitation/)
        - Resource: `PATCH /groups/{GROUP-ID}/invites`
        - Description: Updates one pending invitation to the Ops Manager project that you specify."""
        return self._request(
            "PATCH",
            "/groups/{GROUP-ID}/invites",
            path_params,
            query_params,
            body_params,
        )
    class RemoveTeamPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        team_id: str = Field("None", serialization_alias="TEAM-ID")
    class RemoveTeamQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    def remove_team(self,
        path_params: RemoveTeamPathParams,
        query_params: Optional[RemoveTeamQueryParams],
    ) -> dict[str, Any]:
        """
        ## Remove One Team From One Project
        - Document: [Remove Team](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-remove-from-project/)
        - Resource: `DELETE /groups/{PROJECT-ID}/teams/{TEAM-ID}`
        - Description: No description."""
        return self._request(
            "DELETE",
            "/groups/{PROJECT-ID}/teams/{TEAM-ID}",
            path_params,
            query_params,
            None,
        )