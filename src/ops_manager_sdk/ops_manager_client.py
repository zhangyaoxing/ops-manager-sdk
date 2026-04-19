
from httpx import Auth, DigestAuth, Client
from .config import ClientConfig
from .resources.access_list_resource import AccessListResource
from .resources.backup_daemon_resource import BackupDaemonResource
from .resources.project_backup_job_resource import ProjectBackupJobResource
from .resources.oplog_store_resource import OplogStoreResource
from .resources.s3_oplog_resource import S3OplogResource
from .resources.file_system_store_resource import FileSystemStoreResource
from .resources.blockstore_resource import BlockstoreResource
from .resources.s3_compatible_blockstore_resource import S3CompatibleBlockstoreResource
from .resources.sync_store_resource import SyncStoreResource
from .resources.agents_resource import AgentsResource
from .resources.alert_configurations_resource import AlertConfigurationsResource
from .resources.alerts_resource import AlertsResource
from .resources.global_access_list_resource import GlobalAccessListResource
from .resources.global_api_keys_resource import GlobalApiKeysResource
from .resources.organization_api_keys_resource import OrganizationApiKeysResource
from .resources.organization_access_lists_resource import OrganizationAccessListsResource
from .resources.api_keys_on_projects_resource import ApiKeysOnProjectsResource
from .resources.configuration_resource import ConfigurationResource
from .resources.automation_resource import AutomationResource
from .resources.deployment_regions_resource import DeploymentRegionsResource
from .resources.backup_configurations_resource import BackupConfigurationsResource
from .resources.snapshot_schedule_resource import SnapshotScheduleResource
from .resources.migrate_to_mongodb_atlas_resource import MigrateToMongodbAtlasResource
from .resources.clusters_resource import ClustersResource
from .resources.feature_control_policies_resource import FeatureControlPoliciesResource
from .resources.databases_resource import DatabasesResource
from .resources.server_usage_resource import ServerUsageResource
from .resources.disks_resource import DisksResource
from .resources.events_resource import EventsResource
from .resources.global_events_resource import GlobalEventsResource
from .resources.global_alert_configurations_resource import GlobalAlertConfigurationsResource
from .resources.global_alerts_resource import GlobalAlertsResource
from .resources.projects_resource import ProjectsResource
from .resources.hosts_resource import HostsResource
from .resources.import_deployments_resource import ImportDeploymentsResource
from .resources.organizations_resource import OrganizationsResource
from .resources.backup_encryption_keys_resource import BackupEncryptionKeysResource
from .resources.log_collection_jobs_resource import LogCollectionJobsResource
from .resources.maintenance_windows_resource import MaintenanceWindowsResource
from .resources.measurements_resource import MeasurementsResource
from .resources.performance_advisor_resource import PerformanceAdvisorResource
from .resources.restore_jobs_resource import RestoreJobsResource
from .resources.root_resource import RootResource
from .resources.snapshots_resource import SnapshotsResource
from .resources.teams_resource import TeamsResource
from .resources.telemetry_resource import TelemetryResource
from .resources.integration_settings_resource import IntegrationSettingsResource
from .resources.users_resource import UsersResource
from .resources.version_manifest_resource import VersionManifestResource



