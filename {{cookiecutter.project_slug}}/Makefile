.PHONY: tests docs env init create_environment test_environment

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = {{ cookiecutter.project_slug }}

ifeq (,$(shell which conda))
HAS_CONDA=False
else
HAS_CONDA=True
endif

CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate

# use this function to load modules on the cluster
# usage in Makefile: $(call module-load,snakemake) && snakemake -j1 ...
define module-load
        eval `/usr/bin/modulecmd bash load $(1)`
endef


#################################################################################
# COMMANDS                                                                      #
#################################################################################

init: 
	@echo "Installing dependencies..."
	curl -sSL https://install.python-poetry.org | python3 -
	poetry --version

env: 
	@echo "Activating virtual environment..."
	#conda activate $(PROJECT_NAME)
	poetry install
	poetry run pre-commit install

conda_update: env
	@echo "Updating environment file"
	conda env update --file environment.yaml --prune

poetry_env: env
	@echo "Activating poetry ..."
	poetry shell

tests:
	pytest

docs:
	@echo Save documentation to docs... 
	pdoc src -o docs --force
	@echo View API documentation... 
	pdoc src --http localhost:8080

## Set up python interpreter environment
create_environment:
ifeq (True,$(HAS_CONDA))
	@echo ">>> Detected conda, creating conda environment."
	conda env create -f environment.yaml
	@echo ">>> New conda env created. Activate with: "
	@echo "conda activate $(PROJECT_NAME)"

else
	@echo "Error: conda not detected. Exiting. "
	exit 1
endif

## Test python environment is setup correctly
test_environment:
	eval "$(conda shell.bash hook)"
	conda activate $(PROJECT_NAME)
	python3 test_environment.py




.PHONY: help
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')