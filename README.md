# TAP_HT24_Test tools final exam

This repo contains code for the final exam of the TAPHT24D Test tools course.

The assignment is to test the site located at https://tap-ht24-testverktyg.github.io/exam-template/

For more detailed information regarding the assignment, see links and information in the ASSIGNMENT_INFO.md file.

## Technology used

* Python
* Playwright
* Pytest
* Behave
* Code is using Page Object Model

## Steps to setup project from scratch (For my own personal use)

### Setup folder structure

Create folder structure:

- tests/features

- tests/pages

- tests/steps

### Setup environment and .gitignore

environment.py and .gitignore (as per this project)

### Setup and install dependencies

(setup .venv)

in terminal:

`pip install playwright`

`playwright install` (installs browser binaries)

`pip install behave`

`pip install pytest-playwright` (This also installs pytest, which is a dependency to pytest-playwright)

## Good to have commands

Command below gives a nice gui to get ideas of identifiers

playwright codegen https://lejonmanen.github.io/agile-helper/



