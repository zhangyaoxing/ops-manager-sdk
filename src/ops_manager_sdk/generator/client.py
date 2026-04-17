from pathlib import Path
from jinja2 import Template

CLIENT_TEMPLATE = """
from httpx import Auth, DigestAuth, Client
from .config import ClientConfig
{% for package_name, class_name in resources %}from .resources.{{ package_name }} import {{class_name}}
{% endfor %}


class OpsManagerClient:
    def __init__(self, cfg: ClientConfig) -> None:
        self._config = cfg
        assert (
            cfg.digest_username is not None and cfg.digest_password is not None
        ), "Digest credentials must be provided"
        auth: Auth = DigestAuth(cfg.digest_username, cfg.digest_password)
        self._client = Client(
            base_url=f"{cfg.base_url.rstrip('/')}/api/public/v1.0",
            headers=cfg.headers,
            timeout=cfg.timeout,
            auth=auth,
        )
    {% for package_name, class_name in resources %}
    @property
    def {{ package_name }}(self) -> {{ class_name }}:
        \"\"\"Get the client for {{ class_name }} resource.\"\"\"
        return {{ class_name }}(self._client)
    {% endfor %}

"""


def generate_client_code(resources: list[tuple[str, str]]) -> None:
    """Generate the OpsManagerClient code based on the provided resources."""
    template = Template(CLIENT_TEMPLATE)
    code = template.render(resources=resources)
    file_name = Path(__file__).parent.parent / "ops_manager_client.py"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(code)
