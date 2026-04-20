from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class ImportDeploymentsResource(BaseResource):
    """Client for ImportDeploymentsResource resource."""
    class CancelImportDeploymentRequestPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        request_id: str = Field("None", serialization_alias="REQUEST-ID")
    class CancelImportDeploymentRequestQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def cancel_import_deployment_request(self,
        path_params: CancelImportDeploymentRequestPathParams,
        query_params: Optional[CancelImportDeploymentRequestQueryParams],
    ) -> dict[str, Any]:
        """API: Cancel Import Deployment Request
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/import-deployments/cancel/
        Description: Cancel an in-progress import deployment request. This endpoint allows you to stop an import deployment request that is currently running. Once cancelled, the import process will stop and the request state will change to CANCELLED."""
        return self._request(
            "POST",
            "/automation/importDeployment/{PROJECT-ID}/{REQUEST-ID}/cancel",
            path_params,
            query_params,
            None,
        )
    class CreateImportDeploymentRequestPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class CreateImportDeploymentRequestQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class CreateImportDeploymentRequestBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        seed_hostport: str = Field("None", serialization_alias="seedHostport")
        required_processes: list[Any] = Field(serialization_alias="requiredProcesses")
        timeouts: Optional[dict] = Field(serialization_alias="timeouts")
        auth_mechanism: Optional[str] = Field("None", serialization_alias="authMechanism")
        username: Optional[str] = Field("None", serialization_alias="username")
        password: Optional[str] = Field("None", serialization_alias="password")
        admin_db: Optional[str] = Field("None", serialization_alias="adminDb")
        pem_key_file_path: Optional[str] = Field("None", serialization_alias="pemKeyFilePath")
        pem_key_file_password: Optional[str] = Field("None", serialization_alias="pemKeyFilePassword")
        admin_kerberos_keytab: Optional[str] = Field("None", serialization_alias="adminKerberosKeytab")
        admin_ldap_group_dn: Optional[str] = Field("None", serialization_alias="adminLdapGroupDn")
        sasl_service_name: Optional[str] = Field("None", serialization_alias="saslServiceName")
        ca_file_path: Optional[str] = Field("None", serialization_alias="caFilePath")
        cluster_ca_file_path: Optional[str] = Field("None", serialization_alias="clusterCaFilePath")
        client_certificate_mode: Optional[str] = Field("None", serialization_alias="clientCertificateMode")
    def create_import_deployment_request(self,
        path_params: CreateImportDeploymentRequestPathParams,
        query_params: Optional[CreateImportDeploymentRequestQueryParams],
        body_params: CreateImportDeploymentRequestBodyParams,
    ) -> dict[str, Any]:
        """API: Create Import Deployment Request
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/import-deployments/create/
        Description: Create a new import deployment request to add existing MongoDB processes to Ops Manager automation. This endpoint initiates the process of importing multiple MongoDB processes into both monitoring and automation management."""
        return self._request(
            "POST",
            "/automation/importDeployment/{PROJECT-ID}",
            path_params,
            query_params,
            body_params,
        )
    class DeleteImportDeploymentRequestPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        request_id: str = Field("None", serialization_alias="REQUEST-ID")
    class DeleteImportDeploymentRequestQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def delete_import_deployment_request(self,
        path_params: DeleteImportDeploymentRequestPathParams,
        query_params: Optional[DeleteImportDeploymentRequestQueryParams],
    ) -> dict[str, Any]:
        """API: Delete Import Deployment Request
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/import-deployments/delete/
        Description: Delete a failed import deployment request and clean up any partially imported resources. This endpoint removes the import deployment request record and performs cleanup of any resources that were partially imported during the failed import process."""
        return self._request(
            "DELETE",
            "/automation/importDeployment/{PROJECT-ID}/{REQUEST-ID}",
            path_params,
            query_params,
            None,
        )
    class GetImportDeploymentRequestsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetImportDeploymentRequestsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_import_deployment_requests(self,
        path_params: GetImportDeploymentRequestsPathParams,
        query_params: Optional[GetImportDeploymentRequestsQueryParams],
    ) -> dict[str, Any]:
        """API: Get Import Deployment Requests
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/import-deployments/get-all/
        Description: Retrieve all import deployment requests for a project. This endpoint returns a list of all import deployment requests that have been created for the specified project, including their current status and history."""
        return self._request(
            "GET",
            "/automation/importDeployment/{PROJECT-ID}",
            path_params,
            query_params,
            None,
        )
    class GetImportDeploymentRequestStatusPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        import_process_id: str = Field("None", serialization_alias="IMPORT-PROCESS-ID")
    class GetImportDeploymentRequestStatusQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_import_deployment_request_status(self,
        path_params: GetImportDeploymentRequestStatusPathParams,
        query_params: Optional[GetImportDeploymentRequestStatusQueryParams],
    ) -> dict[str, Any]:
        """API: Get Import Deployment Request Status
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/import-deployments/get-status/
        Description: Retrieve the status of a specific import deployment request. This endpoint provides detailed information about the current state and history of a single import deployment request."""
        return self._request(
            "GET",
            "/automation/importDeployment/{PROJECT-ID}/{IMPORT-PROCESS-ID}",
            path_params,
            query_params,
            None,
        )