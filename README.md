# FastAPI-Raw
A lightweight cookiecutter template for a FastAPI project that serves static HTML files.

## Overview
This project contains the basic structure of a FastAPI project including Unit Tests and a website template from [HTML5UP](https://html5up.net/). Nothing more and nothing less.

## Installation
You can install a cookiecutter template using different ways. The easiest is probably by referencing the Git repository directly.

```shell
cookiecutter gh:MauriceKuenicke/fastapi-raw
```
Cookiecutter will prompt you for a set of values that you need to define. Cookiecutter will then create the project based on your input. The values you'll need to set are:

```
- project_name > The name of your project
- project_version > The version you want to start with
- author > Your name
- use_website_template > Decision whether you want to have the website template or not.
```

## Running FastAPI
After you created your project, move into the new directory and create a virtual python environment.
```
cd <<project_name>>
python -m venv .venv
```
Install the dependencies after activating your environment
```
pip install -r requirements.txt
```
and start your local uvicorn server:
```
uvicorn app.main:app --reload
```
Your application should now be available on your ``localhost``. You can run the unit tests with
```
pytest tests -v --cov
```