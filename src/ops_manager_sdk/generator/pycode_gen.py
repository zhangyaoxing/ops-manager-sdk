import re
from typing import Any
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
        ver_num: str = version("pyomsdk")
        assert base_url and public_key and private_key, "Base URL, public key, and private key are required to initialize the OpsManagerClient."
        auth: Auth = DigestAuth(public_key, private_key)
        self._client = Client(
            base_url=f"{base_url.rstrip('/')}",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "User-Agent": f"pyomsdk/{ver_num}",
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

RESOURCE_TEMPLATE = """
\"\"\"Auto-generated client for {{ class_name }} resource.
Any manual changes to this file may be overwritten when the code is regenerated.
\"\"\"
from typing import Any, Optional
{% if need_datetime_import %}
from datetime import datetime
{% endif %}
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
from .enums import *

class {{ class_name }}(BaseResource):
    \"\"\"Client for {{ class_name }} resource.
    \"\"\"
    {% for snippet in code_data %}
    {% if snippet.path_params.needed %}
    class {{ snippet.params_class_name }}PathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        {% for param in snippet.path_params.params %}
        {{ param.name }}: {% if param.required %}{{ param.type }}{% else %}Optional[{{ param.type }}]{% endif %} = Field({% if param.default is not none or not param.required %}default={{ param.default }}, {% endif %}serialization_alias="{{ param.alias }}")
        \"\"\"{{ param.description }}
        \"\"\"
        {% endfor %}
    {% endif %}
    {% if snippet.query_params.needed %}
    class {{ snippet.params_class_name }}QueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        {% for param in snippet.query_params.params %}
        {% if param.has_nested_params %}
        class {{ param.class_name }}(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            {% for nested_param in param.nested_params %}
            {{ nested_param.name }}: {% if nested_param.required %}{{ nested_param.type }}{% else %}Optional[{{ nested_param.type }}]{% endif %} = Field({% if nested_param.default is not none or not nested_param.required %}default={{ nested_param.default }}, {% endif %}serialization_alias="{{ nested_param.alias }}")
            \"\"\"{{ nested_param.description }}
            \"\"\"
            {% endfor %}
        {% endif %}
        {{ param.name }}: {% if param.required %}{{ param.type }}{% else %}Optional[{{ param.type }}]{% endif %} = Field({% if param.default is not none or not param.required %}default={{ param.default }}, {% endif %}serialization_alias="{{ param.alias }}")
        \"\"\"{{ param.description }}
        \"\"\"
        {% endfor %}
    {% endif %}
    {% if snippet.body_params.needed %}
    class {{ snippet.params_class_name }}BodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        {% for param in snippet.body_params.params %}
        {% if param.has_nested_params %}
        class {{ param.class_name }}(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            {% for nested_param in param.nested_params %}
            {{ nested_param.name }}: {% if nested_param.required %}{{ nested_param.type }}{% else %}Optional[{{ nested_param.type }}]{% endif %} = Field({% if nested_param.default is not none or not nested_param.required %}default={{ nested_param.default }}, {% endif %}serialization_alias="{{ nested_param.alias }}")
            \"\"\"{{ nested_param.description }}
            \"\"\"
            {% endfor %}
        {% endif %}
        {{ param.name }}: {% if param.required %}{{ param.type }}{% else %}Optional[{{ param.type }}]{% endif %} = Field({% if param.default is not none or not param.required %}default={{ param.default }}, {% endif %}serialization_alias="{{ param.alias }}")
        \"\"\"{{ param.description }}
        \"\"\"
        {% endfor %}
    {% endif %}
    def {{ snippet.method_name }}(self,
        {% if snippet.path_params.needed %}
        path_params: {% if snippet.path_params.required %}{{ snippet.params_class_name }}PathParams{% else %}Optional[{{ snippet.params_class_name }}PathParams]{% endif %},
        {% endif %}
        {% if snippet.query_params.needed %}
        query_params: {% if snippet.query_params.required %}{{ snippet.params_class_name }}QueryParams{% else %}Optional[{{ snippet.params_class_name }}QueryParams]{% endif %},
        {% endif %}
        {% if snippet.body_params.needed %}
        body_params: {% if snippet.body_type == "array" %}list[{% endif %}{% if snippet.body_params.required %}{{ snippet.params_class_name }}BodyParams{% else %}Optional[{{ snippet.params_class_name }}BodyParams]{% endif %}{% if snippet.body_type == "array" %}]{% endif %},
        {% endif %}
    ) -> dict[str, Any]:
        \"\"\"{{ snippet.doc }}
        \"\"\"
        return self._request(
            "{{ snippet.verb }}",
            "{{ snippet.path }}",
            {% if snippet.path_params.needed %}path_params{%else%}None{% endif %},
            {% if snippet.query_params.needed %}query_params{%else%}None{% endif %},
            {% if snippet.body_params.needed %}body_params{%else%}None{% endif %},
        )
    {% endfor %}

"""


def gen_resource_code(class_name: str, apis: list[dict[str, Any]]) -> tuple[str, str]:
    """Generate the resource class code based on the provided API information."""
    package_name = re.sub(r"(?<!^)(?=[A-Z][a-z])|(?<=[a-z0-9])(?=[A-Z])", "_", class_name).lower()
    template = Template(RESOURCE_TEMPLATE)
    need_datetime_import = any(api["need_datetime"] for api in apis)
    code = template.render(
        class_name=class_name,
        code_data=apis,
        need_datetime_import=need_datetime_import,
    )
    file_name = f"{package_name}.py"
    output_path = Path().cwd() / "pyomsdk/src/pyomsdk/resources" / f"{file_name}"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(code)
    return package_name, class_name


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
