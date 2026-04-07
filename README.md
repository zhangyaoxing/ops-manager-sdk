# ops-manager-sdk

Python SDK skeleton for invoking Ops Manager REST APIs.

## Project layout

```text
.
├── Makefile
├── pyproject.toml
├── src/
│   └── ops_manager_sdk/
│       ├── client.py
│       ├── config.py
│       ├── exceptions.py
│       └── resources/
│           └── base.py
└── tests/
```

## Quick start

```bash
make install-dev
```

```python
from ops_manager_sdk import ClientConfig, OpsManagerClient

config = ClientConfig(
	base_url="https://example.ops-manager.local/api/v1",
	base_url="https://example.ops-manager.local/api/v1",
	digest_username="api-user",
	digest_password="api-password",
)

with OpsManagerClient(config) as client:
	projects = client.get("/projects")
	print(projects)
```

## Lint

```bash
make lint
```

## Next steps

- Add concrete resource modules under `src/ops_manager_sdk/resources/`
- Add test cases for authentication, error handling, and resource wrappers
- Add retries and backoff strategy for transient HTTP failures
