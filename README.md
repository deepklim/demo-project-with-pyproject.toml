# demo-project-with-pyproject.toml
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyCQA: flake8](https://img.shields.io/badge/PyCQA-flake8-brightgreen)](https://flake8.pycqa.org/)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

Demo Python distribution package using pyproject.toml. Incorporates common CI tools.

## Steps for setting up a local development environment
### Required software
- [Python 3.10](https://www.python.org/downloads/release/python-31011/)

### Initial setup
1. Clone the repo and navigate into its directory
1. Create and activate a virtual environment
	- `python -m venv venv`
	- `. venv/Scripts/activate`
1. Install development dependencies into the virtual environment
    - `python -m pip install -U pip`
	- `pip install -r requirements-dev.txt`
1. Install the package in editable mode
	- `pip install -e .`

### Running CI tools
1. [black](https://github.com/psf/black), to check code formatting
	- `black --check --diff .`
1. [flake8](https://flake8.pycqa.org/), to lint
	- `flake8 .`
1. [isort](https://pycqa.github.io/isort/), to check sort order of imports
	- `isort --check --diff .`
1. [mypy](https://mypy-lang.org/), to check type hints
	- `mypy .`

### Running unit tests
- `python -m unittest discover -s tests/`
#### With coverage&#46;py
- `coverage run -m unittest discover -s tests/`
- `coverage html`

### Building the package
- `python -m build`
