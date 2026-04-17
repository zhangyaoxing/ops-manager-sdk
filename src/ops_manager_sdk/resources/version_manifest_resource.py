from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class VersionManifestResource(BaseResource):
    """Client for VersionManifestResource resource."""
    class RetrievePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class RetrieveQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(alias="pretty")
    class RetrieveBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def retrieve(self,
        path_params: Optional[RetrievePathParams],
        query_params: Optional[RetrieveQueryParams],
        body_params: Optional[RetrieveBodyParams],
    ) -> dict[str, Any]:
        """API: Retrieve the Ops Manager Version Manifest
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/version-manifest/get-om-version-manifest/
        Description: Use this resource to retrieve the version manifest that Ops Manager is configured to use."""
        return self._request(
            "GET",
            "/unauth/versionManifest",
            path_params,
            query_params,
            body_params,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(alias="pretty")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def update(self,
        path_params: Optional[UpdatePathParams],
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """API: Update the Version Manifest
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/version-manifest/update-version-manifest/
        Description: Use this resource to upload the latest version manifest from MongoDB, Inc."""
        return self._request(
            "PUT",
            "/versionManifest",
            path_params,
            query_params,
            body_params,
        )