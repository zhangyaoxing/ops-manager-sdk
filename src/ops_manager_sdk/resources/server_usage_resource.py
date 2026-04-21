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
        age_limit: Optional[int] = Field(7, serialization_alias="ageLimit")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        limit: Optional[int] = Field(1000, serialization_alias="limit")
        minutes: Optional[int] = Field(1440, serialization_alias="minutes")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        size_limit: Optional[int] = Field(50000000, serialization_alias="sizeLimit")
    def get_diagnostic_archive(self,
        path_params: GetDiagnosticArchivePathParams,
        query_params: Optional[GetDiagnosticArchiveQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Project Diagnostic Archive
        - Document: [Get Diagnostic Archive](https://www.mongodb.com/docs/ops-manager/current/reference/api/diagnostics/get-project-diagnostic-archive/)
        - Resource: `GET /groups/{PROJECT-ID}/diagnostics`
        - Description: MongoDB engineers may request that Ops Manager administrators provide diagnostic archives for one project for debugging and troubleshooting. Project diagnostic archives also contain global system information about Ops Manager."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/diagnostics",
            path_params,
            query_params,
            None,
        )
    class CreatePhysicalHostQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    class CreatePhysicalHostBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        name: str = Field("None", serialization_alias="name")
        server_type: str = Field("None", serialization_alias="serverType")
        class VirtualhostsParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            group_id: Optional[str] = Field("None", serialization_alias="groupId")
            hostname: Optional[str] = Field("None", serialization_alias="hostname")
        virtual_hosts: list[VirtualhostsParams] = Field(serialization_alias="virtualHosts")
    def create_physical_host(self,
        query_params: Optional[CreatePhysicalHostQueryParams],
        body_params: CreatePhysicalHostBodyParams,
    ) -> dict[str, Any]:
        """
        ## Create One Physical Host
        - Document: [Create Physical Host](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/create-one-physical-host/)
        - Resource: `POST /usage/groups`
        - Description: No description."""
        return self._request(
            "POST",
            "/usage/groups",
            None,
            query_params,
            body_params,
        )
    class GetGlobalUsageReportArchiveQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        end_date: str = Field("None", serialization_alias="endDate")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        file_format: str = Field("None", serialization_alias="fileFormat")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        redact: Optional[bool] = Field(True, serialization_alias="redact")
        start_date: str = Field("None", serialization_alias="startDate")
    def get_global_usage_report_archive(self,
        query_params: GetGlobalUsageReportArchiveQueryParams,
    ) -> dict[str, Any]:
        """
        ## Get One Global Usage Report Archive
        - Document: [Get Global Usage Report Archive](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/create-one-report/)
        - Resource: `GET /usage/report`
        - Description: Retrieve a compressed report, in zip or .tar.gz format, of server usage in a given timeframe."""
        return self._request(
            "GET",
            "/usage/report",
            None,
            query_params,
            None,
        )
    class GenerateUsageSnapshotQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    def generate_usage_snapshot(self,
        query_params: Optional[GenerateUsageSnapshotQueryParams],
    ) -> dict[str, Any]:
        """
        ## Generate Daily Usage Snapshot
        - Document: [Generate Usage Snapshot](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/generate-daily-usage-snapshot/)
        - Resource: `POST /usage/dailyCapture`
        - Description: If MongoDB Usage UI is set to On, you can trigger this endpoint which tells Ops Manager to:"""
        return self._request(
            "POST",
            "/usage/dailyCapture",
            None,
            query_params,
            None,
        )
    class RetrieveAllPhysicalHostsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    def retrieve_all_physical_hosts(self,
        query_params: Optional[RetrieveAllPhysicalHostsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Retrieve All Physical Hosts
        - Document: [Retrieve All Physical Hosts](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/get-all-physical-hosts/)
        - Resource: `GET /usage/groups`
        - Description: No description."""
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
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_server_type_in_one_organization(self,
        path_params: GetServerTypeInOneOrganizationPathParams,
        query_params: Optional[GetServerTypeInOneOrganizationQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Default Server Type For One Organization
        - Document: [Get Server Type in One Organization](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/get-default-server-type-for-one-organization/)
        - Resource: `GET /usage/organizations/{orgId}/defaultServerType`
        - Description: Retrieve the default server type for one organization."""
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
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_default_server_type(self,
        path_params: GetDefaultServerTypePathParams,
        query_params: Optional[GetDefaultServerTypeQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Default Server Type For One Project
        - Document: [Get Default Server Type](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/get-default-server-type-for-one-project/)
        - Resource: `GET /usage/groups/{groupId}/defaultServerType`
        - Description: Retrieve the default server type for one project."""
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
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    def retreive_one_physical_host(self,
        path_params: RetreiveOnePhysicalHostPathParams,
        query_params: Optional[RetreiveOnePhysicalHostQueryParams],
    ) -> dict[str, Any]:
        """
        ## Retrieve One Physical Host
        - Document: [Retreive One Physical Host](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/get-one-physical-host-by-host-id/)
        - Resource: `GET /usage/groups/{physicalHostId}`
        - Description: No description."""
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
        end_date: str = Field("None", serialization_alias="endDate")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: float = Field(100.0, serialization_alias="itemsPerPage")
        page_num: float = Field(serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        start_date: str = Field("None", serialization_alias="startDate")
    def list_host_assignments_in_one_organization(self,
        path_params: ListHostAssignmentsInOneOrganizationPathParams,
        query_params: ListHostAssignmentsInOneOrganizationQueryParams,
    ) -> dict[str, Any]:
        """
        ## List All Host Assignments In One Organization
        - Document: [List Host Assignments in One Organization](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/list-all-host-assignments-in-one-organization/)
        - Resource: `GET /usage/organizations/{orgId}/hosts`
        - Description: Retrieves all host assignments for one organization."""
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
        end_date: str = Field("None", serialization_alias="endDate")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: float = Field(100.0, serialization_alias="itemsPerPage")
        page_num: float = Field(serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        start_date: str = Field("None", serialization_alias="startDate")
    def list_host_assignments_in_one_project(self,
        path_params: ListHostAssignmentsInOneProjectPathParams,
        query_params: ListHostAssignmentsInOneProjectQueryParams,
    ) -> dict[str, Any]:
        """
        ## List All Host Assignments In One Project
        - Document: [List Host Assignments in One Project](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/list-all-host-assignments-in-one-project/)
        - Resource: `GET /usage/groups/{groupId}/hosts`
        - Description: Retrieves all host assignments for one project."""
        return self._request(
            "GET",
            "/usage/groups/{groupId}/hosts",
            path_params,
            query_params,
            None,
        )
    class ListHostAssignmentsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        end_date: str = Field("None", serialization_alias="endDate")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: float = Field(100.0, serialization_alias="itemsPerPage")
        page_num: float = Field(serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        start_date: str = Field("None", serialization_alias="startDate")
    def list_host_assignments(self,
        query_params: ListHostAssignmentsQueryParams,
    ) -> dict[str, Any]:
        """
        ## List All Host Assignments
        - Document: [List Host Assignments](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/list-all-host-assignments/)
        - Resource: `GET /usage/assignments`
        - Description: Retrieves all host assignments."""
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
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    def remove_physical_host(self,
        path_params: RemovePhysicalHostPathParams,
        query_params: Optional[RemovePhysicalHostQueryParams],
    ) -> dict[str, Any]:
        """
        ## Remove One Physical Host
        - Document: [Remove Physical Host](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/remove-one-physical-host/)
        - Resource: `DELETE /usage/groups/{physicalHostId}`
        - Description: No description."""
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
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class UpdateServerTypeForOneOrganizationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        class ServertypeParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            label: Optional[dict] = Field(serialization_alias="label")
            name: dict = Field(serialization_alias="name")
        server_type: ServertypeParams = Field(serialization_alias="serverType")
    def update_server_type_for_one_organization(self,
        path_params: UpdateServerTypeForOneOrganizationPathParams,
        query_params: Optional[UpdateServerTypeForOneOrganizationQueryParams],
        body_params: UpdateServerTypeForOneOrganizationBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update Default Server Type For One Organization
        - Document: [Update Server Type for One Organization](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/update-default-server-type-for-one-organization/)
        - Resource: `PUT /usage/organizations/{orgId}/defaultServerType`
        - Description: Update the default server type for one organization."""
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
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class UpdateDefaultServerTypeBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        class ServertypeParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            label: Optional[dict] = Field(serialization_alias="label")
            name: dict = Field(serialization_alias="name")
        server_type: ServertypeParams = Field(serialization_alias="serverType")
    def update_default_server_type(self,
        path_params: UpdateDefaultServerTypePathParams,
        query_params: Optional[UpdateDefaultServerTypeQueryParams],
        body_params: UpdateDefaultServerTypeBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update Default Server Type For One Project
        - Document: [Update Default Server Type](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/update-default-server-type-for-one-project/)
        - Resource: `PUT /usage/groups/{groupId}/defaultServerType`
        - Description: Update the default server type for one project."""
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
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    class UpdatePhysicalHostBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        name: str = Field("None", serialization_alias="name")
        server_type: str = Field("None", serialization_alias="serverType")
        class VirtualhostsParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            group_id: Optional[str] = Field("None", serialization_alias="groupId")
            hostname: Optional[str] = Field("None", serialization_alias="hostname")
        virtual_hosts: list[VirtualhostsParams] = Field(serialization_alias="virtualHosts")
    def update_physical_host(self,
        path_params: UpdatePhysicalHostPathParams,
        query_params: Optional[UpdatePhysicalHostQueryParams],
        body_params: UpdatePhysicalHostBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update One Physical Host
        - Document: [Update Physical Host](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/update-one-physical-host/)
        - Resource: `PUT /usage/groups/{physicalHostId}`
        - Description: No description."""
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
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class UpdateServerTypeBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        class ServertypeParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            label: Optional[dict] = Field(serialization_alias="label")
            name: dict = Field(serialization_alias="name")
        server_type: ServertypeParams = Field(serialization_alias="serverType")
    def update_server_type(self,
        path_params: UpdateServerTypePathParams,
        query_params: Optional[UpdateServerTypeQueryParams],
        body_params: UpdateServerTypeBodyParams,
    ) -> dict[str, Any]:
        """
        ## Update Server Type for One Host
        - Document: [Update Server Type](https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/update-server-type-for-one-host/)
        - Resource: `PUT /usage/hosts/{hostId}`
        - Description: Update one default server type for one host."""
        return self._request(
            "PUT",
            "/usage/hosts/{hostId}",
            path_params,
            query_params,
            body_params,
        )