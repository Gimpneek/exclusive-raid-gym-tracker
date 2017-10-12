# Contributing to this repo
Pull Requests, Issues and just general feedback is very much welcome.

## Contributing code
[![Build Status](https://travis-ci.org/Gimpneek/exclusive-raid-gym-tracker.svg?branch=master)](https://travis-ci.org/Gimpneek/exclusive-raid-gym-tracker)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/82888cd32269446181395bc5a745edb7)](https://www.codacy.com/app/colin-wren/exclusive-raid-gym-tracker?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Gimpneek/exclusive-raid-gym-tracker&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/82888cd32269446181395bc5a745edb7)](https://www.codacy.com/app/colin-wren/exclusive-raid-gym-tracker?utm_source=github.com&utm_medium=referral&utm_content=Gimpneek/exclusive-raid-gym-tracker&utm_campaign=Badge_Coverage)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Documentation Status](https://readthedocs.org/projects/exclusive-raid-gym-tracker/badge/?version=latest)](http://exclusive-raid-gym-tracker.readthedocs.io/en/latest/?badge=latest)

To ensure the quality of the code in this repository the master branch requires
the Travis and Codacy checks must pass in order to merge in a Pull Request.

That being the case if you're looking to contribute it may be worth signing up
for these services (they're free, just login with your Github account) to save
any issues on submitting your Pull Request.

### Documentation
Documentation for the project can be found on [ReadTheDocs](http://exclusive-raid-gym-tracker.readthedocs.io/en/latest/).

### Testing
Unit, Integration and end-to-end testing is part of the development cycle when
building this project.

You can run the unit and integration tests using the following command:
`python manage.py test app`

You can run the end-to-end tests using the following command once you've
installed the `behave-django` dependency:
`python manage.py behave`

### Code Style
To ensure code quality and style both PyLint and Flake8 are run against the
codebase.

You can run these using the following commands:

- `pylint --load-plugins pylint_django app`
- `flake8 app`

## Submitting Feedback
If you've got any ideas of how to improve the tracker, issues that you've
encountered using it or general questions feel free to create an issue.
