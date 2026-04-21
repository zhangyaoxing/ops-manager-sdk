from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class MigrateToMongodbAtlasResource(BaseResource):
    """Client for MigrateToMongodbAtlasResource resource."""
    class ConnectWithAtlasOrganizationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="orgId")
    class ConnectWithAtlasOrganizationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class ConnectWithAtlasOrganizationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        link_token: str = Field("None", serialization_alias="linkToken")
    def connect_with_atlas_organization(self,
        path_params: ConnectWithAtlasOrganizationPathParams,
        query_params: Optional[ConnectWithAtlasOrganizationQueryParams],
        body_params: ConnectWithAtlasOrganizationBodyParams,
    ) -> dict[str, Any]:
        """API: Connect One Organization with One Atlas Organization
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/cloud-migration/link-the-organization-with-atlas/
        Description: Connect the source Ops Manager organization with a target MongoDB Atlas organization."""
        return self._request(
            "POST",
            "/orgs/{orgId}/liveExport/migrationLink",
            path_params,
            query_params,
            body_params,
        )
    class RemoveConnectionPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="orgId")
    class RemoveConnectionQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def remove_connection(self,
        path_params: RemoveConnectionPathParams,
        query_params: Optional[RemoveConnectionQueryParams],
    ) -> dict[str, Any]:
        """API: Remove the Connection between Organizations
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/cloud-migration/remove-the-link-between-organizations/
        Description: Remove the connection between the source Ops Manager organization and the target MongoDB Atlas organization. This stops the source organization from synchronizing data with the target organization."""
        return self._request(
            "DELETE",
            "/orgs/{orgId}/liveExport/migrationLink",
            path_params,
            query_params,
            None,
        )
    class ReturnConnectionStatusPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="orgId")
    class ReturnConnectionStatusQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def return_connection_status(self,
        path_params: ReturnConnectionStatusPathParams,
        query_params: Optional[ReturnConnectionStatusQueryParams],
    ) -> dict[str, Any]:
        """API: Return the Status of the Connection between Organizations
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/cloud-migration/return-the-status-of-the-organization-link/
        Description: Return the status of the connection between the specified source Ops Manager organization and the target MongoDB Atlas organization."""
        return self._request(
            "GET",
            "/orgs/{orgId}/liveExport/migrationLink/status",
            path_params,
            query_params,
            None,
        )