PARAM_TO_ENUM = [
    {"param": "headDiskType", "enum": "HeadDiskType", "urls": "*"},
    {"param": "writeConcern", "enum": "WriteConcern", "urls": "*"},
    {"param": "serverType.name", "enum": "ServerTypeName", "urls": "*"},
    {
        "param": "serverType",
        "enum": "ServerTypeName",
        "urls": [
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/create-one-physical-host/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/usage/update-one-physical-host/",
        ],
    },
    {"param": "serverType.label", "enum": "ServerTypeLabel", "urls": "*"},
    {"param": "policies.policy", "enum": "Policy", "urls": "*"},
    {"param": "oplogStoreFilter.type", "enum": "OplogStoreFilterType", "urls": "*"},
    {
        "param": "snapshotStoreFilter.type",
        "enum": "SnapshotStoreFilterType",
        "urls": "*",
    },
    {"param": "s3AuthMethod", "enum": "S3AuthMethod", "urls": "*"},
    {
        "param": "TYPE",
        "enum": "AgentType",
        "urls": "https://www.mongodb.com/docs/ops-manager/current/reference/api/agents-get-by-type/",
    },
    {"param": "eventTypeName", "enum": "EventTypeName", "urls": "*"},
    {"param": "matchers.fieldName", "enum": "MatcherFieldName", "urls": "*"},
    {"param": "matchers.operator", "enum": "MatcherOperator", "urls": "*"},
    {"param": "matchers.value", "enum": "MatcherValue", "urls": "*"},
    {"param": "metricThreshold.operator", "enum": "ThresholdOperator", "urls": "*"},
    {"param": "threshold.operator", "enum": "ThresholdOperator", "urls": "*"},
    {"param": "metricThreshold.units", "enum": "Unit", "urls": "*"},
    {"param": "notifications.typeName", "enum": "NotificationsTypeName", "urls": "*"},
    {
        "param": "status",
        "enum": "AlertStatus",
        "urls": [
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/global-alerts-get-all/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/alerts-get-all-alerts/",
        ],
    },
    {
        "param": "roles",
        "enum": "GlobalRole",
        "urls": [
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/create-one-global-api-key/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/global/update-one-global-api-key/",
        ],
    },
    {
        "param": "roles",
        "enum": "OrgRole",
        "urls": [
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/org/create-one-org-api-key/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/org/update-one-org-api-key/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/organizations/create-one-invitation/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/organizations/update-one-invitation-by-id/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/organizations/update-one-invitation/",
        ],
    },
    {
        "param": "ldapGroupMappings.roleName",
        "enum": "OrgRole",
        "urls": [
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/organizations/organization-create-one/"
        ],
    },
    {
        "param": "roles",
        "enum": "GroupRole",
        "urls": [
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/project/assign-one-org-apiKey-to-one-project/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/project/create-one-apiKey-in-one-project/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/api-keys/project/update-one-apiKey-in-one-project/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/projects/create-one-invitation/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/projects/update-one-invitation-by-id/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/invitations/projects/update-one-invitation/",
        ],
    },
    {
        "param": "roleNames",
        "enum": "GroupRole",
        "urls": [
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/groups/project-add-team/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/teams/teams-update-roles/",
        ],
    },
    {
        "param": "roles.roleName",
        "enum": "AllRole",
        "urls": [
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/user-create/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/user-update/",
        ],
    },
    {"param": "authMechanismName", "enum": "AuthMechanismName", "urls": "*"},
    {"param": "authMechanism", "enum": "AuthMechanismName", "urls": "*"},
    {
        "param": "statusName",
        "enum": "BackupStatusName",
        "urls": [
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/update-backup-config/"
        ],
    },
    {"param": "storageEngineName", "enum": "StorageEngineName", "urls": "*"},
    {"param": "resourceType", "enum": "ResourceType", "urls": "*"},
    {
        "param": "logTypes",
        "enum": "ServerLogType",
        "urls": [
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/om-log-collections/om-log-collections-submit/"
        ],
    },
    {"param": "logTypes", "enum": "LogType", "urls": "*"},
    {"param": "delivery.methodName", "enum": "DeliveryMethodName", "urls": "*"},
    {
        "param": "completed",
        "enum": "SnapshotCompletedState",
        "urls": [
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/snapshots/get-all-snapshots-for-one-cluster/"
        ],
    },
    {"param": "INTEGRATION-TYPE", "enum": "IntegrationType", "urls": "*"},
    {
        "param": "type",
        "enum": "IntegrationType",
        "urls": [
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/third-party-integration-settings-create/",
            "https://www.mongodb.com/docs/ops-manager/current/reference/api/third-party-integration-settings-update/",
        ],
    },
]
