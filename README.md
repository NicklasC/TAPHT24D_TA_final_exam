# TAP_HT24_Test tools final exam

This repo contains code for the final exam of the TAPHT24D Test tools course.

The assignment is to test the site located at https://tap-ht24-testverktyg.github.io/exam-template/

For more detailed information regarding the assignment, see links and information in the ASSIGNMENT_INFO.md file.

## To run the tests, see instruction in the "Auto installation" chapter below

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

#### Auto installation

Checkout the repo and install dependencies according to dependencies.txt
If you do not, you can do the dependency installation manually as below:

Note that You MIGHT need to do the `playwright install` command after installing using dependencies.txt

Then to run the tests use `behave .\tests\features\`, or in PyCharm right-click tests/features folder and select run
features

#### Manual installation

(setup .venv)

in terminal:

`pip install playwright`

`playwright install` (installs browser binaries)

`pip install behave`

`pip install pytest-playwright` (This also installs pytest, which is a dependency to pytest-playwright)

## Good to have command

Command below gives a nice gui to get ideas of identifiers

playwright codegen https://lejonmanen.github.io/agile-helper/



