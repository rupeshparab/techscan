[![License: MIT](https://img.shields.io/github/license/vintasoftware/django-react-boilerplate.svg)](LICENSE.txt)

# TechScan

## About
Project has been hosted at https://cast-techscan.herokuapp.com/
Data can be entered from https://cast-techscan.herokuapp.com/crud

Please follow the instructions in Setup and Running the project

## Running
### Setup
- On project root, do the following:
- Run the migrations:  
  `python manage.py migrate`

### Running the project
- `pip install -r requirements.txt`
- `npm install`
- `npm run start`
- `python manage.py runserver`

### Testing
`make test`

Will run django tests using `--keepdb` and `--parallel`. You may pass a path to the desired test module in the make command. E.g.:

`make test someapp.tests.test_views`

### Adding new pypi libs
Add high level dependecies to `requirements-to-freeze.txt` and `pip freeze > requirements.txt`. This is [A Better Pip Workflow](http://www.kennethreitz.org/essays/a-better-pip-workflow).

## Linting
- Manually with `prospector` and `npm run lint` on project root.
- During development with an editor compatible with prospector and ESLint.

## Pre-commit hooks
- Run `pre-commit install` to enable the hook into your git repo. The hook will run automatically for each commit.
- Run `git commit -m "Your message" -n` to skip the hook if you need.

[MIT License](LICENSE.txt)
