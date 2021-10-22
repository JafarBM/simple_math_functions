help:
	@echo "Please use \`make <ROOT>' where <ROOT> is one of"
	@echo "  dependencies         to install project dependencies"
	@echo "  test                 to run tests"
	@echo "  coverage             to get coverage report"
	@echo "  docker               to build docker image"
	@echo "  dev-deploy           to deploy on development environment"

dependencies:
	pip install --upgrade pip
	pip install -r requirements.txt

test:
	python3 -m pytest --disable-warnings

coverage:
	coverage run -m pytest --disable-warnings && coverage report

docker:
	$(DOCKER) build -t $(IMAGE_NAME):$(IMAGE_VERSION) .

dev-deploy:
	$(DOCKER) up $(IMAGE_NAME):$(IMAGE_VERSION)

.PHONY: help deploy

## Commons Vars ##########################################################
GIT ?= git
DOCKER ?= docker
COMMIT := $(shell $(GIT) rev-parse HEAD)
VERSION ?= $(shell $(GIT) describe --tag 2> /dev/null || echo "$(COMMIT)")
IMAGE_VERSION ?= $(VERSION)
IMAGE_NAME ?= calculator_developoment
