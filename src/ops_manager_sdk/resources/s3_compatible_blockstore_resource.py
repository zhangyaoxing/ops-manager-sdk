from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class S3CompatibleBlockstoreResource(BaseResource):
    """Client for S3CompatibleBlockstoreResource resource."""
    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        accepted_tos: bool = Field(serialization_alias="acceptedTos")
        assignment_enabled: Optional[bool] = Field(serialization_alias="assignmentEnabled")
        aws_access_key: Optional[str] = Field("None", serialization_alias="awsAccessKey")
        aws_secret_key: Optional[str] = Field("None", serialization_alias="awsSecretKey")
        custom_certificates: Optional[list[Any]] = Field(serialization_alias="customCertificates")
        disable_proxy_s3: Optional[bool] = Field(serialization_alias="disableProxyS3")
        encrypted_credentials: Optional[bool] = Field(serialization_alias="encryptedCredentials")
        id: str = Field("None", serialization_alias="id")
        labels: Optional[list[str]] = Field(serialization_alias="labels")
        load_factor: Optional[float] = Field(serialization_alias="loadFactor")
        object_lock_enabled: Optional[bool] = Field(serialization_alias="objectLockEnabled")
        path_style_access_enabled: bool = Field(serialization_alias="pathStyleAccessEnabled")
        s3_auth_method: Optional[str] = Field("None", serialization_alias="s3AuthMethod")
        s3_bucket_endpoint: str = Field("None", serialization_alias="s3BucketEndpoint")
        s3_bucket_name: str = Field("None", serialization_alias="s3BucketName")
        s3_max_connections: float = Field(serialization_alias="s3MaxConnections")
        s3_region_override: Optional[str] = Field("None", serialization_alias="s3RegionOverride")
        sse_enabled: bool = Field(serialization_alias="sseEnabled")
        ssl: Optional[bool] = Field(serialization_alias="ssl")
        uri: str = Field("None", serialization_alias="uri")
        write_concern: Optional[str] = Field("None", serialization_alias="writeConcern")
    def create(self,
        path_params: Optional[CreatePathParams],
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """API: Create One S3 Blockstore Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/s3Configs/create-one-s3-blockstore-configuration/
        Description: Configures one new s3 blockstore."""
        return self._request(
            "POST",
            "/snapshot/s3Configs",
            path_params,
            query_params,
            body_params,
        )
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        s3_blockstore_config_id: str = Field("None", serialization_alias="S3-BLOCKSTORE-CONFIG-ID")
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
        """API: Delete One S3-Compatible Blockstore Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/s3Configs/delete-one-s3-blockstore-configuration/
        Description: Deletes the configuration of one s3 blockstore."""
        return self._request(
            "DELETE",
            "/snapshot/s3Configs/{S3-BLOCKSTORE-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )
    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        assignable_only: Optional[bool] = Field(True, serialization_alias="assignableOnly")
    class GetAllBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all(self,
        path_params: Optional[GetAllPathParams],
        query_params: Optional[GetAllQueryParams],
        body_params: Optional[GetAllBodyParams],
    ) -> dict[str, Any]:
        """API: Get All S3 Blockstore Configurations
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/s3Configs/get-all-s3-blockstore-configurations/
        Description: Retrieves the configurations of all S3 blockstores."""
        return self._request(
            "GET",
            "/snapshot/s3Configs",
            path_params,
            query_params,
            body_params,
        )
    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        s3_blockstore_config_id: str = Field("None", serialization_alias="S3-BLOCKSTORE-CONFIG-ID")
    class GetByIdQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class GetByIdBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_by_id(self,
        path_params: GetByIdPathParams,
        query_params: Optional[GetByIdQueryParams],
        body_params: Optional[GetByIdBodyParams],
    ) -> dict[str, Any]:
        """API: Get One S3 Blockstore Configuration by ID
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/s3Configs/get-one-s3-blockstore-configuration-by-id/
        Description: Retrieves the configuration of one S3 blockstore."""
        return self._request(
            "GET",
            "/snapshot/s3Configs/{S3-BLOCKSTORE-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        s3_blockstore_config_id: str = Field("None", serialization_alias="S3-BLOCKSTORE-CONFIG-ID")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        accepted_tos: bool = Field(serialization_alias="acceptedTos")
        assignment_enabled: Optional[bool] = Field(serialization_alias="assignmentEnabled")
        aws_access_key: Optional[str] = Field("None", serialization_alias="awsAccessKey")
        aws_secret_key: Optional[str] = Field("None", serialization_alias="awsSecretKey")
        custom_certificates: Optional[list[Any]] = Field(serialization_alias="customCertificates")
        disable_proxy_s3: Optional[bool] = Field(serialization_alias="disableProxyS3")
        encrypted_credentials: Optional[bool] = Field(serialization_alias="encryptedCredentials")
        labels: Optional[list[str]] = Field(serialization_alias="labels")
        load_factor: Optional[float] = Field(serialization_alias="loadFactor")
        object_lock_enabled: Optional[bool] = Field(serialization_alias="objectLockEnabled")
        path_style_access_enabled: bool = Field(serialization_alias="pathStyleAccessEnabled")
        s3_auth_method: Optional[str] = Field("None", serialization_alias="s3AuthMethod")
        s3_bucket_endpoint: str = Field("None", serialization_alias="s3BucketEndpoint")
        s3_bucket_name: str = Field("None", serialization_alias="s3BucketName")
        s3_max_connections: float = Field(serialization_alias="s3MaxConnections")
        s3_region_override: Optional[str] = Field("None", serialization_alias="s3RegionOverride")
        sse_enabled: bool = Field(serialization_alias="sseEnabled")
        uri: str = Field("None", serialization_alias="uri")
        ssl: Optional[bool] = Field(serialization_alias="ssl")
        write_concern: Optional[str] = Field("None", serialization_alias="writeConcern")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: UpdateBodyParams,
    ) -> dict[str, Any]:
        """API: Update One S3 Blockstore Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/admin/backup/snapshot/s3Configs/update-one-s3-blockstore-configuration/
        Description: Updates the configuration of one s3 blockstore."""
        return self._request(
            "PUT",
            "/snapshot/s3Configs/{S3-BLOCKSTORE-CONFIG-ID}",
            path_params,
            query_params,
            body_params,
        )