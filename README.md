# Bioinformatics Cookiecutter


This repository provides a template that incorporates best practices to create a maintainable and reproducible bioinformatics project.

## Tools used in this project
 - [conda](#) for environment management
 - [poetry](#) for dependency management
 - [git](#) for Code Version Control
 - [pdoc](#) for project documentation
 - [snakemake](#) to manage configuration files
 - [DVC](#) for Data Version Control
 
 ## Project Structure

```bash
.
├── .flake8                         # complement for linting
├── .gitignore                      # ignore files that cannot commit to Git
├── .pre-commit-config.yaml         # complement for installing pre-commit tools
├── config                      
│   ├── main.yaml                   # Main configuration file
│   └── process                     # Configurations for processing data
├── data            
│   ├── processed                   # data after processing
│   ├── raw                         # raw data
│   ├── raw.dvc                     # DVC file of data/rawa
│   └── results                     # data results
├── docs                            # documentation for your project
├── environment.yaml                # conda environment file
├── Makefile                        # store useful commands to set up the environment
├── notebooks                       # store notebooks
├── pyproject.toml                  # dependencies for poetry
├── README.md                       # describe your project
├── reports                         # store reports
├── setup.py                        # setup script
├── src                             # store source code
│   ├── __init__.py                 # make src a Python module 
│   ├── helpers                     # helpers functions folder
│   └── main.py                     # main analysis
├── test_environment.py             # script to test environment
└── tests                           # should mirror src  
```

## How to use this project

Install Cookiecutter using an environment:
```bash
pip install cookiecutter
```

```bash
conda install cookiecutter
```

```bash
poetry install cookiecutter
```

Create a project based on the template:
```bash
cookiecutter https://github.com/rgalindor/bioinfocutter --checkout main
```
