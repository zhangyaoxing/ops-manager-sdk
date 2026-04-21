from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class HostsResource(BaseResource):
    """Client for HostsResource resource."""
    class BeginMonitoringPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class BeginMonitoringQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class BeginMonitoringBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        alerts_enabled: Optional[bool] = Field(serialization_alias="alertsEnabled")
        auth_mechanism_name: Optional[str] = Field("None", serialization_alias="authMechanismName")
        hostname: str = Field("None", serialization_alias="hostname")
        logs_enabled: Optional[bool] = Field(serialization_alias="logsEnabled")
        password: Optional[str] = Field("None", serialization_alias="password")
        port: float = Field(serialization_alias="port")
        profiler_enabled: Optional[bool] = Field(serialization_alias="profilerEnabled")
        ssl_enabled: Optional[bool] = Field(serialization_alias="sslEnabled")
        username: Optional[str] = Field("None", serialization_alias="username")
    def begin_monitoring(self,
        path_params: BeginMonitoringPathParams,
        query_params: Optional[BeginMonitoringQueryParams],
        body_params: BeginMonitoringBodyParams,
    ) -> dict[str, Any]:
        """
        ## Begin Monitoring One Host
        - Document: [Begin Monitoring](https://www.mongodb.com/docs/ops-manager/current/reference/api/hosts/create-one-host/)
        - Resource: `POST /groups/{PROJECT-ID}/hosts`
        - Description: Start monitoring a new MongoDB process. The Monitoring starts monitoring the MongoDB process on the hostname and port you specify. Ops Manager knows only the information that you provide. The response document includes blank values until Ops Manager completes discovery of the MongoDB processes configuration."""
        return self._request(
            "POST",
            "/groups/{PROJECT-ID}/hosts",
            path_params,
            query_params,
            body_params,
        )
    class StopMonitoringPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        host_id: str = Field("None", serialization_alias="HOST-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class StopMonitoringQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def stop_monitoring(self,
        path_params: StopMonitoringPathParams,
        query_params: Optional[StopMonitoringQueryParams],
    ) -> dict[str, Any]:
        """
        ## Stop Monitoring One Host
        - Document: [Stop Monitoring](https://www.mongodb.com/docs/ops-manager/current/reference/api/hosts/delete-one-host/)
        - Resource: `DELETE /groups/{PROJECT-ID}/hosts/{HOST-ID}`
        - Description: Stops the Monitoring from monitoring the MongoDB process on the hostname and port you specify."""
        return self._request(
            "DELETE",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}",
            path_params,
            query_params,
            None,
        )
    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        cluster_id: str = Field("None", serialization_alias="clusterId")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_all(self,
        path_params: GetAllPathParams,
        query_params: GetAllQueryParams,
    ) -> dict[str, Any]:
        """
        ## Get All Hosts in One Project
        - Document: [Get All](https://www.mongodb.com/docs/ops-manager/current/reference/api/hosts/get-all-hosts-in-group/)
        - Resource: `GET /groups/{PROJECT-ID}/hosts`
        - Description: Get all MongoDB hosts in a project. Use the CLUSTER-ID query parameter to only get the hosts that belong to the specified cluster. The response sorts the hosts alphabetically by HOSTNAME:PORT."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts",
            path_params,
            query_params,
            None,
        )
    class GetByHostnamePortPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        hostname: str = Field("None", serialization_alias="HOSTNAME")
        port: str = Field("None", serialization_alias="PORT")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetByHostnamePortQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_by_hostname_port(self,
        path_params: GetByHostnamePortPathParams,
        query_params: Optional[GetByHostnamePortQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get One Host by Hostname and Port
        - Document: [Get by Hostname & Port](https://www.mongodb.com/docs/ops-manager/current/reference/api/hosts/get-one-host-by-hostname-port/)
        - Resource: `GET /groups/{PROJECT-ID}/hosts/byName/{HOSTNAME}:{PORT}`
        - Description: Get a single MongoDB process by its hostname and port combination. You can specify either the primary hostname or an alias."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/byName/{HOSTNAME}:{PORT}",
            path_params,
            query_params,
            None,
        )
    class GetByIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        host_id: str = Field("None", serialization_alias="HOST-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetByIdQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_by_id(self,
        path_params: GetByIdPathParams,
        query_params: Optional[GetByIdQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Host by ID
        - Document: [Get by ID](https://www.mongodb.com/docs/ops-manager/current/reference/api/hosts/get-one-host-by-id/)
        - Resource: `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}`
        - Description: Get the MongoDB process with the specified host ID."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}",
            path_params,
            query_params,
            None,
        )
    class UpdateConfigurationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        host_id: str = Field("None", serialization_alias="HOST-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class UpdateConfigurationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class UpdateConfigurationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        alerts_enabled: Optional[bool] = Field(serialization_alias="alertsEnabled")
        auth_mechanism_name: Optional[str] = Field("None", serialization_alias="authMechanismName")
        logs_enabled: Optional[bool] = Field(serialization_alias="logsEnabled")
        password: Optional[str] = Field("None", serialization_alias="password")
        profiler_enabled: Optional[bool] = Field(serialization_alias="profilerEnabled")
        ssl_enabled: Optional[bool] = Field(serialization_alias="sslEnabled")
        username: Optional[str] = Field("None", serialization_alias="username")
    def update_configuration(self,
        path_params: UpdateConfigurationPathParams,
        query_params: Optional[UpdateConfigurationQueryParams],
        body_params: Optional[UpdateConfigurationBodyParams],
    ) -> dict[str, Any]:
        """
        ## Update Configuration of One Monitored Host
        - Document: [Update Configuration](https://www.mongodb.com/docs/ops-manager/current/reference/api/hosts/update-one-host/)
        - Resource: `PATCH /groups/{PROJECT-ID}/hosts/{HOST-ID}`
        - Description: Update the configuration of a monitored MongoDB process."""
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}",
            path_params,
            query_params,
            body_params,
        )