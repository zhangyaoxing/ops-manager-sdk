from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class OrganizationsResource(BaseResource):
    """Client for OrganizationsResource resource."""
    class InviteUserPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
    class InviteUserQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class InviteUserBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        roles: list[str] = Field(serialization_alias="roles")
        team_ids: Optional[list[str]] = Field(serialization_alias="teamIds")
        username: str = Field("None", serialization_alias="username")
    def invite_user(self,
        path_params: InviteUserPathParams,
        query_params: Optional[InviteUserQueryParams],
        body_params: InviteUserBodyParams,
    ) -> dict[str, Any]:
        """API: Invite One User to an Ops Manager Organization
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/organizations/create-one-invitation/
        Description: Invites one user to the Ops Manager organization that you specify."""
        return self._request(
            "POST",
            "/orgs/{ORG-ID}/invites",
            path_params,
            query_params,
            body_params,
        )
    class DeleteInvitationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        invitation_id: str = Field("None", serialization_alias="INVITATION-ID")
        org_id: str = Field("None", serialization_alias="ORG-ID")
    class DeleteInvitationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def delete_invitation(self,
        path_params: DeleteInvitationPathParams,
        query_params: Optional[DeleteInvitationQueryParams],
    ) -> dict[str, Any]:
        """API: Delete One Organization Invitation
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/organizations/delete-one-invitation/
        Description: Deletes one pending invitation to the specified Ops Manager organization. You can't delete an invitation that a user has accepted."""
        return self._request(
            "DELETE",
            "/orgs/{ORG-ID}/invites/{INVITATION-ID}",
            path_params,
            query_params,
            None,
        )
    class GetAllInvitationsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
    class GetAllInvitationsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        username: Optional[str] = Field("None", serialization_alias="username")
    def get_all_invitations(self,
        path_params: GetAllInvitationsPathParams,
        query_params: Optional[GetAllInvitationsQueryParams],
    ) -> dict[str, Any]:
        """API: Get All Organization Invitations
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/organizations/get-all-invitations/
        Description: Retrieves all pending invitations to the specified Ops Manager organization."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/invites",
            path_params,
            query_params,
            None,
        )
    class GetOneInvitationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        invitation_id: str = Field("None", serialization_alias="INVITATION-ID")
        org_id: str = Field("None", serialization_alias="ORG-ID")
    class GetOneInvitationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_one_invitation(self,
        path_params: GetOneInvitationPathParams,
        query_params: Optional[GetOneInvitationQueryParams],
    ) -> dict[str, Any]:
        """API: Get One Organization Invitation
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/organizations/get-one-invitation/
        Description: Retrieve details for one pending invitation to the specified Ops Manager organization."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/invites/{INVITATION-ID}",
            path_params,
            query_params,
            None,
        )
    class UpdateByInvitationIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        invitation_id: str = Field("None", serialization_alias="INVITATION-ID")
        org_id: str = Field("None", serialization_alias="ORG-ID")
    class UpdateByInvitationIdQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class UpdateByInvitationIdBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        roles: list[str] = Field(serialization_alias="roles")
    def update_by_invitation_id(self,
        path_params: UpdateByInvitationIdPathParams,
        query_params: Optional[UpdateByInvitationIdQueryParams],
        body_params: UpdateByInvitationIdBodyParams,
    ) -> dict[str, Any]:
        """API: Update One Organization Invitation by Invitation ID
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/organizations/update-one-invitation-by-id/
        Description: Updates one pending invitation by {INVITATION-ID} to the Ops Manager organization that you specify."""
        return self._request(
            "PATCH",
            "/orgs/{ORG-ID}/invites/{INVITATION-ID}",
            path_params,
            query_params,
            body_params,
        )
    class UpdateInvitationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
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
        """API: Update One Organization Invitation
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/organizations/update-one-invitation/
        Description: Updates one pending invitation to the Ops Manager organization that you specify."""
        return self._request(
            "PATCH",
            "/orgs/{ORG-ID}/invites",
            path_params,
            query_params,
            body_params,
        )
    class CreateOrganizationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class CreateOrganizationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        class LdapgroupmappingsParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            ldap_groups: Optional[list[Any]] = Field(serialization_alias="ldapGroups")
            role_name: Optional[str] = Field("None", serialization_alias="roleName")
        ldap_group_mappings: Optional[list[LdapgroupmappingsParams]] = Field(serialization_alias="ldapGroupMappings")
        name: str = Field("None", serialization_alias="name")
    def create_organization(self,
        query_params: Optional[CreateOrganizationQueryParams],
        body_params: CreateOrganizationBodyParams,
    ) -> dict[str, Any]:
        """API: Create One Organization
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/organizations/organization-create-one/
        Description: No description."""
        return self._request(
            "POST",
            "/orgs",
            None,
            query_params,
            body_params,
        )
    class DeleteOrganizationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
    class DeleteOrganizationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def delete_organization(self,
        path_params: DeleteOrganizationPathParams,
        query_params: Optional[DeleteOrganizationQueryParams],
    ) -> dict[str, Any]:
        """API: Delete One Organization
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/organizations/organization-delete-one/
        Description: No description."""
        return self._request(
            "DELETE",
            "/orgs/{ORG-ID}",
            path_params,
            query_params,
            None,
        )
    class GetAllProjectsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
    class GetAllProjectsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        name: Optional[str] = Field("None", serialization_alias="name")
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    def get_all_projects(self,
        path_params: GetAllProjectsPathParams,
        query_params: Optional[GetAllProjectsQueryParams],
    ) -> dict[str, Any]:
        """API: Get All Projects in an Organization
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/organizations/organization-get-all-projects/
        Description: No description."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/groups",
            path_params,
            query_params,
            None,
        )
    class GetAllUsersPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
    class GetAllUsersQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    def get_all_users(self,
        path_params: GetAllUsersPathParams,
        query_params: Optional[GetAllUsersQueryParams],
    ) -> dict[str, Any]:
        """API: Get All Organization Users
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/organizations/organization-get-all-users/
        Description: No description."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/users",
            path_params,
            query_params,
            None,
        )
    class GetAllOrganizationsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        include_deleted_orgs: Optional[bool] = Field(serialization_alias="includeDeletedOrgs")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        name: Optional[str] = Field("None", serialization_alias="name")
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    def get_all_organizations(self,
        query_params: Optional[GetAllOrganizationsQueryParams],
    ) -> dict[str, Any]:
        """API: Get All Organizations
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/organizations/organization-get-all/
        Description: No description."""
        return self._request(
            "GET",
            "/orgs",
            None,
            query_params,
            None,
        )
    class GetOneOrganizationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
    class GetOneOrganizationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        include_deleted_orgs: Optional[bool] = Field(serialization_alias="includeDeletedOrgs")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    def get_one_organization(self,
        path_params: GetOneOrganizationPathParams,
        query_params: Optional[GetOneOrganizationQueryParams],
    ) -> dict[str, Any]:
        """API: Get One Organization
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/organizations/organization-get-one/
        Description: No description."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}",
            path_params,
            query_params,
            None,
        )
    class RenameOrganizationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
    class RenameOrganizationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class RenameOrganizationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        ldap_group_mappings: Optional[list[dict]] = Field(serialization_alias="ldapGroupMappings")
        name: Optional[str] = Field("None", serialization_alias="name")
    def rename_organization(self,
        path_params: RenameOrganizationPathParams,
        query_params: Optional[RenameOrganizationQueryParams],
        body_params: Optional[RenameOrganizationBodyParams],
    ) -> dict[str, Any]:
        """API: Update One Organization
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/organizations/organization-rename/
        Description: Use this endpoint to make any of the following changes to one organization:"""
        return self._request(
            "PATCH",
            "/orgs/{ORG-ID}",
            path_params,
            query_params,
            body_params,
        )