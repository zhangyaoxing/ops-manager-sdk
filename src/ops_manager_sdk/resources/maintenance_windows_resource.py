from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class MaintenanceWindowsResource(BaseResource):
    """Client for MaintenanceWindowsResource resource."""
    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        alert_type_names: list[str] = Field(serialization_alias="alertTypeNames")
        description: Optional[str] = Field("None", serialization_alias="description")
        end_date: str = Field("None", serialization_alias="endDate")
        start_date: str = Field("None", serialization_alias="startDate")
    def create(self,
        path_params: CreatePathParams,
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """API: Create One Maintenance Window
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/maintenance-windows-create-one/
        Description: Create one maintenance window. Ops Manager turns off alert notifications for certain alert types for a period of time you specify to allow maintenance to occur."""
        return self._request(
            "POST",
            "/groups/{PROJECT-ID}/maintenanceWindows/",
            path_params,
            query_params,
            body_params,
        )
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        mw_id: str = Field("None", serialization_alias="MW-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class DeleteQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def delete(self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
    ) -> dict[str, Any]:
        """API: Delete One Maintenance Window
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/maintenance-windows-delete-one/
        Description: Delete one maintenance window with an end date in the future."""
        return self._request(
            "DELETE",
            "/groups/{PROJECT-ID}/maintenanceWindows/{MW-ID}",
            path_params,
            query_params,
            None,
        )
    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_all(self,
        path_params: GetAllPathParams,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """API: Get All Maintenance Windows
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/maintenance-windows-get-all/
        Description: Retrieve all maintenance windows with end dates in the future."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/maintenanceWindows/",
            path_params,
            query_params,
            None,
        )
    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        mw_id: str = Field("None", serialization_alias="MW-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_one(self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
    ) -> dict[str, Any]:
        """API: Get One Maintenance Window
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/maintenance-windows-get-one/
        Description: Retrieve one maintenance window with an end date in the future."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/maintenanceWindows/{MW-ID}",
            path_params,
            query_params,
            None,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        mw_id: str = Field("None", serialization_alias="MW-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        alert_type_names: list[str] = Field(serialization_alias="alertTypeNames")
        description: Optional[str] = Field("None", serialization_alias="description")
        end_date: str = Field("None", serialization_alias="endDate")
        start_date: str = Field("None", serialization_alias="startDate")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: UpdateBodyParams,
    ) -> dict[str, Any]:
        """API: Update One Maintenance Window
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/maintenance-windows-update-one/
        Description: Update one maintenance window with an end date in the future."""
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/maintenanceWindows/{MW-ID}",
            path_params,
            query_params,
            body_params,
        )