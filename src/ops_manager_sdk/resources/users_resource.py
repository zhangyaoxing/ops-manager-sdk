from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class UsersResource(BaseResource):
    """Client for UsersResource resource."""
    class CreateFirstUserPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class CreateFirstUserQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        whitelist: Optional[str] = Field(alias="whitelist")
    class CreateFirstUserBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        username: str = Field(alias="username")
        password: str = Field(alias="password")
        email_address: Optional[str] = Field(alias="emailAddress")
        first_name: str = Field(alias="firstName")
        last_name: str = Field(alias="lastName")
    def create_first_user(self,
        path_params: Optional[CreateFirstUserPathParams],
        query_params: Optional[CreateFirstUserQueryParams],
        body_params: CreateFirstUserBodyParams,
    ) -> dict[str, Any]:
        """API: Create the First User
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/user-create-first/
        Description: Create the first Ops Manager user. You can call this endpoint without having an API key."""
        return self._request(
            "POST",
            "/unauth/users",
            path_params,
            query_params,
            body_params,
        )
    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        username: str = Field(alias="username")
        password: Optional[str] = Field(alias="password")
        email_address: Optional[str] = Field(alias="emailAddress")
        mobile_number: Optional[str] = Field(alias="mobileNumber")
        first_name: Optional[str] = Field(alias="firstName")
        last_name: Optional[str] = Field(alias="lastName")
        roles: Optional[list[dict]] = Field(alias="roles")
        roles.org_id: Optional[str] = Field(alias="roles.orgId")
        roles.group_id: Optional[str] = Field(alias="roles.groupId")
        roles.role_name: Optional[str] = Field(alias="roles.roleName")
    def create(self,
        path_params: Optional[CreatePathParams],
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """API: Create One User
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/user-create/
        Description: Create a new user. By default, any non-global organization and project roles in the payload send users an invitation to the organization or project first."""
        return self._request(
            "POST",
            "/users",
            path_params,
            query_params,
            body_params,
        )
    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        user_id: str = Field(alias="USER-ID")
    class GetByIdQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetByIdBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_by_id(self,
        path_params: GetByIdPathParams,
        query_params: Optional[GetByIdQueryParams],
        body_params: Optional[GetByIdBodyParams],
    ) -> dict[str, Any]:
        """API: Get a User by ID
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/user-get-by-id/
        Description: You can always retrieve your own user account. Otherwise, you must be a global user or you must have the Project User Admin role in at least one project that is common between you and the user you are retrieving."""
        return self._request(
            "GET",
            "/users/{USER-ID}",
            path_params,
            query_params,
            body_params,
        )
    class GetByNamePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        user_name: str = Field(alias="USER-NAME")
    class GetByNameQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetByNameBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_by_name(self,
        path_params: GetByNamePathParams,
        query_params: Optional[GetByNameQueryParams],
        body_params: Optional[GetByNameBodyParams],
    ) -> dict[str, Any]:
        """API: Get a User by Name
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/user-get-by-name/
        Description: You can always retrieve your own user account. Otherwise, you must be a global user or you must have the Project User Admin role in at least one project that is common between you and the user you are retrieving."""
        return self._request(
            "GET",
            "/users/byName/{USER-NAME}",
            path_params,
            query_params,
            body_params,
        )
    class UpdateRolesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        user_id: str = Field(alias="USER-ID")
    class UpdateRolesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class UpdateRolesBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        roles: list[dict] = Field(alias="roles")
        roles.org_id: Optional[str] = Field(alias="roles.orgId")
        roles.group_id: Optional[str] = Field(alias="roles.groupId")
        roles.role_name: Optional[str] = Field(alias="roles.roleName")
    def update_roles(self,
        path_params: UpdateRolesPathParams,
        query_params: Optional[UpdateRolesQueryParams],
        body_params: UpdateRolesBodyParams,
    ) -> dict[str, Any]:
        """API: Update Roles for One User
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/user-update/
        Description: Add, update, or remove a user's roles within an organization or project. By default, any new non-global organization and project roles in the payload send users an invitation to the organization or project first. You can add users directly to an organization or project only if you set the mms.user.bypassInviteForExistingUsers setting to true."""
        return self._request(
            "PATCH",
            "/users/{USER-ID}",
            path_params,
            query_params,
            body_params,
        )
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        user_id: str = Field(alias="USER-ID")
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
        """API: Remove One User
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/users/delete-one-user/
        Description: Removes one user from Ops Manager by user ID."""
        return self._request(
            "DELETE",
            "/users/{USER-ID}",
            path_params,
            query_params,
            body_params,
        )