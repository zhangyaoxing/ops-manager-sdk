PYTHON ?= python3
PACKAGE = ops_manager_sdk
VENV = .venv
VENV_PYTHON = $(VENV)/bin/python

.PHONY: help venv install install-dev lint format-resources clean

help:
	@echo "Available targets:"
	@echo "  venv         Create the local virtual environment"
	@echo "  install      Install runtime dependencies"
	@echo "  install-dev  Install package with development dependencies"
	@echo "  lint         Run pylint on source and tests"
	@echo "  format-resources  Format all Python files under resources"
	@echo "  clean        Remove Python build artifacts"

venv:
	@if [ ! -x "$(VENV_PYTHON)" ]; then $(PYTHON) -m venv $(VENV); fi
	$(VENV_PYTHON) -m pip install --upgrade pip

install: venv
	$(VENV_PYTHON) -m pip install -e .

install-dev: venv
	$(VENV_PYTHON) -m pip install -e .[dev]
	$(VENV_PYTHON) -m playwright install chromium

lint: venv
	$(VENV_PYTHON) -m pylint src/$(PACKAGE) tests

format-resources: venv
	$(VENV_PYTHON) -m black pyomsdk/src/pyomsdk/

clean:
	find . -type d \( -name __pycache__ -o -name .pytest_cache -o -name .mypy_cache \) -prune -exec rm -rf {} +
	find . -type d -name '*.egg-info' -prune -exec rm -rf {} +
	find . -type f \( -name '*.pyc' -o -name '*.pyo' \) -delete
	rm -rf build dist
