from tests.shared import get_client


def test_projects_resource() -> None:
    client = get_client()
    query_params = client.projects_resource.GetAllQueryParams()
    query_params.page_num = 1
    query_params.items_per_page = 10
    projects = client.projects_resource.get_all(query_params=query_params)
    assert isinstance(projects["results"], list)


def test_projects_resource_add() -> None:
    client = get_client()
    project_name = "Test Project"
    body_params = client.projects_resource.CreateBodyParams(
        name=project_name,
        org_id="698117018b47f47002806d04",
    )
    new_project = client.projects_resource.create(query_params=None, body_params=body_params)
    assert new_project["result"]["name"] == project_name
