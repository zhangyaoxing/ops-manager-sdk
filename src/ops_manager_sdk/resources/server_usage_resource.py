from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class ServerUsageResource(BaseResource):
    """Client for ServerUsageResource resource."""
    class GetDiagnosticArchivePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetDiagnosticArchiveQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        age_limit: Optional[int] = Field(7, serialization_alias="ageLimit")
        limit: Optional[int] = Field(1000, serialization_alias="limit")
        minutes: Optional[int] = Field(1440, serialization_alias="minutes")
        size_limit: Optional[int] = Field(50000000, serialization_alias="sizeLimit")
    def get_diagnostic_archive(self,
        path_params: GetDiagnosticArchivePathParams,
        query_params: Optional[GetDiagnosticArchiveQueryParams],
    ) -> dict[str, Any]:
        """API: Get One Project Diagnostic Archive
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/diagnostics/get-project-diagnostic-archive/
        Description: MongoDB engineers may request that Ops Manager administrators provide diagnostic archives for one project for debugging and troubleshooting. Project diagnostic archives also contain global system information about Ops Manager."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/diagnostics",
            path_params,
            query_params,
            None,
        )
    class CreatePhysicalHostQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
    class CreatePhysicalHostBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        virtual_hosts: list[str] = Field(serialization_alias="virtualHosts")
        name: str = Field("None", serialization_alias="name")
        server_type: str = Field("None", serialization_alias="serverType")
    def create_physical_host(self,
        query_params: Optional[CreatePhysicalHostQueryParams],
        body_params: CreatePhysicalHostBodyParams,
    ) -> dict[str, Any]:
        """API: Create One Physical Host
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/create-one-physical-host/
        Description: No description."""
        return self._request(
            "POST",
            "/usage/groups",
            None,
            query_params,
            body_params,
        )
    class GetGlobalUsageReportArchiveQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        start_date: str = Field("None", serialization_alias="startDate")
        end_date: str = Field("None", serialization_alias="endDate")
        file_format: str = Field("None", serialization_alias="fileFormat")
        redact: Optional[bool] = Field(True, serialization_alias="redact")
    def get_global_usage_report_archive(self,
        query_params: GetGlobalUsageReportArchiveQueryParams,
    ) -> dict[str, Any]:
        """API: Get One Global Usage Report Archive
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/create-one-report/
        Description: Retrieve a compressed report, in zip or .tar.gz format, of server usage in a given timeframe."""
        return self._request(
            "GET",
            "/usage/report",
            None,
            query_params,
            None,
        )
    class GenerateUsageSnapshotQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
    def generate_usage_snapshot(self,
        query_params: Optional[GenerateUsageSnapshotQueryParams],
    ) -> dict[str, Any]:
        """API: Generate Daily Usage Snapshot
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/generate-daily-usage-snapshot/
        Description: If MongoDB Usage UI is set to On, you can trigger this endpoint which tells Ops Manager to:"""
        return self._request(
            "POST",
            "/usage/dailyCapture",
            None,
            query_params,
            None,
        )
    class RetrieveAllPhysicalHostsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
    def retrieve_all_physical_hosts(self,
        query_params: Optional[RetrieveAllPhysicalHostsQueryParams],
    ) -> dict[str, Any]:
        """API: Retrieve All Physical Hosts
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/get-all-physical-hosts/
        Description: No description."""
        return self._request(
            "GET",
            "/usage/groups",
            None,
            query_params,
            None,
        )
    class GetServerTypeInOneOrganizationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="orgId")
    class GetServerTypeInOneOrganizationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_server_type_in_one_organization(self,
        path_params: GetServerTypeInOneOrganizationPathParams,
        query_params: Optional[GetServerTypeInOneOrganizationQueryParams],
    ) -> dict[str, Any]:
        """API: Get Default Server Type For One Organization
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/get-default-server-type-for-one-organization/
        Description: Retrieve the default server type for one organization."""
        return self._request(
            "GET",
            "/usage/organizations/{orgId}/defaultServerType",
            path_params,
            query_params,
            None,
        )
    class GetDefaultServerTypePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="groupId")
    class GetDefaultServerTypeQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_default_server_type(self,
        path_params: GetDefaultServerTypePathParams,
        query_params: Optional[GetDefaultServerTypeQueryParams],
    ) -> dict[str, Any]:
        """API: Get Default Server Type For One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/get-default-server-type-for-one-project/
        Description: Retrieve the default server type for one project."""
        return self._request(
            "GET",
            "/usage/groups/{groupId}/defaultServerType",
            path_params,
            query_params,
            None,
        )
    class RetreiveOnePhysicalHostPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        physical_host_id: str = Field("None", serialization_alias="physicalHostId")
    class RetreiveOnePhysicalHostQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
    def retreive_one_physical_host(self,
        path_params: RetreiveOnePhysicalHostPathParams,
        query_params: Optional[RetreiveOnePhysicalHostQueryParams],
    ) -> dict[str, Any]:
        """API: Retrieve One Physical Host
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/get-one-physical-host-by-host-id/
        Description: No description."""
        return self._request(
            "GET",
            "/usage/groups/{physicalHostId}",
            path_params,
            query_params,
            None,
        )
    class ListHostAssignmentsInOneOrganizationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="orgId")
    class ListHostAssignmentsInOneOrganizationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        start_date: str = Field("None", serialization_alias="startDate")
        end_date: str = Field("None", serialization_alias="endDate")
        page_num: float = Field(serialization_alias="pageNum")
        items_per_page: float = Field(100.0, serialization_alias="itemsPerPage")
    def list_host_assignments_in_one_organization(self,
        path_params: ListHostAssignmentsInOneOrganizationPathParams,
        query_params: ListHostAssignmentsInOneOrganizationQueryParams,
    ) -> dict[str, Any]:
        """API: List All Host Assignments In One Organization
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/list-all-host-assignments-in-one-organization/
        Description: Retrieves all host assignments for one organization."""
        return self._request(
            "GET",
            "/usage/organizations/{orgId}/hosts",
            path_params,
            query_params,
            None,
        )
    class ListHostAssignmentsInOneProjectPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="groupId")
    class ListHostAssignmentsInOneProjectQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        start_date: str = Field("None", serialization_alias="startDate")
        end_date: str = Field("None", serialization_alias="endDate")
        page_num: float = Field(serialization_alias="pageNum")
        items_per_page: float = Field(100.0, serialization_alias="itemsPerPage")
    def list_host_assignments_in_one_project(self,
        path_params: ListHostAssignmentsInOneProjectPathParams,
        query_params: ListHostAssignmentsInOneProjectQueryParams,
    ) -> dict[str, Any]:
        """API: List All Host Assignments In One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/list-all-host-assignments-in-one-project/
        Description: Retrieves all host assignments for one project."""
        return self._request(
            "GET",
            "/usage/groups/{groupId}/hosts",
            path_params,
            query_params,
            None,
        )
    class ListHostAssignmentsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        start_date: str = Field("None", serialization_alias="startDate")
        end_date: str = Field("None", serialization_alias="endDate")
        page_num: float = Field(serialization_alias="pageNum")
        items_per_page: float = Field(100.0, serialization_alias="itemsPerPage")
    def list_host_assignments(self,
        query_params: ListHostAssignmentsQueryParams,
    ) -> dict[str, Any]:
        """API: List All Host Assignments
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/list-all-host-assignments/
        Description: Retrieves all host assignments."""
        return self._request(
            "GET",
            "/usage/assignments",
            None,
            query_params,
            None,
        )
    class RemovePhysicalHostPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        physical_host_id: str = Field("None", serialization_alias="physicalHostId")
    class RemovePhysicalHostQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
    def remove_physical_host(self,
        path_params: RemovePhysicalHostPathParams,
        query_params: Optional[RemovePhysicalHostQueryParams],
    ) -> dict[str, Any]:
        """API: Remove One Physical Host
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/remove-one-physical-host/
        Description: No description."""
        return self._request(
            "DELETE",
            "/usage/groups/{physicalHostId}",
            path_params,
            query_params,
            None,
        )
    class UpdateServerTypeForOneOrganizationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        org_id: str = Field("None", serialization_alias="orgId")
    class UpdateServerTypeForOneOrganizationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class UpdateServerTypeForOneOrganizationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        server_type: dict = Field(serialization_alias="serverType")
    def update_server_type_for_one_organization(self,
        path_params: UpdateServerTypeForOneOrganizationPathParams,
        query_params: Optional[UpdateServerTypeForOneOrganizationQueryParams],
        body_params: UpdateServerTypeForOneOrganizationBodyParams,
    ) -> dict[str, Any]:
        """API: Update Default Server Type For One Organization
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/update-default-server-type-for-one-organization/
        Description: Update the default server type for one organization."""
        return self._request(
            "PUT",
            "/usage/organizations/{orgId}/defaultServerType",
            path_params,
            query_params,
            body_params,
        )
    class UpdateDefaultServerTypePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="groupId")
    class UpdateDefaultServerTypeQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class UpdateDefaultServerTypeBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        server_type: dict = Field(serialization_alias="serverType")
    def update_default_server_type(self,
        path_params: UpdateDefaultServerTypePathParams,
        query_params: Optional[UpdateDefaultServerTypeQueryParams],
        body_params: UpdateDefaultServerTypeBodyParams,
    ) -> dict[str, Any]:
        """API: Update Default Server Type For One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/update-default-server-type-for-one-project/
        Description: Update the default server type for one project."""
        return self._request(
            "PUT",
            "/usage/groups/{groupId}/defaultServerType",
            path_params,
            query_params,
            body_params,
        )
    class UpdatePhysicalHostPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        physical_host_id: str = Field("None", serialization_alias="physicalHostId")
    class UpdatePhysicalHostQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
    class UpdatePhysicalHostBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        virtual_hosts: list[str] = Field(serialization_alias="virtualHosts")
        name: str = Field("None", serialization_alias="name")
        server_type: str = Field("None", serialization_alias="serverType")
    def update_physical_host(self,
        path_params: UpdatePhysicalHostPathParams,
        query_params: Optional[UpdatePhysicalHostQueryParams],
        body_params: UpdatePhysicalHostBodyParams,
    ) -> dict[str, Any]:
        """API: Update One Physical Host
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/update-one-physical-host/
        Description: No description."""
        return self._request(
            "PUT",
            "/usage/groups/{physicalHostId}",
            path_params,
            query_params,
            body_params,
        )
    class UpdateServerTypePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        host_id: str = Field("None", serialization_alias="hostId")
    class UpdateServerTypeQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class UpdateServerTypeBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        server_type: dict = Field(serialization_alias="serverType")
    def update_server_type(self,
        path_params: UpdateServerTypePathParams,
        query_params: Optional[UpdateServerTypeQueryParams],
        body_params: UpdateServerTypeBodyParams,
    ) -> dict[str, Any]:
        """API: Update Server Type for One Host
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/update-server-type-for-one-host/
        Description: Update one default server type for one host."""
        return self._request(
            "PUT",
            "/usage/hosts/{hostId}",
            path_params,
            query_params,
            body_params,
        )