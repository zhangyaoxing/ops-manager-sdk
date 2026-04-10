from typing import Any
from pathlib import Path
import re
from jinja2 import Template


def _type_mapping(type_str: str) -> Any:
    """Map the type string from documentation to a Python type hint."""
    type_str = type_str.lower()
    mapping = {
        "string": "str",
        "integer": "int",
        "long": "int",
        "number": "float",
        "boolean": "bool",
        "object": "dict",
        "timestamp": "datetime",
        "array of strings": "list[str]",
        "string array": "list[str]",
        "array of objects": "list[dict]",
        "object array": "list[dict]",
        "array": "list[Any]",
        "date field": "datetime",
    }
    return mapping.get(type_str, "Any")


def _parse_value(value_str: str, type_str: str) -> Any:
    """Parse the string value to the appropriate Python type."""
    if type_str == "int":
        return int(value_str)
    elif type_str == "float":
        return float(value_str)
    elif type_str == "bool":
        return value_str.lower() == "true"
    elif type_str == "str":
        return value_str
    else:
        return value_str


def _resolve_endpoints(endpoints: list[str]) -> list[tuple[str, str]]:
    """Resolve the HTTP method and path from the endpoint strings."""
    result: list[tuple[str, str]] = []
    for e in endpoints:
        parts = e.split()
        if len(parts) != 2:
            raise ValueError(f"Invalid endpoint format: {e}")
        verb: str = parts[0].upper()
        path: str = parts[1]
        # Normalize path parameters to be in the format {ParamName}.
        path_params: list[str] = re.findall(r"\{([^}]+)\}", path)
        for param in path_params:
            replacement = param.strip().replace("-", " ").title().replace(" ", "")
            path = path.replace(f"{{{param}}}", f"{{{replacement}}}")
        result.append((verb, path))
    return result


def _resolve_params(params: list[dict[str, Any]]) -> list[tuple[str, str, bool, Any]]:
    """Resolve the parameter name, type, required status, and default value from the parameter dictionaries."""
    result: list[tuple[str, str, bool, Any]] = []
    for param in params:
        param_name: str = param["name"]
        param_type: str = _type_mapping(param["type"])
        is_required: bool = param.get("required", False)
        default_value: Any = _parse_value(param["default"], param_type)
        result.append((param_name, param_type, is_required, default_value))
    return result


PARAMS_TEMPLATE = """
@dataclass
class {{ param_category }}:
    {% for name, type_str, required, default in params %}
    {{ name }}: {{ type_str }}{% if not required %} = None{% elif default is not None %} = {{ default }}{% endif %}
    {% endfor %}
"""
PARAMS_OBJECT_TEMPLATE = """
@dataclass
class {{ param_obj_name }}:
    path_params: PathParams
    query_params: QueryParams
    body_params: BodyParams
"""
RESOURCE_TEMPLATE = """
class {{ class_name }}(ResourceClient):
    \"\"\"Client for {{ class_name }} resource.\"\"\"
    {% for verb, path in endpoints %}
"""


def resource_generator(api_docs: dict[str, list[dict[str, Any]]]) -> None:
    """
    Generate resource clients based on the extracted API documentation.

    Args:
        api_docs: A dictionary containing the API documentation categorized by resource.
    """
    for resource, apis in api_docs.items():
        code_file: Path = (
            Path.cwd() / f"src/ops_manager_sdk/resources/{resource.lower()}_resource.py"
        )
        param_obj_name: str = f"{resource}Params"
        class_name: str = f"{resource}Resource"
        with code_file.open("w", encoding="utf-8") as f:
            f.write("from dataclasses import dataclass\n")
            f.write("from .base import ResourceClient\n")
            for api in apis:
                title: str = api["title"]
                endpoints: list[str] = api["endpoints"]
                path_params: list[dict[str, Any]] = api["path_params"]
                query_params: list[dict[str, Any]] = api["query_params"]
                body_params: list[dict[str, Any]] = api["body_params"]
                doc_url: str = api["doc_url"]
                template: Template = Template(PARAMS_TEMPLATE)
                path_params_code = template.render(
                    param_category="PathParams", params=_resolve_params(path_params)
                )
                query_params_code = template.render(
                    param_category="QueryParams", params=_resolve_params(query_params)
                )
                body_params_code = template.render(
                    param_category="BodyParams", params=_resolve_params(body_params)
                )
                param_obj_code = Template(PARAMS_OBJECT_TEMPLATE).render(
                    param_obj_name=param_obj_name
                )
                f.write(path_params_code)
                f.write(query_params_code)
                f.write(body_params_code)
                f.write(param_obj_code)
