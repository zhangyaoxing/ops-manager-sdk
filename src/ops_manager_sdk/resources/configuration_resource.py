from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class ConfigurationResource(BaseResource):
    """Client for ConfigurationResource resource."""
    class GetTheAuditLogRotateConfigurationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
    class GetTheAuditLogRotateConfigurationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetTheAuditLogRotateConfigurationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_the_audit_log_rotate_configuration(self,
        path_params: GetTheAuditLogRotateConfigurationPathParams,
        query_params: Optional[GetTheAuditLogRotateConfigurationQueryParams],
        body_params: Optional[GetTheAuditLogRotateConfigurationBodyParams],
    ) -> dict[str, Any]:
        """API: Get the Audit Log Rotate Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/get-audit-log-rotate-config/
        Description: This endpoint returns the current audit log rotation configuration."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/automationConfig/auditLogRotateConfig",
            path_params,
            query_params,
            body_params,
        )
    class GetTheAutomationConfigurationNoSecretsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
    class GetTheAutomationConfigurationNoSecretsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetTheAutomationConfigurationNoSecretsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_the_automation_configuration_no_secrets_(self,
        path_params: GetTheAutomationConfigurationNoSecretsPathParams,
        query_params: Optional[GetTheAutomationConfigurationNoSecretsQueryParams],
        body_params: Optional[GetTheAutomationConfigurationNoSecretsBodyParams],
    ) -> dict[str, Any]:
        """API: Get the Automation Configuration (Redacted Secrets)
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/get-automation-config-no-secrets/
        Description: A project's automation configuration determines the goal state of its MongoDB processes and agents. The MongoDB Agent builds the deployment according to the goals specified."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/automationConfig/noSecrets",
            path_params,
            query_params,
            body_params,
        )
    class GetTheAutomationConfigurationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
    class GetTheAutomationConfigurationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetTheAutomationConfigurationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_the_automation_configuration(self,
        path_params: GetTheAutomationConfigurationPathParams,
        query_params: Optional[GetTheAutomationConfigurationQueryParams],
        body_params: Optional[GetTheAutomationConfigurationBodyParams],
    ) -> dict[str, Any]:
        """API: Get the Automation Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/get-automation-config/
        Description: A project's automation configuration determines the goal state of its MongoDB processes and agents. The MongoDB Agent builds the deployment according to the goals specified."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/automationConfig",
            path_params,
            query_params,
            body_params,
        )
    class GetBackupConfigurationSettingsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
    class GetBackupConfigurationSettingsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetBackupConfigurationSettingsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_backup_configuration_settings(self,
        path_params: GetBackupConfigurationSettingsPathParams,
        query_params: Optional[GetBackupConfigurationSettingsQueryParams],
        body_params: Optional[GetBackupConfigurationSettingsBodyParams],
    ) -> dict[str, Any]:
        """API: Get Backup Configuration Settings
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/get-backup-log-attributes/
        Description: No description found."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/automationConfig/backupAgentConfig",
            path_params,
            query_params,
            body_params,
        )
    class GetMonitoringConfigurationSettingsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
    class GetMonitoringConfigurationSettingsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetMonitoringConfigurationSettingsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_monitoring_configuration_settings(self,
        path_params: GetMonitoringConfigurationSettingsPathParams,
        query_params: Optional[GetMonitoringConfigurationSettingsQueryParams],
        body_params: Optional[GetMonitoringConfigurationSettingsBodyParams],
    ) -> dict[str, Any]:
        """API: Get Monitoring Configuration Settings
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/get-monitoring-log-attributes/
        Description: No description found."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/automationConfig/monitoringAgentConfig",
            path_params,
            query_params,
            body_params,
        )
    class GetTheSystemLogRotateConfigurationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
    class GetTheSystemLogRotateConfigurationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetTheSystemLogRotateConfigurationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_the_system_log_rotate_configuration(self,
        path_params: GetTheSystemLogRotateConfigurationPathParams,
        query_params: Optional[GetTheSystemLogRotateConfigurationQueryParams],
        body_params: Optional[GetTheSystemLogRotateConfigurationBodyParams],
    ) -> dict[str, Any]:
        """API: Get the System Log Rotate Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/get-system-log-rotate-config/
        Description: This endpoint returns the current system log rotation configuration."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/automationConfig/systemLogRotateConfig",
            path_params,
            query_params,
            body_params,
        )
    class UpdateAgentVersionsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
    class UpdateAgentVersionsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class UpdateAgentVersionsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        automation_agent_version: Optional[str] = Field("None", alias="automationAgentVersion")
        bi_connector_version: Optional[str] = Field("None", alias="biConnectorVersion")
        mongo_db_tools_version: Optional[str] = Field("None", alias="mongoDbToolsVersion")
    def update_agent_versions(self,
        path_params: UpdateAgentVersionsPathParams,
        query_params: Optional[UpdateAgentVersionsQueryParams],
        body_params: Optional[UpdateAgentVersionsBodyParams],
    ) -> dict[str, Any]:
        """API: Update Agent Versions
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/update-agent-versions/
        Description: This endpoint updates the MongoDB Agent and tools to the latest versions available at the time of the request:"""
        return self._request(
            "POST",
            "/groups/{PROJECT-ID}/automationConfig/updateAgentVersions",
            path_params,
            query_params,
            body_params,
        )
    class UpdateTheAuditLogRotateConfigPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
    class UpdateTheAuditLogRotateConfigQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class UpdateTheAuditLogRotateConfigBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        size_threshold_mb: Optional[Any] = Field(alias="sizeThresholdMB")
        time_threshold_hrs: Optional[Any] = Field(alias="timeThresholdHrs")
        num_uncompressed: Optional[Any] = Field(alias="numUncompressed")
        percent_of_diskspace: Optional[Any] = Field(alias="percentOfDiskspace")
        num_total: Optional[Any] = Field(alias="numTotal")
    def update_the_audit_log_rotate_config(self,
        path_params: UpdateTheAuditLogRotateConfigPathParams,
        query_params: Optional[UpdateTheAuditLogRotateConfigQueryParams],
        body_params: Optional[UpdateTheAuditLogRotateConfigBodyParams],
    ) -> dict[str, Any]:
        """API: Update the Audit Log Rotate Config
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/update-audit-log-rotate-config/
        Description: This endpoint updates the MongoDB Agent audit log rotation configuration. After this request completes, Ops Manager modifies the agent configuration and saves the updated version."""
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}/automationConfig/auditLogRotateConfig",
            path_params,
            query_params,
            body_params,
        )
    class UpdateTheAutomationConfigurationNoSecretsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
    class UpdateTheAutomationConfigurationNoSecretsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class UpdateTheAutomationConfigurationNoSecretsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def update_the_automation_configuration_no_secrets_(self,
        path_params: UpdateTheAutomationConfigurationNoSecretsPathParams,
        query_params: Optional[UpdateTheAutomationConfigurationNoSecretsQueryParams],
        body_params: Optional[UpdateTheAutomationConfigurationNoSecretsBodyParams],
    ) -> dict[str, Any]:
        """API: Update the Automation Configuration (Sensitive Information Ignored)
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/update-automation-config-no-secrets/
        Description: A project's automation configuration determines the goal state of its MongoDB processes and agents. The MongoDB Agent builds the deployment according to the goals specified."""
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}/automationConfig/noSecrets",
            path_params,
            query_params,
            body_params,
        )
    class UpdateTheAutomationConfigurationPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
    class UpdateTheAutomationConfigurationQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class UpdateTheAutomationConfigurationBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def update_the_automation_configuration(self,
        path_params: UpdateTheAutomationConfigurationPathParams,
        query_params: Optional[UpdateTheAutomationConfigurationQueryParams],
        body_params: Optional[UpdateTheAutomationConfigurationBodyParams],
    ) -> dict[str, Any]:
        """API: Update the Automation Configuration
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/update-automation-config/
        Description: A project's automation configuration determines the goal state of its MongoDB processes and agents. The MongoDB Agent builds the deployment according to the goals specified."""
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}/automationConfig",
            path_params,
            query_params,
            body_params,
        )
    class UpdateBackupConfigurationSettingsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
    class UpdateBackupConfigurationSettingsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class UpdateBackupConfigurationSettingsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        config_overrides: Optional[dict] = Field(alias="configOverrides")
        log_path: Optional[str] = Field("None", alias="logPath")
        log_rotate: Optional[dict] = Field(alias="logRotate")
        username: Optional[str] = Field("None", alias="username")
    def update_backup_configuration_settings(self,
        path_params: UpdateBackupConfigurationSettingsPathParams,
        query_params: Optional[UpdateBackupConfigurationSettingsQueryParams],
        body_params: Optional[UpdateBackupConfigurationSettingsBodyParams],
    ) -> dict[str, Any]:
        """API: Update Backup Configuration Settings
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/update-backup-log-attributes/
        Description: No description found."""
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}/automationConfig/backupAgentConfig",
            path_params,
            query_params,
            body_params,
        )
    class UpdateMonitoringConfigurationSettingsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
    class UpdateMonitoringConfigurationSettingsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class UpdateMonitoringConfigurationSettingsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        config_overrides: Optional[dict] = Field(alias="configOverrides")
        log_path: Optional[str] = Field("None", alias="logPath")
        log_rotate: Optional[dict] = Field(alias="logRotate")
        username: Optional[str] = Field("None", alias="username")
    def update_monitoring_configuration_settings(self,
        path_params: UpdateMonitoringConfigurationSettingsPathParams,
        query_params: Optional[UpdateMonitoringConfigurationSettingsQueryParams],
        body_params: Optional[UpdateMonitoringConfigurationSettingsBodyParams],
    ) -> dict[str, Any]:
        """API: Update Monitoring Configuration Settings
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/update-monitoring-log-attributes/
        Description: No description found."""
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}/automationConfig/monitoringAgentConfig",
            path_params,
            query_params,
            body_params,
        )
    class UpdateTheSystemLogRotateConfigPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
    class UpdateTheSystemLogRotateConfigQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class UpdateTheSystemLogRotateConfigBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        size_threshold_mb: Optional[Any] = Field(alias="sizeThresholdMB")
        time_threshold_hrs: Optional[Any] = Field(alias="timeThresholdHrs")
        num_uncompressed: Optional[Any] = Field(alias="numUncompressed")
        percent_of_diskspace: Optional[Any] = Field(alias="percentOfDiskspace")
        num_total: Optional[Any] = Field(alias="numTotal")
    def update_the_system_log_rotate_config(self,
        path_params: UpdateTheSystemLogRotateConfigPathParams,
        query_params: Optional[UpdateTheSystemLogRotateConfigQueryParams],
        body_params: Optional[UpdateTheSystemLogRotateConfigBodyParams],
    ) -> dict[str, Any]:
        """API: Update the System Log Rotate Config
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/automation-config/update-system-log-rotate-config/
        Description: This endpoint updates the MongoDB Agent system log rotation configuration. After this request completes, Ops Manager modifies the agent configuration and saves the updated version."""
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}/automationConfig/systemLogRotateConfig",
            path_params,
            query_params,
            body_params,
        )