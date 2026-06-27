PYTHON ?= python3
PACKAGE = ops_manager_sdk
VENV = .venv
VENV_PYTHON = $(VENV)/bin/python

.PHONY: help venv install install-dev crawl recrawl pygen reset lint format-resources clean

help:
	@echo "Available targets:"
	@echo "  venv         Create the local virtual environment"
	@echo "  install      Install runtime dependencies"
	@echo "  install-dev  Install package with development dependencies"
	@echo "  crawl        Crawl API docs and write .data/api_docs.json and .data/normalized_api_docs.json"
	@echo "  recrawl      Crawl all API docs and replace .data/api_docs.json"
	@echo "  pygen        Generate Python SDK code from .data/normalized_api_docs.json"
	@echo "  reset        Set statuses for one api_docs.json key to 404: make reset KEY=<key>"
	@echo "  lint         Run pylint on source and tests"
	@echo "  format-resources  Format all Python files under resources"
	@echo "  clean        Remove Python build artifacts"

venv:
	@if [ ! -x "$(VENV_PYTHON)" ]; then $(PYTHON) -m venv $(VENV); fi
	$(VENV_PYTHON) -m pip install --upgrade pip

install: venv
	$(VENV_PYTHON) -m pip install -e .

install-dev: venv install
	$(VENV_PYTHON) -m pip install -e .[dev]
	$(VENV_PYTHON) -m playwright install chromium

crawl:
	$(VENV_PYTHON) -m ops_manager_sdk.generator crawl

recrawl:
	FORCE_CRAWL=1 $(VENV_PYTHON) -m ops_manager_sdk.generator crawl

pygen:
	$(VENV_PYTHON) -m ops_manager_sdk.generator pygen

reset:
	@test -n "$(KEY)" || ( echo "Usage: make reset KEY=<api_docs_key>"; exit 1 )
	$(VENV_PYTHON) -m ops_manager_sdk.generator reset "$(KEY)"

lint: venv
	$(VENV_PYTHON) -m pylint src/$(PACKAGE) tests

format-resources: venv
	$(VENV_PYTHON) -m black pyomsdk/src/pyomsdk/

clean:
	find . -type d \( -name __pycache__ -o -name .pytest_cache -o -name .mypy_cache \) -prune -exec rm -rf {} +
	find . -type d -name '*.egg-info' -prune -exec rm -rf {} +
	find . -type f \( -name '*.pyc' -o -name '*.pyo' \) -delete
	rm -rf build dist
