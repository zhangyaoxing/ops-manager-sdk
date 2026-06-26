from ops_manager_sdk.generator.pycode_gen import gen_resource_code


def test_gen_resource_code_emits_raw_docstrings_for_markdown_escapes(tmp_path, monkeypatch) -> None:
    output_dir = tmp_path / "pyomsdk/src/pyomsdk/resources"
    output_dir.mkdir(parents=True)
    monkeypatch.chdir(tmp_path)

    gen_resource_code(
        "ExampleResource",
        [
            {
                "need_datetime": False,
                "params_class_name": "Example",
                "method_name": "get_example",
                "verb": "GET",
                "path": "/example/{name}",
                "path_params": {
                    "required": True,
                    "needed": True,
                    "params": [
                        {
                            "name": "name",
                            "type": "str",
                            "required": True,
                            "default": None,
                            "alias": "name",
                            "description": r"Use literal\_underscore.",
                        }
                    ],
                },
                "query_params": {"required": False, "needed": False, "params": []},
                "body_params": {"required": False, "needed": False, "params": []},
                "body_type": "object",
                "doc": r"Method docs with literal\_underscore.",
            }
        ],
    )

    generated = (output_dir / "example_resource.py").read_text(encoding="utf-8")

    assert "r\"\"\"Use literal\\_underscore." in generated
    assert "r\"\"\"Method docs with literal\\_underscore." in generated
