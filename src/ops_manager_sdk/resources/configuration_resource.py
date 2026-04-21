from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class ConfigurationResource(BaseResource):
    """Client for ConfigurationResource resource."""
    class GetTheAuditLogRotateConfigurationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetTheAuditLogRotateConfigurationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_the_audit_log_rotate_configuration(self,
        path_params: GetTheAuditLogRotateConfigurationPathParams,
        query_params: Optional[GetTheAuditLogRotateConfigurationQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get the Audit Log Rotate Configuration
        - Document: [Get the Audit Log Rotate Configuration](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/get-audit-log-rotate-config/)
        - Resource: `GET /groups/{PROJECT-ID}/automationConfig/auditLogRotateConfig`
        - Description: This endpoint returns the current audit log rotation configuration."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/automationConfig/auditLogRotateConfig",
            path_params,
            query_params,
            None,
        )
    class GetTheAutomationConfigurationNoSecretsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetTheAutomationConfigurationNoSecretsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_the_automation_configuration_no_secrets_(self,
        path_params: GetTheAutomationConfigurationNoSecretsPathParams,
        query_params: Optional[GetTheAutomationConfigurationNoSecretsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get the Automation Configuration (Redacted Secrets)
        - Document: [Get the Automation Configuration (No Secrets)](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/get-automation-config-no-secrets/)
        - Resource: `GET /groups/{PROJECT-ID}/automationConfig/noSecrets`
        - Description: A project's automation configuration determines the goal state of its MongoDB processes and agents. The MongoDB Agent builds the deployment according to the goals specified."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/automationConfig/noSecrets",
            path_params,
            query_params,
            None,
        )
    class GetTheAutomationConfigurationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetTheAutomationConfigurationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_the_automation_configuration(self,
        path_params: GetTheAutomationConfigurationPathParams,
        query_params: Optional[GetTheAutomationConfigurationQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get the Automation Configuration
        - Document: [Get the Automation Configuration](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/get-automation-config/)
        - Resource: `GET /groups/{PROJECT-ID}/automationConfig`
        - Description: A project's automation configuration determines the goal state of its MongoDB processes and agents. The MongoDB Agent builds the deployment according to the goals specified."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/automationConfig",
            path_params,
            query_params,
            None,
        )
    class GetBackupConfigurationSettingsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetBackupConfigurationSettingsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_backup_configuration_settings(self,
        path_params: GetBackupConfigurationSettingsPathParams,
        query_params: Optional[GetBackupConfigurationSettingsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Backup Configuration Settings
        - Document: [Get Backup Configuration Settings](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/get-backup-log-attributes/)
        - Resource: `GET /groups/{PROJECT-ID}/automationConfig/backupAgentConfig`
        - Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/automationConfig/backupAgentConfig",
            path_params,
            query_params,
            None,
        )
    class GetMonitoringConfigurationSettingsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetMonitoringConfigurationSettingsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_monitoring_configuration_settings(self,
        path_params: GetMonitoringConfigurationSettingsPathParams,
        query_params: Optional[GetMonitoringConfigurationSettingsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Monitoring Configuration Settings
        - Document: [Get Monitoring Configuration Settings](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/get-monitoring-log-attributes/)
        - Resource: `GET /groups/{PROJECT-ID}/automationConfig/monitoringAgentConfig`
        - Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/automationConfig/monitoringAgentConfig",
            path_params,
            query_params,
            None,
        )
    class GetTheSystemLogRotateConfigurationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetTheSystemLogRotateConfigurationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_the_system_log_rotate_configuration(self,
        path_params: GetTheSystemLogRotateConfigurationPathParams,
        query_params: Optional[GetTheSystemLogRotateConfigurationQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get the System Log Rotate Configuration
        - Document: [Get the System Log Rotate Configuration](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/get-system-log-rotate-config/)
        - Resource: `GET /groups/{PROJECT-ID}/automationConfig/systemLogRotateConfig`
        - Description: This endpoint returns the current system log rotation configuration."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/automationConfig/systemLogRotateConfig",
            path_params,
            query_params,
            None,
        )
    class UpdateAgentVersionsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class UpdateAgentVersionsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class UpdateAgentVersionsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        automation_agent_version: Optional[str] = Field("None", serialization_alias="automationAgentVersion")
        bi_connector_version: Optional[str] = Field("None", serialization_alias="biConnectorVersion")
        mongo_db_tools_version: Optional[str] = Field("None", serialization_alias="mongoDbToolsVersion")
    def update_agent_versions(self,
        path_params: UpdateAgentVersionsPathParams,
        query_params: Optional[UpdateAgentVersionsQueryParams],
        body_params: Optional[UpdateAgentVersionsBodyParams],
    ) -> dict[str, Any]:
        """
        ## Update Agent Versions
        - Document: [Update Agent Versions](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/update-agent-versions/)
        - Resource: `POST /groups/{PROJECT-ID}/automationConfig/updateAgentVersions`
        - Description: This endpoint updates the MongoDB Agent and tools to the latest versions available at the time of the request:"""
        return self._request(
            "POST",
            "/groups/{PROJECT-ID}/automationConfig/updateAgentVersions",
            path_params,
            query_params,
            body_params,
        )
    class UpdateTheAuditLogRotateConfigPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class UpdateTheAuditLogRotateConfigQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class UpdateTheAuditLogRotateConfigBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        num_total: Optional[Any] = Field(serialization_alias="numTotal")
        num_uncompressed: Optional[Any] = Field(serialization_alias="numUncompressed")
        percent_of_diskspace: Optional[Any] = Field(serialization_alias="percentOfDiskspace")
        size_threshold_mb: Optional[Any] = Field(serialization_alias="sizeThresholdMB")
        time_threshold_hrs: Optional[Any] = Field(serialization_alias="timeThresholdHrs")
    def update_the_audit_log_rotate_config(self,
        path_params: UpdateTheAuditLogRotateConfigPathParams,
        query_params: Optional[UpdateTheAuditLogRotateConfigQueryParams],
        body_params: Optional[UpdateTheAuditLogRotateConfigBodyParams],
    ) -> dict[str, Any]:
        """
        ## Update the Audit Log Rotate Config
        - Document: [Update the Audit Log Rotate Config](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/update-audit-log-rotate-config/)
        - Resource: `PUT /groups/{PROJECT-ID}/automationConfig/auditLogRotateConfig`
        - Description: This endpoint updates the MongoDB Agent audit log rotation configuration. After this request completes, Ops Manager modifies the agent configuration and saves the updated version."""
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}/automationConfig/auditLogRotateConfig",
            path_params,
            query_params,
            body_params,
        )
    class UpdateTheAutomationConfigurationNoSecretsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class UpdateTheAutomationConfigurationNoSecretsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def update_the_automation_configuration_no_secrets_(self,
        path_params: UpdateTheAutomationConfigurationNoSecretsPathParams,
        query_params: Optional[UpdateTheAutomationConfigurationNoSecretsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Update the Automation Configuration (Sensitive Information Ignored)
        - Document: [Update the Automation Configuration (No Secrets)](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/update-automation-config-no-secrets/)
        - Resource: `PUT /groups/{PROJECT-ID}/automationConfig/noSecrets`
        - Description: A project's automation configuration determines the goal state of its MongoDB processes and agents. The MongoDB Agent builds the deployment according to the goals specified."""
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}/automationConfig/noSecrets",
            path_params,
            query_params,
            None,
        )
    class UpdateTheAutomationConfigurationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class UpdateTheAutomationConfigurationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def update_the_automation_configuration(self,
        path_params: UpdateTheAutomationConfigurationPathParams,
        query_params: Optional[UpdateTheAutomationConfigurationQueryParams],
    ) -> dict[str, Any]:
        """
        ## Update the Automation Configuration
        - Document: [Update the Automation Configuration](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/update-automation-config/)
        - Resource: `PUT /groups/{PROJECT-ID}/automationConfig`
        - Description: A project's automation configuration determines the goal state of its MongoDB processes and agents. The MongoDB Agent builds the deployment according to the goals specified."""
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}/automationConfig",
            path_params,
            query_params,
            None,
        )
    class UpdateBackupConfigurationSettingsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class UpdateBackupConfigurationSettingsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class UpdateBackupConfigurationSettingsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        config_overrides: Optional[dict] = Field(serialization_alias="configOverrides")
        log_path: Optional[str] = Field("None", serialization_alias="logPath")
        class LogrotateParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            size_threshold_mb: Optional[int] = Field(serialization_alias="sizeThresholdMB")
            time_duration_hrs: Optional[int] = Field(serialization_alias="timeDurationHrs")
        log_rotate: Optional[LogrotateParams] = Field(serialization_alias="logRotate")
        username: Optional[str] = Field("None", serialization_alias="username")
    def update_backup_configuration_settings(self,
        path_params: UpdateBackupConfigurationSettingsPathParams,
        query_params: Optional[UpdateBackupConfigurationSettingsQueryParams],
        body_params: Optional[UpdateBackupConfigurationSettingsBodyParams],
    ) -> dict[str, Any]:
        """
        ## Update Backup Configuration Settings
        - Document: [Update Backup Configuration Settings](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/update-backup-log-attributes/)
        - Resource: `PUT /groups/{PROJECT-ID}/automationConfig/backupAgentConfig`
        - Description: No description."""
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}/automationConfig/backupAgentConfig",
            path_params,
            query_params,
            body_params,
        )
    class UpdateMonitoringConfigurationSettingsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class UpdateMonitoringConfigurationSettingsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class UpdateMonitoringConfigurationSettingsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        config_overrides: Optional[dict] = Field(serialization_alias="configOverrides")
        log_path: Optional[str] = Field("None", serialization_alias="logPath")
        class LogrotateParams(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            size_threshold_mb: Optional[int] = Field(serialization_alias="sizeThresholdMB")
            time_duration_hrs: Optional[int] = Field(serialization_alias="timeDurationHrs")
        log_rotate: Optional[LogrotateParams] = Field(serialization_alias="logRotate")
        username: Optional[str] = Field("None", serialization_alias="username")
    def update_monitoring_configuration_settings(self,
        path_params: UpdateMonitoringConfigurationSettingsPathParams,
        query_params: Optional[UpdateMonitoringConfigurationSettingsQueryParams],
        body_params: Optional[UpdateMonitoringConfigurationSettingsBodyParams],
    ) -> dict[str, Any]:
        """
        ## Update Monitoring Configuration Settings
        - Document: [Update Monitoring Configuration Settings](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/update-monitoring-log-attributes/)
        - Resource: `PUT /groups/{PROJECT-ID}/automationConfig/monitoringAgentConfig`
        - Description: No description."""
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}/automationConfig/monitoringAgentConfig",
            path_params,
            query_params,
            body_params,
        )
    class UpdateTheSystemLogRotateConfigPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class UpdateTheSystemLogRotateConfigQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class UpdateTheSystemLogRotateConfigBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        num_total: Optional[Any] = Field(serialization_alias="numTotal")
        num_uncompressed: Optional[Any] = Field(serialization_alias="numUncompressed")
        percent_of_diskspace: Optional[Any] = Field(serialization_alias="percentOfDiskspace")
        size_threshold_mb: Optional[Any] = Field(serialization_alias="sizeThresholdMB")
        time_threshold_hrs: Optional[Any] = Field(serialization_alias="timeThresholdHrs")
    def update_the_system_log_rotate_config(self,
        path_params: UpdateTheSystemLogRotateConfigPathParams,
        query_params: Optional[UpdateTheSystemLogRotateConfigQueryParams],
        body_params: Optional[UpdateTheSystemLogRotateConfigBodyParams],
    ) -> dict[str, Any]:
        """
        ## Update the System Log Rotate Config
        - Document: [Update the System Log Rotate Config](https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/update-system-log-rotate-config/)
        - Resource: `PUT /groups/{PROJECT-ID}/automationConfig/systemLogRotateConfig`
        - Description: This endpoint updates the MongoDB Agent system log rotation configuration. After this request completes, Ops Manager modifies the agent configuration and saves the updated version."""
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}/automationConfig/systemLogRotateConfig",
            path_params,
            query_params,
            body_params,
        )