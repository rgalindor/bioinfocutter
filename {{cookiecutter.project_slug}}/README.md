# {{ cookiecutter.project_title }}

{{ cookiecutter.description }}

By: {{ cookiecutter.author }}

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

## Getting started

**Before you start**

- Get sure you have `python` with a version {{ cookiecutter.python_version }}, if you want to start from fresh take a look at [this resource](https://wiki.python.org/moin/BeginnersGuide/Download).
- Install `poetry` by following the reccomended instructions in [the oficial documentation](https://python-poetry.org/docs/#installation)


Make sure have installed:
 - `conda`
 - `cookiecutter`
 - `make`

Init your project by:

```bash
make init
make create_environment
conda activate {{ cookiecutter.project_slug }}
make env
```

### Alternatives


```bash
curl -sSL https://install.python-poetry.org | python3 -
```

To install all the dependencies of this project use

```bash
poetry install
```

To install any other dependency type

```bash
poetry add <package-name>[@<version>]
```



## Contact info

[{{ cookiecutter.author }}](mailto:{{ cookiecutter.git_email }})