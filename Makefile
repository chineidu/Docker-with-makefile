.PHONY: setup-venv setup clean-pyc clean-test test mypy lint checks

setup-venv: # Create virtual env. You have to run this first!
	python3 -m venv .venv && . .venv/bin/activate
	pip install --upgrade pip
	pip install -r test_requirements.txt

setup:  # fastapi_app is the tag. you can rename it
	DOCKER_BUILDKIT=1 docker build -t fastapi_app -f Dockerfile .

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -f .coverage.*
	find . -name '.pytest_cache' -exec rm -fr {} +

clean: clean-pyc clean-test
	find . -name '.my_cache' -exec rm -fr {} +
	rm -rf logs/

test: clean # src is the source code
	. .venv/bin/activate && py.test tests -v --cov=src \
	--cov-report=term-missing --cov-fail-under 80

mypy:
	. .venv/bin/activate && mypy src

lint:
	. .venv/bin/activate && black src && isort src

checks: test lint mypy clean
