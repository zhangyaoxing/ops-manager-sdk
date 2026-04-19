from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class OrganizationsResource(BaseResource):
    """Client for OrganizationsResource resource."""
    class InviteUserPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
    class InviteUserQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
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
        org_id: str = Field("None", serialization_alias="ORG-ID")
        invitation_id: str = Field("None", serialization_alias="INVITATION-ID")
    class DeleteInvitationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class DeleteInvitationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def delete_invitation(self,
        path_params: DeleteInvitationPathParams,
        query_params: Optional[DeleteInvitationQueryParams],
        body_params: Optional[DeleteInvitationBodyParams],
    ) -> dict[str, Any]:
        """API: Delete One Organization Invitation
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/organizations/delete-one-invitation/
        Description: Deletes one pending invitation to the specified Ops Manager organization. You can't delete an invitation that a user has accepted."""
        return self._request(
            "DELETE",
            "/orgs/{ORG-ID}/invites/{INVITATION-ID}",
            path_params,
            query_params,
            body_params,
        )
    class GetAllInvitationsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
    class GetAllInvitationsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        username: Optional[str] = Field("None", serialization_alias="username")
    class GetAllInvitationsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all_invitations(self,
        path_params: GetAllInvitationsPathParams,
        query_params: Optional[GetAllInvitationsQueryParams],
        body_params: Optional[GetAllInvitationsBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Organization Invitations
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/organizations/get-all-invitations/
        Description: Retrieves all pending invitations to the specified Ops Manager organization."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/invites",
            path_params,
            query_params,
            body_params,
        )
    class GetOneInvitationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
        invitation_id: str = Field("None", serialization_alias="INVITATION-ID")
    class GetOneInvitationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class GetOneInvitationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_one_invitation(self,
        path_params: GetOneInvitationPathParams,
        query_params: Optional[GetOneInvitationQueryParams],
        body_params: Optional[GetOneInvitationBodyParams],
    ) -> dict[str, Any]:
        """API: Get One Organization Invitation
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/organizations/get-one-invitation/
        Description: Retrieve details for one pending invitation to the specified Ops Manager organization."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/invites/{INVITATION-ID}",
            path_params,
            query_params,
            body_params,
        )
    class UpdateByInvitationIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
        invitation_id: str = Field("None", serialization_alias="INVITATION-ID")
    class UpdateByInvitationIdQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
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
    class CreateOrganizationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class CreateOrganizationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class CreateOrganizationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        ldap_group_mappings: Optional[list[Any]] = Field(serialization_alias="ldapGroupMappings")
        name: str = Field("None", serialization_alias="name")
    def create_organization(self,
        path_params: Optional[CreateOrganizationPathParams],
        query_params: Optional[CreateOrganizationQueryParams],
        body_params: CreateOrganizationBodyParams,
    ) -> dict[str, Any]:
        """API: Create One Organization
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/organizations/organization-create-one/
        Description: No description found."""
        return self._request(
            "POST",
            "/orgs",
            path_params,
            query_params,
            body_params,
        )
    class DeleteOrganizationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
    class DeleteOrganizationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class DeleteOrganizationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def delete_organization(self,
        path_params: DeleteOrganizationPathParams,
        query_params: Optional[DeleteOrganizationQueryParams],
        body_params: Optional[DeleteOrganizationBodyParams],
    ) -> dict[str, Any]:
        """API: Delete One Organization
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/organizations/organization-delete-one/
        Description: No description found."""
        return self._request(
            "DELETE",
            "/orgs/{ORG-ID}",
            path_params,
            query_params,
            body_params,
        )
    class GetAllProjectsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
    class GetAllProjectsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        name: Optional[str] = Field("None", serialization_alias="name")
    class GetAllProjectsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all_projects(self,
        path_params: GetAllProjectsPathParams,
        query_params: Optional[GetAllProjectsQueryParams],
        body_params: Optional[GetAllProjectsBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Projects in an Organization
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/organizations/organization-get-all-projects/
        Description: No description found."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/groups",
            path_params,
            query_params,
            body_params,
        )
    class GetAllUsersPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
    class GetAllUsersQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    class GetAllUsersBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all_users(self,
        path_params: GetAllUsersPathParams,
        query_params: Optional[GetAllUsersQueryParams],
        body_params: Optional[GetAllUsersBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Organization Users
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/organizations/organization-get-all-users/
        Description: No description found."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/users",
            path_params,
            query_params,
            body_params,
        )
    class GetAllOrganizationsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class GetAllOrganizationsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        name: Optional[str] = Field("None", serialization_alias="name")
        include_deleted_orgs: Optional[bool] = Field(serialization_alias="includeDeletedOrgs")
    class GetAllOrganizationsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all_organizations(self,
        path_params: Optional[GetAllOrganizationsPathParams],
        query_params: Optional[GetAllOrganizationsQueryParams],
        body_params: Optional[GetAllOrganizationsBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Organizations
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/organizations/organization-get-all/
        Description: No description found."""
        return self._request(
            "GET",
            "/orgs",
            path_params,
            query_params,
            body_params,
        )
    class GetOneOrganizationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
    class GetOneOrganizationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        include_deleted_orgs: Optional[bool] = Field(serialization_alias="includeDeletedOrgs")
    class GetOneOrganizationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_one_organization(self,
        path_params: GetOneOrganizationPathParams,
        query_params: Optional[GetOneOrganizationQueryParams],
        body_params: Optional[GetOneOrganizationBodyParams],
    ) -> dict[str, Any]:
        """API: Get One Organization
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/organizations/organization-get-one/
        Description: No description found."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}",
            path_params,
            query_params,
            body_params,
        )
    class RenameOrganizationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
    class RenameOrganizationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class RenameOrganizationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        name: Optional[str] = Field("None", serialization_alias="name")
        ldap_group_mappings: Optional[list[dict]] = Field(serialization_alias="ldapGroupMappings")
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