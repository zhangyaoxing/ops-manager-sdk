from typing import Any
import re
from pathlib import Path
from jinja2 import Template
from loguru import logger

from ops_manager_sdk.generator.utils import parse_value, type_mapping

RESOURCE_TEMPLATE = """
from typing import Any, Optional
{% if need_datetime_import %}
from datetime import datetime
{% endif %}
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource

class {{ class_name }}(BaseResource):
    \"\"\"Client for {{ class_name }} resource.\"\"\"
    {% for snippet in code_data %}
    {% if snippet.path_params.needed %}
    class {{ snippet.params_class_name }}PathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        {% for param in snippet.path_params.params %}
        {{ param.name }}: {% if param.required %}{{ param.type }}{% else %}Optional[{{ param.type }}]{% endif %} = Field({% if param.default is not none %}{{ param.default }}, {% endif %}serialization_alias="{{ param.alias }}")
        {% endfor %}
    {% endif %}
    {% if snippet.query_params.needed %}
    class {{ snippet.params_class_name }}QueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        {% for param in snippet.query_params.params %}
        {{ param.name }}: {% if param.required %}{{ param.type }}{% else %}Optional[{{ param.type }}]{% endif %} = Field({% if param.default is not none %}{{ param.default }}, {% endif %}serialization_alias="{{ param.alias }}")
        {% endfor %}
    {% endif %}
    {% if snippet.body_params.needed %}
    class {{ snippet.params_class_name }}BodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        {% for param in snippet.body_params.params %}
        {{ param.name }}: {% if param.required %}{{ param.type }}{% else %}Optional[{{ param.type }}]{% endif %} = Field({% if param.default is not none %}{{ param.default }}, {% endif %}serialization_alias="{{ param.alias }}")
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
        \"\"\"{{ snippet.doc }}\"\"\"
        return self._request(
            "{{ snippet.verb }}",
            "{{ snippet.path }}",
            {% if snippet.path_params.needed %}path_params{%else%}None{% endif %},
            {% if snippet.query_params.needed %}query_params{%else%}None{% endif %},
            {% if snippet.body_params.needed %}body_params{%else%}None{% endif %},
        )
    {% endfor %}

"""


class APIResource:
    def __init__(self, name: str, apis: list[dict[str, Any]]) -> None:
        self.name: str = name
        self.apis: list[dict[str, Any]] = apis

    def _resolve_endpoint(self, endpoint: str) -> tuple[str, str]:
        """Resolve the HTTP method and path from the endpoint strings."""
        parts = endpoint.split()
        if len(parts) != 2:
            raise ValueError(f"Invalid endpoint format: {endpoint}")
        verb: str = parts[0].upper()
        path: str = parts[1]
        return verb, path

    def _resolve_params(self, params: list[dict[str, Any]]) -> tuple[bool, list[dict[str, Any]]]:
        """Resolve the parameter name, type, required status,
        and default value from the parameter dictionaries."""
        result: list[dict[str, Any]] = []
        params_required: bool = False
        for param in params:
            required_str: str = param.get("required", "").lower()
            is_required: bool = "required" in required_str and "required if" not in required_str
            original_name: str = param["name"]
            if "." in original_name:
                logger.warning(
                    f"Parameter name '{original_name}' is a nested parameter. Which is not supported in the current version. Skipping..."
                )
                continue
            if "{" in original_name or "}" in original_name:
                original_name = original_name.strip("{}")
            # Sometimes the required is written in the parameter name.
            if "\nrequired" in original_name.lower():
                original_name = original_name.split("\n")[0]
                is_required = True
            original_name = original_name.replace("\n", "").strip()
            if "-" in original_name:
                param_name: str = original_name.replace("-", "_").lower()
            else:
                param_name = re.sub(
                    r"(?<!^)(?=[A-Z][a-z])|(?<=[a-z0-9])(?=[A-Z])", "_", original_name
                ).lower()
                param_name = re.sub(r"[^\w]+", "", param_name)
            param_type: str = type_mapping(param["type"])
            if is_required:
                params_required = True
            default_value: Any = parse_value(param["default"], param_type)
            result.append(
                {
                    "name": param_name,
                    "alias": original_name,
                    "type": param_type,
                    "required": is_required,
                    "default": default_value if param_type != "str" else f'"{default_value}"',
                }
            )
        return params_required, result

    def _pre_process(self) -> dict[str, Any]:
        """Pre-process the API documentation to extract information for code generation."""
        code_gen_data: dict[str, list[dict[str, Any]]] = {}

        class_name: str = re.sub(r"[^\w]+", "", f"{self.name}Resource")
        code_gen_data[class_name] = []
        for api in self.apis:
            verb, path = self._resolve_endpoint(api["endpoints"][0])
            doc = f"""API: {api['title']}
        Document: {api['doc_url']}
        Description: {api.get('description', '')}"""
            path_required, path_params = self._resolve_params(api.get("path_params", []))
            query_required, query_params = self._resolve_params(api.get("query_params", []))
            body_required, body_params = self._resolve_params(api.get("body_params", []))
            path_needed = len(path_params) > 0
            query_needed = len(query_params) > 0
            body_needed = len(body_params) > 0
            need_datetime = any(
                param["type"] == "datetime" for param in path_params + query_params + body_params
            )
            code_gen_data[class_name].append(
                {
                    "method_name": re.sub(r"[^\w]+", "_", api["name"].lower()),
                    "params_class_name": re.sub(r"[^\w]+", "", api["name"].title()),
                    "verb": verb,
                    "path": path,
                    "path_params": {
                        "required": path_required,
                        "needed": path_needed,
                        "params": path_params,
                    },
                    "query_params": {
                        "required": query_required,
                        "needed": query_needed,
                        "params": query_params,
                    },
                    "body_params": {
                        "required": body_required,
                        "needed": body_needed,
                        "params": body_params,
                    },
                    "body_type": api.get("body_type", "object"),
                    "need_datetime": need_datetime,
                    "doc": doc,
                }
            )
        return code_gen_data

    def _post_code_process(self, code: str) -> str:
        """Post-process the generated code to clean up extra blank lines."""
        return re.sub(r"\n\s*\n", "\n", code).strip()

    def generate_code(self) -> list[tuple[str, str]]:
        """
        Generate resource code based on the extracted API documentation.

        Args:
            api_docs: A dictionary containing the API documentation categorized by resource.
        """
        resources: list[tuple[str, str]] = []
        code_gen_data = self._pre_process()
        for class_name, snippets in code_gen_data.items():
            template = Template(RESOURCE_TEMPLATE)
            need_datetime_import = any(snippet["need_datetime"] for snippet in snippets)
            code = template.render(
                class_name=class_name,
                code_data=snippets,
                need_datetime_import=need_datetime_import,
            )
            code = self._post_code_process(code)
            package_name = re.sub(
                r"(?<!^)(?=[A-Z][a-z])|(?<=[a-z0-9])(?=[A-Z])", "_", class_name
            ).lower()
            file_name = f"{package_name}.py"
            output_path = Path(__file__).parent.parent / "resources" / f"{file_name}"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(code)
            resources.append((package_name, class_name))
        return resources
