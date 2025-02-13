##@ Utility

.PHONY: help
help: ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Project Commands

.PHONY: deps
deps: ## Download deps for venv
	@poetry install
	@poetry run pre-commit install

.PHONY: clean
clean: ## Remove temp files
	@rm -rf .venv poetry.lock

.PHONY: format
format: ## Format Project
	@poetry run black .

.PHONY: test
test: ## Run tests
	@pytest

