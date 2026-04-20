from ops_manager_sdk import OpsManagerClient, ClientConfig
from ops_manager_sdk.resources.access_list_resource import AccessListResource


def test_access_list_operations() -> None:
    config = ClientConfig(
        base_url="http://host.docker.internal:8080/",
        public_key="qaddrmnh",
        private_key="90325c2e-d762-4566-bdf4-6b233f0204c6",
    )
    client = OpsManagerClient(config)

    path_params = AccessListResource.AddEntriesPathParams(
        user_id="698116eb8b47f47002806ce7",
    )
    body_params = AccessListResource.AddEntriesBodyParams(
        ip_address="172.18.0.1",
    )
    access_list = client.access_list_resource.add_entries(
        path_params=path_params,
        query_params=None,
        body_params=body_params,
    )
    print(access_list)
