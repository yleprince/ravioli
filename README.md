# ravioly :spaghetti:

[![](https://img.shields.io/badge/linkedin-connect-9cf?&logo=linkedin)](https://www.linkedin.com/in/yrieix.leprince)
![](https://img.shields.io/github/license/yleprince/ravioly.svg?color=9cf)
![](https://img.shields.io/github/languages/top/yleprince/ravioly.svg)

![](https://github.com/yleprince/ravioly/workflows/Python%20CI/badge.svg)
![](https://img.shields.io/github/last-commit/yleprince/ravioly.svg)
![](https://img.shields.io/github/commit-activity/y/yleprince/ravioly)

![](https://img.shields.io/github/issues-pr-closed-raw/yleprince/ravioly.svg)
![](https://img.shields.io/github/issues-closed-raw/yleprince/ravioly.svg)


## Context :car: :cityscape: :us:
The goal is to have a production ready code to analyse New York taxi data.

Ravioly is a way to encapsulate the raw data contained in NYC taxi csv files. As mentionned in the documentation (https://yleprince.github.io/ravioly/) it is built on top of `pandas.DataFrame` and provide specific processing functionalities and dedicated methods.

## Install and Use: :seedling:

:bulb: Python `^3.7` is required.

Install using `pip`:

```sh
pip install git+https://github.com/yleprince/ravioly.git
```

In your python code:

```python
>>> from ravioly.datastructure import Ravioly

>>> df = Ravioly('../data/nyc_data.csv', nrows=1000)
>>> df.km_by_dow()

day_of_week
0    480.647876
1    466.137703
2    553.287868
3    427.187865
4    465.982398
5    489.352866
6    557.113716
Name: km_by_dow, dtype: float64
```

## Tools used: :gear:
* **`Dev`**: :computer:
  * [pandas](https://pandas.pydata.org/): the code is a subclass of pandas.DataFrame data structure.
  * [poetry](https://python-poetry.org/): package management is made with poetry
  
* **`Lint`**: :triangular_ruler: 
  * [isort](https://pypi.org/project/isort/): to sort the imports
  * [mypy](http://mypy-lang.org/): to check the use of types within the code
  * [black](https://pypi.org/project/black/): to format automatically the code with the pep8 requirements
  * [flake8](https://gitlab.com/PyCQA/flake8): to check code syntax

* **`Tests`**: :teacher:
  * [pytest](https://docs.pytest.org/en/latest/): to unit test the code
  * [pytest-cov](https://pypi.org/project/pytest-cov/): to check percentage of code covered by the tests

* **`CI`**: :robot:
  * [github actions](https://github.com/features/actions): to maintain code consistency over commits.

* **`Documentation`**: :books: 
  * [sphinx](https://www.sphinx-doc.org/en/master/): automatically generate the documentation from source code.
  * [read the doc theme](https://sphinx-rtd-theme.readthedocs.io/): theme for the documentation
  * [github pages](https://pages.github.com/): to serve the documentation: https://yleprince.github.io/ravioly/

* **`Bonus`**: :gift: 
  * [pre-commit](https://pre-commit.com/): pre-commit allows to run lint and tests workflow automatically at every step of the project
  * [pre-push](https://www.git-scm.com/docs/githooks#_pre_push): pre-push allows to update the documentation every time the code is pushed on the github.
 
