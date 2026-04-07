PYTHON ?= python3
PACKAGE = ops_manager_sdk

.PHONY: help install install-dev lint clean

help:
	@echo "Available targets:"
	@echo "  install      Install runtime dependencies"
	@echo "  install-dev  Install package with development dependencies"
	@echo "  lint         Run pylint on source and tests"
	@echo "  clean        Remove Python build artifacts"

install:
	$(PYTHON) -m pip install -e .

install-dev:
	$(PYTHON) -m pip install -e .[dev]

lint:
	$(PYTHON) -m pylint src/$(PACKAGE) tests

clean:
	find . -type d \( -name __pycache__ -o -name .pytest_cache -o -name .mypy_cache \) -prune -exec rm -rf {} +
	find . -type d -name '*.egg-info' -prune -exec rm -rf {} +
	find . -type f \( -name '*.pyc' -o -name '*.pyo' \) -delete
	rm -rf build dist
