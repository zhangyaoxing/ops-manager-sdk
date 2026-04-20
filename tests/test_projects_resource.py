from tests.shared import get_client


def test_projects_resource() -> None:
    client = get_client()
    projects = client.projects_resource.get_all(query_params=None)
    assert isinstance(projects, list)


def test_projects_resource_add() -> None:
    client = get_client()
    project_name = "Test Project"
    body_params = client.projects_resource.CreateBodyParams(
        name=project_name,
        org_id="698117018b47f47002806d04",
    )
    new_project = client.projects_resource.create(query_params=None, body_params=body_params)
    assert new_project["name"] == project_name
