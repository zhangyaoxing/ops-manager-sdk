from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class TeamsResource(BaseResource):
    """Client for TeamsResource resource."""
    class AddUsersPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field(alias="ORG-ID")
        team_id: str = Field(alias="TEAM-ID")
    class AddUsersQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class AddUsersBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        id: Optional[str] = Field(alias="id")
    def add_users(self,
        path_params: AddUsersPathParams,
        query_params: Optional[AddUsersQueryParams],
        body_params: Optional[AddUsersBodyParams],
    ) -> dict[str, Any]:
        """API: Add Users to Team
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-add-user/
        Description: No description found."""
        return self._request(
            "POST",
            "/orgs/{ORG-ID}/teams/{TEAM-ID}/users",
            path_params,
            query_params,
            body_params,
        )
    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field(alias="ORG-ID")
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        name: Optional[str] = Field(alias="name")
    def create(self,
        path_params: CreatePathParams,
        query_params: Optional[CreateQueryParams],
        body_params: Optional[CreateBodyParams],
    ) -> dict[str, Any]:
        """API: Create a Team
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-create-one/
        Description: No description found."""
        return self._request(
            "POST",
            "/orgs/{ORG-ID}/teams",
            path_params,
            query_params,
            body_params,
        )
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field(alias="ORG-ID")
        team_id: str = Field(alias="TEAM-ID")
    class DeleteQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class DeleteBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def delete(self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
        body_params: Optional[DeleteBodyParams],
    ) -> dict[str, Any]:
        """API: Delete One Team
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-delete-one/
        Description: No description found."""
        return self._request(
            "DELETE",
            "/orgs/{ORG-ID}/teams/{TEAM-ID}",
            path_params,
            query_params,
            body_params,
        )
    class GetAllTeamUsersPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field(alias="ORG-ID")
        team_id: str = Field(alias="TEAM-ID")
    class GetAllTeamUsersQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetAllTeamUsersBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all_team_users(self,
        path_params: GetAllTeamUsersPathParams,
        query_params: Optional[GetAllTeamUsersQueryParams],
        body_params: Optional[GetAllTeamUsersBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Users Assigned to a Team
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-get-all-users/
        Description: No description found."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/teams/{TEAM-ID}/users",
            path_params,
            query_params,
            body_params,
        )
    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field(alias="ORG-ID")
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetAllBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all(self,
        path_params: GetAllPathParams,
        query_params: Optional[GetAllQueryParams],
        body_params: Optional[GetAllBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Teams
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-get-all/
        Description: No description found."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/teams",
            path_params,
            query_params,
            body_params,
        )
    class GetOneByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field(alias="ORG-ID")
        team_id: str = Field(alias="TEAM-ID")
    class GetOneByIdQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetOneByIdBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_one_by_id(self,
        path_params: GetOneByIdPathParams,
        query_params: Optional[GetOneByIdQueryParams],
        body_params: Optional[GetOneByIdBodyParams],
    ) -> dict[str, Any]:
        """API: Get One Team by ID
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-get-one-by-id/
        Description: No description found."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/teams/{TEAM-ID}",
            path_params,
            query_params,
            body_params,
        )
    class GetOneByNamePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field(alias="ORG-ID")
        team_name: str = Field(alias="TEAM-NAME")
    class GetOneByNameQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetOneByNameBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_one_by_name(self,
        path_params: GetOneByNamePathParams,
        query_params: Optional[GetOneByNameQueryParams],
        body_params: Optional[GetOneByNameBodyParams],
    ) -> dict[str, Any]:
        """API: Get One Team by Name
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-get-one-by-name/
        Description: No description found."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/teams/byName/{TEAM-NAME}",
            path_params,
            query_params,
            body_params,
        )
    class RemoveUserPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field(alias="ORG-ID")
        team_id: str = Field(alias="TEAM-ID")
        user_id: str = Field(alias="USER-ID")
    class RemoveUserQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class RemoveUserBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def remove_user(self,
        path_params: RemoveUserPathParams,
        query_params: Optional[RemoveUserQueryParams],
        body_params: Optional[RemoveUserBodyParams],
    ) -> dict[str, Any]:
        """API: Remove a User from a Team
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-remove-user/
        Description: No description found."""
        return self._request(
            "DELETE",
            "/orgs/{ORG-ID}/teams/{TEAM-ID}/users/{USER-ID}",
            path_params,
            query_params,
            body_params,
        )
    class RenamePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field(alias="ORG-ID")
        team_id: str = Field(alias="TEAM-ID")
    class RenameQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class RenameBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        name: Optional[Any] = Field(alias="name")
    def rename(self,
        path_params: RenamePathParams,
        query_params: Optional[RenameQueryParams],
        body_params: Optional[RenameBodyParams],
    ) -> dict[str, Any]:
        """API: Rename a Team
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-rename-one/
        Description: No description found."""
        return self._request(
            "PATCH",
            "/orgs/{ORG-ID}/teams/{TEAM-ID}",
            path_params,
            query_params,
            body_params,
        )
    class UpdateRolesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
        team_id: str = Field(alias="TEAM-ID")
    class UpdateRolesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(alias="envelope")
        pretty: Optional[bool] = Field(alias="pretty")
    class UpdateRolesBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        role_names: list[Any] = Field(alias="roleNames")
    def update_roles(self,
        path_params: UpdateRolesPathParams,
        query_params: Optional[UpdateRolesQueryParams],
        body_params: UpdateRolesBodyParams,
    ) -> dict[str, Any]:
        """API: Update Team Roles in One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-update-roles/
        Description: No description found."""
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/teams/{TEAM-ID}",
            path_params,
            query_params,
            body_params,
        )