from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class UsersResource(BaseResource):
    """Client for UsersResource resource."""
    class CreateFirstUserQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        whitelist: Optional[str] = Field("None", serialization_alias="whitelist")
    class CreateFirstUserBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        email_address: Optional[str] = Field("None", serialization_alias="emailAddress")
        first_name: str = Field("None", serialization_alias="firstName")
        last_name: str = Field("None", serialization_alias="lastName")
        password: str = Field("None", serialization_alias="password")
        username: str = Field("None", serialization_alias="username")
    def create_first_user(self,
        query_params: Optional[CreateFirstUserQueryParams],
        body_params: CreateFirstUserBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create the First User
        - Document: [Create First User](https://www.mongodb.com/docs/ops-manager/current/reference/api/user-create-first/)
        - Resource: `POST /unauth/users`
        - Description: Create the first Ops Manager user. You can call this endpoint without having an API key."""
        return self._request(
            "POST",
            "/unauth/users",
            None,
            query_params,
            body_params,
        )
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        email_address: Optional[str] = Field("None", serialization_alias="emailAddress")
        first_name: Optional[str] = Field("None", serialization_alias="firstName")
        last_name: Optional[str] = Field("None", serialization_alias="lastName")
        mobile_number: Optional[str] = Field("None", serialization_alias="mobileNumber")
        password: Optional[str] = Field("None", serialization_alias="password")
        class RolesParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            group_id: Optional[str] = Field("None", serialization_alias="groupId")
            org_id: Optional[str] = Field("None", serialization_alias="orgId")
            role_name: Optional[str] = Field("None", serialization_alias="roleName")
        roles: Optional[list[RolesParams]] = Field(serialization_alias="roles")
        username: str = Field("None", serialization_alias="username")
    def create(self,
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create One User
        - Document: [Create](https://www.mongodb.com/docs/ops-manager/current/reference/api/user-create/)
        - Resource: `POST /users`
        - Description: Create a new user. By default, any non-global organization and project roles in the payload send users an invitation to the organization or project first."""
        return self._request(
            "POST",
            "/users",
            None,
            query_params,
            body_params,
        )
    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        user_id: str = Field("None", serialization_alias="USER-ID")
    class GetByIdQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_by_id(self,
        path_params: GetByIdPathParams,
        query_params: Optional[GetByIdQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get a User by ID
        - Document: [Get by ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/user-get-by-id/)
        - Resource: `GET /users/{USER-ID}`
        - Description: You can always retrieve your own user account. Otherwise, you must be a global user or you must have the Project User Admin role in at least one project that is common between you and the user you are retrieving."""
        return self._request(
            "GET",
            "/users/{USER-ID}",
            path_params,
            query_params,
            None,
        )
    class GetByNamePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        user_name: str = Field("None", serialization_alias="USER-NAME")
    class GetByNameQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_by_name(self,
        path_params: GetByNamePathParams,
        query_params: Optional[GetByNameQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get a User by Name
        - Document: [Get by Name](https://www.mongodb.com/docs/ops-manager/current/reference/api/user-get-by-name/)
        - Resource: `GET /users/byName/{USER-NAME}`
        - Description: You can always retrieve your own user account. Otherwise, you must be a global user or you must have the Project User Admin role in at least one project that is common between you and the user you are retrieving."""
        return self._request(
            "GET",
            "/users/byName/{USER-NAME}",
            path_params,
            query_params,
            None,
        )
    class UpdateRolesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        user_id: str = Field("None", serialization_alias="USER-ID")
    class UpdateRolesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class UpdateRolesBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        class RolesParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            group_id: Optional[str] = Field("None", serialization_alias="groupId")
            org_id: Optional[str] = Field("None", serialization_alias="orgId")
            role_name: Optional[str] = Field("None", serialization_alias="roleName")
        roles: list[RolesParams] = Field(serialization_alias="roles")
    def update_roles(self,
        path_params: UpdateRolesPathParams,
        query_params: Optional[UpdateRolesQueryParams],
        body_params: UpdateRolesBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update Roles for One User
        - Document: [Update Roles](https://www.mongodb.com/docs/ops-manager/current/reference/api/user-update/)
        - Resource: `PATCH /users/{USER-ID}`
        - Description: Add, update, or remove a user's roles within an organization or project. By default, any new non-global organization and project roles in the payload send users an invitation to the organization or project first. You can add users directly to an organization or project only if you set the mms.user.bypassInviteForExistingUsers setting to true."""
        return self._request(
            "PATCH",
            "/users/{USER-ID}",
            path_params,
            query_params,
            body_params,
        )
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        user_id: str = Field("None", serialization_alias="USER-ID")
    class DeleteQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def delete(self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
    ) -> dict[str, Any]:
        """
        ## Remove One User
        - Document: [Delete](https://www.mongodb.com/docs/ops-manager/current/reference/api/users/delete-one-user/)
        - Resource: `DELETE /users/{USER-ID}`
        - Description: Removes one user from Ops Manager by user ID."""
        return self._request(
            "DELETE",
            "/users/{USER-ID}",
            path_params,
            query_params,
            None,
        )