class OpsManagerClient:
    def __init__(self, cfg: ClientConfig) -> None:
        self._config = cfg
        auth: Auth = DigestAuth(cfg.public_key, cfg.private_key)
        self._client = Client(
            base_url=f"{cfg.base_url.rstrip('/')}/api/public/v1.0",
            headers=cfg.headers,
            timeout=cfg.timeout,
            auth=auth,
        )
    
    @property
    def access_list_resource(self) -> AccessListResource:
        """Get the client for AccessListResource resource."""
        return AccessListResource(self._client)
    
    @property
    def backup_daemon_resource(self) -> BackupDaemonResource:
        """Get the client for BackupDaemonResource resource."""
        return BackupDaemonResource(self._client)
    
    @property
    def project_backup_job_resource(self) -> ProjectBackupJobResource:
        """Get the client for ProjectBackupJobResource resource."""
        return ProjectBackupJobResource(self._client)
    
    @property
    def oplog_store_resource(self) -> OplogStoreResource:
        """Get the client for OplogStoreResource resource."""
        return OplogStoreResource(self._client)
    
    @property
    def s3_oplog_resource(self) -> S3OplogResource:
        """Get the client for S3OplogResource resource."""
        return S3OplogResource(self._client)
    
    @property
    def file_system_store_resource(self) -> FileSystemStoreResource:
        """Get the client for FileSystemStoreResource resource."""
        return FileSystemStoreResource(self._client)
    
    @property
    def blockstore_resource(self) -> BlockstoreResource:
        """Get the client for BlockstoreResource resource."""
        return BlockstoreResource(self._client)
    
    @property
    def s3_compatible_blockstore_resource(self) -> S3CompatibleBlockstoreResource:
        """Get the client for S3CompatibleBlockstoreResource resource."""
        return S3CompatibleBlockstoreResource(self._client)
    
    @property
    def sync_store_resource(self) -> SyncStoreResource:
        """Get the client for SyncStoreResource resource."""
        return SyncStoreResource(self._client)
    
    @property
    def agents_resource(self) -> AgentsResource:
        """Get the client for AgentsResource resource."""
        return AgentsResource(self._client)
    
    @property
    def alert_configurations_resource(self) -> AlertConfigurationsResource:
        """Get the client for AlertConfigurationsResource resource."""
        return AlertConfigurationsResource(self._client)
    
    @property
    def alerts_resource(self) -> AlertsResource:
        """Get the client for AlertsResource resource."""
        return AlertsResource(self._client)
    
    @property
    def global_access_list_resource(self) -> GlobalAccessListResource:
        """Get the client for GlobalAccessListResource resource."""
        return GlobalAccessListResource(self._client)
    
    @property
    def global_api_keys_resource(self) -> GlobalApiKeysResource:
        """Get the client for GlobalApiKeysResource resource."""
        return GlobalApiKeysResource(self._client)
    
    @property
    def organization_api_keys_resource(self) -> OrganizationApiKeysResource:
        """Get the client for OrganizationApiKeysResource resource."""
        return OrganizationApiKeysResource(self._client)
    
    @property
    def organization_access_lists_resource(self) -> OrganizationAccessListsResource:
        """Get the client for OrganizationAccessListsResource resource."""
        return OrganizationAccessListsResource(self._client)
    
    @property
    def api_keys_on_projects_resource(self) -> ApiKeysOnProjectsResource:
        """Get the client for ApiKeysOnProjectsResource resource."""
        return ApiKeysOnProjectsResource(self._client)
    
    @property
    def configuration_resource(self) -> ConfigurationResource:
        """Get the client for ConfigurationResource resource."""
        return ConfigurationResource(self._client)
    
    @property
    def automation_resource(self) -> AutomationResource:
        """Get the client for AutomationResource resource."""
        return AutomationResource(self._client)
    
    @property
    def deployment_regions_resource(self) -> DeploymentRegionsResource:
        """Get the client for DeploymentRegionsResource resource."""
        return DeploymentRegionsResource(self._client)
    
    @property
    def backup_configurations_resource(self) -> BackupConfigurationsResource:
        """Get the client for BackupConfigurationsResource resource."""
        return BackupConfigurationsResource(self._client)
    
    @property
    def snapshot_schedule_resource(self) -> SnapshotScheduleResource:
        """Get the client for SnapshotScheduleResource resource."""
        return SnapshotScheduleResource(self._client)
    
    @property
    def migrate_to_mongodb_atlas_resource(self) -> MigrateToMongodbAtlasResource:
        """Get the client for MigrateToMongodbAtlasResource resource."""
        return MigrateToMongodbAtlasResource(self._client)
    
    @property
    def clusters_resource(self) -> ClustersResource:
        """Get the client for ClustersResource resource."""
        return ClustersResource(self._client)
    
    @property
    def feature_control_policies_resource(self) -> FeatureControlPoliciesResource:
        """Get the client for FeatureControlPoliciesResource resource."""
        return FeatureControlPoliciesResource(self._client)
    
    @property
    def databases_resource(self) -> DatabasesResource:
        """Get the client for DatabasesResource resource."""
        return DatabasesResource(self._client)
    
    @property
    def server_usage_resource(self) -> ServerUsageResource:
        """Get the client for ServerUsageResource resource."""
        return ServerUsageResource(self._client)
    
    @property
    def disks_resource(self) -> DisksResource:
        """Get the client for DisksResource resource."""
        return DisksResource(self._client)
    
    @property
    def events_resource(self) -> EventsResource:
        """Get the client for EventsResource resource."""
        return EventsResource(self._client)
    
    @property
    def global_events_resource(self) -> GlobalEventsResource:
        """Get the client for GlobalEventsResource resource."""
        return GlobalEventsResource(self._client)
    
    @property
    def global_alert_configurations_resource(self) -> GlobalAlertConfigurationsResource:
        """Get the client for GlobalAlertConfigurationsResource resource."""
        return GlobalAlertConfigurationsResource(self._client)
    
    @property
    def global_alerts_resource(self) -> GlobalAlertsResource:
        """Get the client for GlobalAlertsResource resource."""
        return GlobalAlertsResource(self._client)
    
    @property
    def projects_resource(self) -> ProjectsResource:
        """Get the client for ProjectsResource resource."""
        return ProjectsResource(self._client)
    
    @property
    def hosts_resource(self) -> HostsResource:
        """Get the client for HostsResource resource."""
        return HostsResource(self._client)
    
    @property
    def import_deployments_resource(self) -> ImportDeploymentsResource:
        """Get the client for ImportDeploymentsResource resource."""
        return ImportDeploymentsResource(self._client)
    
    @property
    def organizations_resource(self) -> OrganizationsResource:
        """Get the client for OrganizationsResource resource."""
        return OrganizationsResource(self._client)
    
    @property
    def backup_encryption_keys_resource(self) -> BackupEncryptionKeysResource:
        """Get the client for BackupEncryptionKeysResource resource."""
        return BackupEncryptionKeysResource(self._client)
    
    @property
    def log_collection_jobs_resource(self) -> LogCollectionJobsResource:
        """Get the client for LogCollectionJobsResource resource."""
        return LogCollectionJobsResource(self._client)
    
    @property
    def maintenance_windows_resource(self) -> MaintenanceWindowsResource:
        """Get the client for MaintenanceWindowsResource resource."""
        return MaintenanceWindowsResource(self._client)
    
    @property
    def measurements_resource(self) -> MeasurementsResource:
        """Get the client for MeasurementsResource resource."""
        return MeasurementsResource(self._client)
    
    @property
    def performance_advisor_resource(self) -> PerformanceAdvisorResource:
        """Get the client for PerformanceAdvisorResource resource."""
        return PerformanceAdvisorResource(self._client)
    
    @property
    def restore_jobs_resource(self) -> RestoreJobsResource:
        """Get the client for RestoreJobsResource resource."""
        return RestoreJobsResource(self._client)
    
    @property
    def root_resource(self) -> RootResource:
        """Get the client for RootResource resource."""
        return RootResource(self._client)
    
    @property
    def snapshots_resource(self) -> SnapshotsResource:
        """Get the client for SnapshotsResource resource."""
        return SnapshotsResource(self._client)
    
    @property
    def teams_resource(self) -> TeamsResource:
        """Get the client for TeamsResource resource."""
        return TeamsResource(self._client)
    
    @property
    def telemetry_resource(self) -> TelemetryResource:
        """Get the client for TelemetryResource resource."""
        return TelemetryResource(self._client)
    
    @property
    def integration_settings_resource(self) -> IntegrationSettingsResource:
        """Get the client for IntegrationSettingsResource resource."""
        return IntegrationSettingsResource(self._client)
    
    @property
    def users_resource(self) -> UsersResource:
        """Get the client for UsersResource resource."""
        return UsersResource(self._client)
    
    @property
    def version_manifest_resource(self) -> VersionManifestResource:
        """Get the client for VersionManifestResource resource."""
        return VersionManifestResource(self._client)
    
