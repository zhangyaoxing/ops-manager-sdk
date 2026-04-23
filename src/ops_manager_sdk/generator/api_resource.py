from typing import Any, Optional
import re
from loguru import logger
from ops_manager_sdk.generator.utils import parse_value, type_mapping
from ops_manager_sdk.generator.enum import PARAM_TO_ENUM


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
        logger.debug(f"Resolved endpoint: verb={verb}, path={path}")
        return verb, path

    def _resolve_params(
        self, params: list[dict[str, Any]], url: str
    ) -> tuple[bool, list[dict[str, Any]]]:
        """Resolve the parameter name, type, required status,
        and default value from the parameter dictionaries."""
        result: list[dict[str, Any]] = []
        params_required: bool = False
        # Must sort the parameters by name to ensure the parent parameters are always before the nested parameters.
        # Because the nested parameters will be moved into the parent parameters.
        params_sorted = sorted(params, key=lambda x: x["name"])
        parent_param: Optional[dict[str, Any]] = None
        for param in params_sorted:
            required_str: str = param.get("required", "").lower()
            is_required: bool = "required" in required_str and "required if" not in required_str
            original_name: str = param["name"].strip(".")

            original_name = original_name.replace("\n", "").strip()
            if "-" in original_name:
                param_name: str = original_name.replace("-", "_").lower()
                logger.debug(
                    f"Malformed parameter name: {original_name}. Converted to: {param_name}"
                )
            else:
                param_name = re.sub(
                    r"(?<!^)(?=[A-Z][a-z])|(?<=[a-z0-9])(?=[A-Z])", "_", original_name
                ).lower()
                param_name = re.sub(r"[^\w\.]+", "", param_name)
                logger.debug(f"Converted parameter name: {original_name} to {param_name}")
            param_type: str = type_mapping(param["type"])
            if is_required:
                params_required = True
            default_value: Any = parse_value(param["default"], param_type)
            class_name: str = re.sub(r"[^\w]+", "", f"{original_name.title()}Params")
            desc: str = param.get("description", "No description.")
            item: dict = next(
                (item for item in PARAM_TO_ENUM if original_name == item["param"]), None
            )
            if item and (url in item["urls"] or item["urls"] == "*"):
                enum_name = item["enum"]
                param_type = enum_name
                logger.debug(f"Override parameter type of {original_name} to {param_type}")
                if default_value is not None:
                    default_value = f"{enum_name}.{default_value.upper()}"
            # Handle nested params
            if "." in original_name:
                if parent_param is None:
                    # Because params are sorted by name,
                    # The last element in the result must be the parent parameter.
                    parent_param = result[-1]
                    logger.debug(
                        f"Processing nested parameter: {original_name} with parent {parent_param['name']}"
                    )
                if "nested_params" not in parent_param:
                    parent_param["nested_params"] = []
                    parent_param["has_nested_params"] = True
                    if "list" in parent_param["type"]:
                        parent_param["type"] = f"list[{parent_param['class_name']}]"
                    else:
                        parent_param["type"] = parent_param["class_name"]
                    logger.debug(
                        f"Updated parent parameter: {parent_param['name']} type to {parent_param['type']}"
                    )
                param_name = param_name.split(".")[-1]
                original_name = original_name.split(".")[-1]
                logger.debug(
                    f"Adding nested parameter: {param_name} to parent {parent_param['name']}"
                )
                parent_param["nested_params"].append(
                    {
                        "name": param_name,
                        "alias": original_name,
                        "type": param_type,
                        "required": is_required,
                        "default": default_value if param_type != "str" else f'"{default_value}"',
                        "description": desc,
                    }
                )
            else:
                parent_param = None
                result.append(
                    {
                        "name": param_name,
                        "class_name": class_name,
                        "alias": original_name,
                        "type": param_type,
                        "required": is_required,
                        "default": default_value if param_type != "str" else f'"{default_value}"',
                        "description": desc,
                    }
                )
        return params_required, result

    def normalize_doc_data(self) -> tuple[str, list[dict[str, Any]]]:
        """Pre-process the API documentation to extract information for code generation."""
        class_name: str = re.sub(r"[^\w]+", "", f"{self.name}Resource")
        normalized_apis: list[dict[str, Any]] = []
        for api in self.apis:
            verb, path = self._resolve_endpoint(api["endpoints"][0])
            doc = f"""
        ## {api['title']}
        - Document: [{api['name']}]({api['doc_url']})
        - Resource: `{api["endpoints"][0]}`
        - Description: {api.get('description', '')}"""
            path_required, path_params = self._resolve_params(
                api.get("path_params", []), url=api["doc_url"]
            )
            query_required, query_params = self._resolve_params(
                api.get("query_params", []), url=api["doc_url"]
            )
            body_required, body_params = self._resolve_params(
                api.get("body_params", []), url=api["doc_url"]
            )
            path_needed = len(path_params) > 0
            query_needed = len(query_params) > 0
            body_needed = len(body_params) > 0
            need_datetime = any(
                param["type"] == "datetime" for param in path_params + query_params + body_params
            )
            normalized_apis.append(
                {
                    "method_name": re.sub(
                        r"^[^a-z0-9]+|[^a-z0-9]+$", "", re.sub(r"[^\w]+", "_", api["name"].lower())
                    ),
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
        return class_name, normalized_apis
