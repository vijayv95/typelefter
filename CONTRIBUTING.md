# -----------------------------------------------------------------------------
# Typelefter - Free and Open Source Novel Writing Application
# Copyright (C) 2025 Vijay Vasudevan, Bangalore, India
# Started: 09-10-2025
#
# This file is part of Typelefter.
#
# Typelefter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Typelefter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Typelefter.  If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.
# -----------------------------------------------------------------------------

# Contributing to Typelefter

Thank you for your interest in contributing to Typelefter --- a free and
open-source novel-writing application built with Python, PySide6, and
optional C++ modules via pybind11. This document describes how to
contribute code, report issues, and follow the established development
standards.

## Table of Contents

1.  Code of Conduct\
2.  Project Structure\
3.  Branching and Workflow\
4.  Development Setup\
5.  Running Tests\
6.  Coding Standards\
7.  Commit Guidelines\
8.  Pull Request Requirements\
9.  License Headers\
10. Opening Issues\
11. Contact

## 1. Code of Conduct

Contributors must maintain professionalism and respect toward others.
Harassment, discrimination, and hostile behavior are not tolerated.

## 2. Project Structure

    typelefter/
        ui/                 # PySide6 UI components
        core/               # Core logic
        cpp/                # C++ module (pybind11)
        scripts/            # Utility scripts (license, tooling)
    tests/                  # Pytest suite

Python 3.12+ is required. Poetry is used for environment and dependency
management.

## 3. Branching and Workflow

### Protected Branches

- main --- always stable and release-ready.\
- All meaningful development must occur on feature branches.\
- Direct pushes to main are not allowed.

### Workflow

1.  Create a feature branch:

        git checkout -b feature/my-change

2.  Implement changes and add tests.

3.  Follow code standards and ensure all pre-commit hooks pass.

4.  Commit using conventional commits.

5.  Open a Pull Request targeting main.

## 4. Development Setup

### Prerequisites

- Python \>= 3.12
- Poetry
- CMake and build-essential (for C++ compilation)
- pre-commit

### Setup

```bash
git clone https://github.com/<your-username>/typelefter.git
cd typelefter
poetry install
pre-commit install
```

## 5. Running Tests

Tests use Pytest:

```bash
poetry run pytest --cov=typelefter
```

All tests must pass before submitting a PR.

## 6. Coding Standards

### Python

- Formatted with Black
- Imports sorted with isort
- Linting with flake8 + flake8-bugbear
- Type checking with mypy
- No emojis are allowed in any source file

Manual commands:

```bash
poetry run black .
poetry run isort .
poetry run flake8 .
poetry run mypy typelefter
```

### C++

- clang-format is required and enforced via pre-commit

## 7. Commit Guidelines

Commitizen enforces Conventional Commits. Examples:

    feat: add project tree UI
    fix: handle empty workspace load crash
    docs: update contributor documentation
    chore: update dependencies
    test: add parser unit tests

Commit messages must be: - concise - meaningful - scoped only to the
change made

## 8. Pull Request Requirements

A PR must satisfy the following to be accepted:

- Targets main
- All GitHub Actions checks pass
- All code formatted according to Python and C++ rules
- License headers present in all source files
- Tests included for new or modified functionality
- No unrelated or sweeping changes
- No emojis present in code or documentation
- PR description clearly explains:
  - the problem addressed
  - the implementation summary
  - any limitations

Small, focused PRs are preferred.

## 9. License Headers

All source files must contain the project's GPLv3 license header.\
This is enforced via pre-commit:

    id: add-license-headers
    entry: python scripts/add_license_headers.py

If a file lacks a header, the hook will add it automatically.

## 10. Opening Issues

When filing an issue, include:

- Steps to reproduce
- Expected vs actual behavior
- OS and Python version
- Relevant logs or traceback

For feature requests: - describe the problem being solved - explain why
it benefits the project - keep the scope specific and actionable

## 11. Contact

For questions or design discussions, open an Issue or Discussion on
GitHub.\
Maintained by Vijay Vasudevan.
