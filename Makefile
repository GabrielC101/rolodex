TEST_PATH=./tests
VENV_BIN = venv/bin/

# These variables identify cli executables in the virtual environment
PIP = ${VENV_BIN}pip
PIP_INSTALL = ${VENV_BIN}pip-install
PIP_SYNC = ${VENV_BIN}pip-sync
PIP_COMPILE = ${VENV_BIN}pip-compile
PYTHON = ${VENV_BIN}python
PYTEST = ${VENV_BIN}pytest
DMYPY = ${VENV_BIN}dmypy
PROSPECTOR = ${VENV_BIN}prospector
ISORT = ${VENV_BIN}isort
ACTIVATE = ${VENV_BIN}activate


SHELL := /bin/bash

activate:
	source ${ACTIVATE}


# These can be run from anywhere

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force {} +

clean: clean-pyc
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info
	rm --force --recursive *.egg
	rm --force --recursive .mypy_cache/
	rm --force --recursive docs/_build/
	rm --force --recursive .cache
	rm --force --recursive .coverage
	rm --force --recursive .tox
	rm --force --recursive .pytest_cache
	find . -name '__pycache__' -exec rm --recursive --force {} +
	find . -name '*.log' -exec rm --force {} +

pip-base:
	${PIP} install -U pip
	${PIP} install pip-tools

# Update requirement-*.txt files with latest versions of dependencies.
pip-update: pip-base
	${PIP_COMPILE} -U -o requirements/requirements.txt requirements/requirements.in
	${PIP_COMPILE} -U -o requirements/requirements-dev.txt requirements/requirements-dev.in

# Sync virtualenv with versions specified in requirements files.
pip-sync:
	${PIP_SYNC} requirements/requirements-dev.txt

# Install development tools
pip-dev:
	${PIP} install ipython

# Run tests using local virtual environment
local-test: clean-pyc
	${PYTEST} -vv --color=yes $(TEST_PATH)

# Run linter on code. Programming equivalent of spell-checker. Helpful, but not always right.
# Runs mypy, prospector, and isort.
lint:
	@echo 'Checking type annotations with Mypy'
	${DMYPY} start -- --follow-imports=skip --ignore-missing-imports
	${DMYPY} check . ; true
	${DMYPY} stop
	@echo
	@echo 'Static file linting with Prospector'
	${PROSPECTOR} -M ; true
	@echo 'Check import order with isort'
	${ISORT} -df -q 2> /dev/null | cut -d ':' -f 1 ; true

# Run main program using local virtual environment
local-run:
	@rm -f data.json
	${PYTHON} ./main.py
	@cat data.json

# Initialize local virtual environment
local-init:
	@echo 'starting init'
	@rm -rf venv
	@mkdir venv
	@python3 -m venv venv
	${VENV_BIN}pip install -U pip
	${VENV_BIN}pip install pip-tools
	${VENV_BIN}pip-sync requirements/requirements-dev.txt


# Docker related targets

# Builds main docker application
docker-build-application: clean
	@docker build -t "rolodex:latest" -f dockerfiles/Dockerfile .

# Builds docker application to run tests
docker-build-test: clean
	@docker build -t "rolodex-test:latest" -f dockerfiles/DockerfileTest .

docker-build: docker-build-application docker-build-test

# Runs main docker application
docker-run-application:
	@docker run -it rolodex

# Runs docker test application.
docker-run-test:
	@docker run -it "rolodex-test:latest"

docker-run: docker-run-test docker-run-application

# The following targets are intended to be run from the Docker image.

# Runs main application using system Python executable
run-no-venv:
	@python3 main.py
	@cat data.json

# Runs tests using system Pytest executable
test-no-venv:
	@pytest -vv --color=yes tests

# All targets in this Makefile are phony, that is, they don't correspond to a build target file
# Python Makefiles generally only use phony targets. Non-phony files don't serve any Python related purpose.
.PHONY: clean test-no-venv run-no-venv docker-run-test docker-run-application docker-build-test \
docker-build-application local-init local-run lint local-test pip-dev pip-sync pip-update pip-base clean \
clean-pyc