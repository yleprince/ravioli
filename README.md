# ravioly :spaghetti:

![](https://github.com/yleprince/ravioly/workflows/Python%20CI/badge.svg)


## Context 
The goal is to have a production ready code to analyse New York taxi data.

Ravioly is a way to encapsulate the raw data contained in NYC taxi csv files. As mentionned in the documentation (https://yleprince.github.io/ravioly/) it is built on top of `pandas.DataFrame` and provide specific processing functionalities and dedicated methods.

## Install and Use:

```sh
```

## Tools used:
* **`Dev`**:
  * [pandas](https://pandas.pydata.org/): the code is a subclass of pandas.DataFrame data structure.
  * [poetry](https://python-poetry.org/): package management is made with poetry
  
* **`Lint`**:
  * [isort](https://pypi.org/project/isort/): to sort the imports
  * [mypy](http://mypy-lang.org/): to check the use of types within the code
  * [black](https://pypi.org/project/black/): to format automatically the code with the pep8 requirements
  * [flake8](https://gitlab.com/PyCQA/flake8): to check code syntax

* **`Tests`**:
  * [pytest](https://docs.pytest.org/en/latest/): to unit test the code
  * [pytest-cov](https://pypi.org/project/pytest-cov/): to check percentage of code covered by the tests

* **`CI`**:
  * [github actions](https://github.com/features/actions): to maintain code consistency over commits.

* **`Documentation`**:
  * [sphinx](https://www.sphinx-doc.org/en/master/): automatically generate the documentation from source code.
  * [read the doc theme](https://sphinx-rtd-theme.readthedocs.io/): theme for the documentation

* **`Bonus`**:
  * [pre-commit](https://pre-commit.com/): pre-commit allows to run lint and tests workflow automatically at every step of the project
  * [pre-push](https://www.git-scm.com/docs/githooks#_pre_push): pre-push allows to update the documentation every time the code is pushed on the github.
 
