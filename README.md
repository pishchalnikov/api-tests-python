# api-tests-python

Examples for API Testing with Python

[![CircleCI](https://circleci.com/gh/pishchalnikov/api-tests-python.svg?style=svg)](https://circleci.com/gh/pishchalnikov/api-tests-python)

Requirements:
* python3.8
* virtualenv

Prepare venv:
```bash
$ virtualenv --python=python3.8 venv
$ source venv/bin/activate
```

Install dependencies:
```bash
$ pip install -r requirements.txt
```

Run tests:
```bash
$ pytest tests/
```

Run tests in Docker:
```bash
$ docker build --tag api-tests-python .
$ docker run api-tests-python
```
