from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class TeamsResource(BaseResource):
    """Client for TeamsResource resource."""
    class AddUsersPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
        team_id: str = Field("None", serialization_alias="TEAM-ID")
    class AddUsersQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class AddUsersBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        id: Optional[str] = Field("None", serialization_alias="id")
    def add_users(self,
        path_params: AddUsersPathParams,
        query_params: Optional[AddUsersQueryParams],
        body_params: list[Optional[AddUsersBodyParams]],
    ) -> dict[str, Any]:
        """
        ## Add Users to Team
        - Document: [Add Users](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-add-user/)
        - Resource: `POST /orgs/{ORG-ID}/teams/{TEAM-ID}/users`
        - Description: No description."""
        return self._request(
            "POST",
            "/orgs/{ORG-ID}/teams/{TEAM-ID}/users",
            path_params,
            query_params,
            body_params,
        )
    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        name: Optional[str] = Field("None", serialization_alias="name")
    def create(self,
        path_params: CreatePathParams,
        query_params: Optional[CreateQueryParams],
        body_params: Optional[CreateBodyParams],
    ) -> dict[str, Any]:
        """
        ## Create a Team
        - Document: [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-create-one/)
        - Resource: `POST /orgs/{ORG-ID}/teams`
        - Description: No description."""
        return self._request(
            "POST",
            "/orgs/{ORG-ID}/teams",
            path_params,
            query_params,
            body_params,
        )
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
        team_id: str = Field("None", serialization_alias="TEAM-ID")
    class DeleteQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def delete(self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
    ) -> dict[str, Any]:
        """
        ## Delete One Team
        - Document: [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-delete-one/)
        - Resource: `DELETE /orgs/{ORG-ID}/teams/{TEAM-ID}`
        - Description: No description."""
        return self._request(
            "DELETE",
            "/orgs/{ORG-ID}/teams/{TEAM-ID}",
            path_params,
            query_params,
            None,
        )
    class GetAllTeamUsersPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
        team_id: str = Field("None", serialization_alias="TEAM-ID")
    class GetAllTeamUsersQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_all_team_users(self,
        path_params: GetAllTeamUsersPathParams,
        query_params: Optional[GetAllTeamUsersQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Users Assigned to a Team
        - Document: [Get All Team Users](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-get-all-users/)
        - Resource: `GET /orgs/{ORG-ID}/teams/{TEAM-ID}/users`
        - Description: No description."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/teams/{TEAM-ID}/users",
            path_params,
            query_params,
            None,
        )
    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_all(self,
        path_params: GetAllPathParams,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get All Teams
        - Document: [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-get-all/)
        - Resource: `GET /orgs/{ORG-ID}/teams`
        - Description: No description."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/teams",
            path_params,
            query_params,
            None,
        )
    class GetOneByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
        team_id: str = Field("None", serialization_alias="TEAM-ID")
    class GetOneByIdQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_one_by_id(self,
        path_params: GetOneByIdPathParams,
        query_params: Optional[GetOneByIdQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Team by ID
        - Document: [Get One by ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-get-one-by-id/)
        - Resource: `GET /orgs/{ORG-ID}/teams/{TEAM-ID}`
        - Description: No description."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/teams/{TEAM-ID}",
            path_params,
            query_params,
            None,
        )
    class GetOneByNamePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
        team_name: str = Field("None", serialization_alias="TEAM-NAME")
    class GetOneByNameQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_one_by_name(self,
        path_params: GetOneByNamePathParams,
        query_params: Optional[GetOneByNameQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Team by Name
        - Document: [Get One by Name](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-get-one-by-name/)
        - Resource: `GET /orgs/{ORG-ID}/teams/byName/{TEAM-NAME}`
        - Description: No description."""
        return self._request(
            "GET",
            "/orgs/{ORG-ID}/teams/byName/{TEAM-NAME}",
            path_params,
            query_params,
            None,
        )
    class RemoveUserPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
        team_id: str = Field("None", serialization_alias="TEAM-ID")
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
        ## Remove a User from a Team
        - Document: [Remove User](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-remove-user/)
        - Resource: `DELETE /orgs/{ORG-ID}/teams/{TEAM-ID}/users/{USER-ID}`
        - Description: No description."""
        return self._request(
            "DELETE",
            "/orgs/{ORG-ID}/teams/{TEAM-ID}/users/{USER-ID}",
            path_params,
            query_params,
            None,
        )
    class RenamePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="ORG-ID")
        team_id: str = Field("None", serialization_alias="TEAM-ID")
    class RenameQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class RenameBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        name: Optional[Any] = Field(serialization_alias="name")
    def rename(self,
        path_params: RenamePathParams,
        query_params: Optional[RenameQueryParams],
        body_params: Optional[RenameBodyParams],
    ) -> dict[str, Any]:
        """
        ## Rename a Team
        - Document: [Rename](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-rename-one/)
        - Resource: `PATCH /orgs/{ORG-ID}/teams/{TEAM-ID}`
        - Description: No description."""
        return self._request(
            "PATCH",
            "/orgs/{ORG-ID}/teams/{TEAM-ID}",
            path_params,
            query_params,
            body_params,
        )
    class UpdateRolesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        team_id: str = Field("None", serialization_alias="TEAM-ID")
    class UpdateRolesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    class UpdateRolesBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        role_names: list[Any] = Field(serialization_alias="roleNames")
    def update_roles(self,
        path_params: UpdateRolesPathParams,
        query_params: Optional[UpdateRolesQueryParams],
        body_params: list[UpdateRolesBodyParams],
    ) -> dict[str, Any]:
        """
        ## Update Team Roles in One Project
        - Document: [Update Roles](https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-update-roles/)
        - Resource: `PATCH /groups/{PROJECT-ID}/teams/{TEAM-ID}`
        - Description: No description."""
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/teams/{TEAM-ID}",
            path_params,
            query_params,
            body_params,
        )