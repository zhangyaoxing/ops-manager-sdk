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
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class AddExistingUsersBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        id: Optional[str] = Field("None", serialization_alias="id")
        roles: Optional[list[dict]] = Field(serialization_alias="roles")
    def add_existing_users(self,
        path_params: AddExistingUsersPathParams,
        query_params: Optional[AddExistingUsersQueryParams],
        body_params: Optional[AddExistingUsersBodyParams],
    ) -> dict[str, Any]:
        """API: Add Existing Users to One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/add-users-to-one-group/
        Description: This resource adds users who exist in Ops Manager to another project. It does not create new users and add them to a project. By default, users first receive an invitation to the project. You can add users directly to a project only if you set the mms.user.bypassInviteForExistingUsers setting to true."""
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
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        name: Optional[str] = Field("None", serialization_alias="name")
        tags: Optional[list[str]] = Field(serialization_alias="tags")
        ldap_group_mappings: Optional[list[dict]] = Field(serialization_alias="ldapGroupMappings")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """API: Update One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/change-one-group-name/
        Description: Use this endpoint to make any of the following changes to one project:"""
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}",
            path_params,
            query_params,
            body_params,
        )
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        name: str = Field("None", serialization_alias="name")
        org_id: str = Field("None", serialization_alias="orgId")
    def create(self,
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """API: Create One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/create-one-group/
        Description: No description."""
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
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def delete(self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
    ) -> dict[str, Any]:
        """API: Delete One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/delete-one-group/
        Description: No description."""
        return self._request(
            "DELETE",
            "/groups/{PROJECT-ID}",
            path_params,
            query_params,
            None,
        )
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_all(self,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """API: Get All Projects for the Current User
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/get-all-groups-for-current-user/
        Description: No description."""
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
        """API: Get All Projects with Specific Tags for the Current User
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/get-all-groups-with-specific-tags-for-current-user/
        Description: No description."""
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
        """API: Get All Users in One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/get-all-users-in-one-group/
        Description: No description."""
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
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_by_agent_api_key(self,
        path_params: GetByAgentApiKeyPathParams,
        query_params: Optional[GetByAgentApiKeyQueryParams],
    ) -> dict[str, Any]:
        """API: Get One Project by Agent API Key
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/get-one-group-by-agent-api-key/
        Description: No description."""
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
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_by_id(self,
        path_params: GetByIdPathParams,
        query_params: Optional[GetByIdQueryParams],
    ) -> dict[str, Any]:
        """API: Get One Project by ID
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/get-one-group-by-id/
        Description: No description."""
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
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_by_name(self,
        path_params: GetByNamePathParams,
        query_params: Optional[GetByNameQueryParams],
    ) -> dict[str, Any]:
        """API: Get One Project by Name
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/get-one-group-by-name/
        Description: No description."""
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
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class AddTeamsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        role_names: Optional[list[Any]] = Field(serialization_alias="roleNames")
        team_id: Optional[str] = Field("None", serialization_alias="teamId")
    def add_teams(self,
        path_params: AddTeamsPathParams,
        query_params: Optional[AddTeamsQueryParams],
        body_params: list[Optional[AddTeamsBodyParams]],
    ) -> dict[str, Any]:
        """API: Add Teams to a Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/project-add-team/
        Description: No description."""
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
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_all_teams(self,
        path_params: GetAllTeamsPathParams,
        query_params: Optional[GetAllTeamsQueryParams],
    ) -> dict[str, Any]:
        """API: Get All Teams in One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/project-get-teams/
        Description: No description."""
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
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def remove_user(self,
        path_params: RemoveUserPathParams,
        query_params: Optional[RemoveUserQueryParams],
    ) -> dict[str, Any]:
        """API: Remove One User from One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/remove-one-user-from-one-group/
        Description: No description."""
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
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class CreateInvitationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        roles: Optional[list[str]] = Field(serialization_alias="roles")
        username: Optional[str] = Field("None", serialization_alias="username")
    def create_invitation(self,
        path_params: CreateInvitationPathParams,
        query_params: Optional[CreateInvitationQueryParams],
        body_params: Optional[CreateInvitationBodyParams],
    ) -> dict[str, Any]:
        """API: Create One Project Invitation
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/projects/create-one-invitation/
        Description: Retrieve details for one pending invitation to the specified Ops Manager project."""
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
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def delete_invitation(self,
        path_params: DeleteInvitationPathParams,
        query_params: Optional[DeleteInvitationQueryParams],
    ) -> dict[str, Any]:
        """API: Delete One Project Invitation
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/projects/delete-one-invitation/
        Description: Deletes one pending invitation to the Ops Manager project that you specify. You can't delete an invitation that a user has accepted."""
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
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        username: Optional[str] = Field("None", serialization_alias="username")
    def get_all_invitations(self,
        path_params: GetAllInvitationsPathParams,
        query_params: Optional[GetAllInvitationsQueryParams],
    ) -> dict[str, Any]:
        """API: Get All Project Invitations
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/projects/get-all-invitations/
        Description: Retrieves all pending invitations to the specified Ops Manager project."""
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
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_one_invitation(self,
        path_params: GetOneInvitationPathParams,
        query_params: Optional[GetOneInvitationQueryParams],
    ) -> dict[str, Any]:
        """API: Get One Project Invitation
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/projects/get-one-invitation/
        Description: Retrieve details for one pending invitation to the specified Ops Manager project."""
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
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class UpdateInvitationByInvitationIdBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        roles: list[str] = Field(serialization_alias="roles")
    def update_invitation_by_invitation_id(self,
        path_params: UpdateInvitationByInvitationIdPathParams,
        query_params: Optional[UpdateInvitationByInvitationIdQueryParams],
        body_params: UpdateInvitationByInvitationIdBodyParams,
    ) -> dict[str, Any]:
        """API: Update One Project Invitation by Invitation ID
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/projects/update-one-invitation-by-id/
        Description: Updates one pending invitation by {INVITATION-ID} to the Ops Manager project that you specify."""
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
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class UpdateInvitationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        roles: list[str] = Field(serialization_alias="roles")
        username: str = Field("None", serialization_alias="username")
    def update_invitation(self,
        path_params: UpdateInvitationPathParams,
        query_params: Optional[UpdateInvitationQueryParams],
        body_params: UpdateInvitationBodyParams,
    ) -> dict[str, Any]:
        """API: Update One Project Invitation
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/projects/update-one-invitation/
        Description: Updates one pending invitation to the Ops Manager project that you specify."""
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
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
    def remove_team(self,
        path_params: RemoveTeamPathParams,
        query_params: Optional[RemoveTeamQueryParams],
    ) -> dict[str, Any]:
        """API: Remove One Team From One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-remove-from-project/
        Description: No description."""
        return self._request(
            "DELETE",
            "/groups/{PROJECT-ID}/teams/{TEAM-ID}",
            path_params,
            query_params,
            None,
        )