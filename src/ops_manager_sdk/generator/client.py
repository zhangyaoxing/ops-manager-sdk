from pathlib import Path
from jinja2 import Template

CLIENT_TEMPLATE = """
from importlib.metadata import version
from httpx import Auth, DigestAuth, Client
{% for package_name, class_name in resources %}from .resources import {{class_name}}
{% endfor %}


class OpsManagerClient:
    def __init__(
        self, base_url: str, public_key: str, private_key: str, timeout: float = 30.0
    ) -> None:
        ver_num: str = version("ops-manager-sdk")
        auth: Auth = DigestAuth(public_key, private_key)
        self._client = Client(
            base_url=f"{base_url.rstrip('/')}/api/public/v1.0",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "User-Agent": f"ops-manager-sdk-python/{ver_num}",
            },
            timeout=timeout,
            auth=auth,
        )
    {% for package_name, class_name in resources %}
    @property
    def {{ package_name }}(self) -> {{ class_name }}:
        \"\"\"Get the client for {{ class_name }} resource.\"\"\"
        return {{ class_name }}(self._client){% endfor %}

"""


def gen_client_code(resources: list[tuple[str, str]]) -> None:
    """Generate the OpsManagerClient code based on the provided resources."""
    template = Template(CLIENT_TEMPLATE)
    code = template.render(resources=resources)
    file_name = Path().cwd() / "pyomsdk/src/pyomsdk/ops_manager_client.py"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(code)


def gen_resources_init_code(resources: list[tuple[str, str]]) -> None:
    """Generate the __init__.py code based on the provided resources."""
    res = resources + [
        ("integration_settings", "PagerDutyIntegrationSettings"),
        ("integration_settings", "SlackIntegrationSettings"),
        ("integration_settings", "DatadogIntegrationSettings"),
        ("integration_settings", "HipChatIntegrationSettings"),
        ("integration_settings", "OpsgenieIntegrationSettings"),
        ("integration_settings", "VictorOpsIntegrationSettings"),
        ("integration_settings", "WebhookIntegrationSettings"),
        ("integration_settings", "MicrosoftTeamsIntegrationSettings"),
        ("integration_settings", "PrometheusIntegrationSettings"),
    ]
    imports = "\n".join(
        [f"from .{package_name} import {class_name}" for package_name, class_name in res]
    )
    init_code = (
        f"{imports}\n\n__all__ = [\n"
        + ",\n".join([f'    "{class_name}"' for _, class_name in res])
        + "\n]"
    )
    file_name = Path().cwd() / "pyomsdk/src/pyomsdk/resources/__init__.py"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(init_code)
