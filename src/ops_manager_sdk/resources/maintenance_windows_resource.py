from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class MaintenanceWindowsResource(BaseResource):
    """Client for MaintenanceWindowsResource resource."""
    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        alert_type_names: list[str] = Field(serialization_alias="alertTypeNames")
        start_date: str = Field("None", serialization_alias="startDate")
        end_date: str = Field("None", serialization_alias="endDate")
        description: Optional[str] = Field("None", serialization_alias="description")
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
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        mw_id: str = Field("None", serialization_alias="MW-ID")
    class DeleteQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class DeleteBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def delete(self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
        body_params: Optional[DeleteBodyParams],
    ) -> dict[str, Any]:
        """API: Delete One Maintenance Window
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/maintenance-windows-delete-one/
        Description: Delete one maintenance window with an end date in the future."""
        return self._request(
            "DELETE",
            "/groups/{PROJECT-ID}/maintenanceWindows/{MW-ID}",
            path_params,
            query_params,
            body_params,
        )
    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class GetAllBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all(self,
        path_params: GetAllPathParams,
        query_params: Optional[GetAllQueryParams],
        body_params: Optional[GetAllBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Maintenance Windows
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/maintenance-windows-get-all/
        Description: Retrieve all maintenance windows with end dates in the future."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/maintenanceWindows/",
            path_params,
            query_params,
            body_params,
        )
    class GetOnePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        mw_id: str = Field("None", serialization_alias="MW-ID")
    class GetOneQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class GetOneBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_one(self,
        path_params: GetOnePathParams,
        query_params: Optional[GetOneQueryParams],
        body_params: Optional[GetOneBodyParams],
    ) -> dict[str, Any]:
        """API: Get One Maintenance Window
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/maintenance-windows-get-one/
        Description: Retrieve one maintenance window with an end date in the future."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/maintenanceWindows/{MW-ID}",
            path_params,
            query_params,
            body_params,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        mw_id: str = Field("None", serialization_alias="MW-ID")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        alert_type_names: list[str] = Field(serialization_alias="alertTypeNames")
        start_date: str = Field("None", serialization_alias="startDate")
        end_date: str = Field("None", serialization_alias="endDate")
        description: Optional[str] = Field("None", serialization_alias="description")
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