#Contributing to Typelefter

We love contributions! By following this guide, you help keep Typelefter clean, consistent, and maintainable.

Table of Contents

Reporting Issues

Branch Naming

Commit Message Conventions

Making a Pull Request

Code Style and Linting

Tests

Reporting Issues

If you find a bug or have a feature request:

Check the existing issues
to see if it has already been reported.

Open a new issue with a descriptive title and detailed steps to reproduce, or describe the proposed feature.

Include relevant screenshots or logs if applicable.

Branch Naming

Use feature/topic-based branches that reference the issue number. For example:

feature/123-add-markdown-preview
fix/45-resolve-crash-on-startup
chore/dependencies-update

Branch types:

feature/ – new functionality

fix/ – bug fixes

chore/ – maintenance tasks, tooling updates, or dependency bumps

docs/ – documentation changes

test/ – adding or fixing tests

Do not commit directly to main or develop. Always create a branch from develop.

Commit Message Conventions

We use Conventional Commits
via Commitizen.

Commit format:

<type>[optional scope]: <short description>
[optional body]
[optional footer(s)]

Types:

feat: – a new feature

fix: – a bug fix

chore: – changes to build process, tooling, or dependencies

docs: – documentation changes

style: – code style changes (formatting, missing semi-colons, etc.)

refactor: – refactoring code without adding features or fixing bugs

test: – adding or updating tests

ci: – CI/CD related changes

Examples:

feat(editor): add markdown preview panel
fix(project): resolve crash when opening empty project
chore(ci): update GitHub Actions workflow
docs: add contributing guidelines

Breaking changes:
Include BREAKING CHANGE: in the body for any commit that introduces backward-incompatible changes.

Using Commitizen to Commit

Install Commitizen and use it to ensure messages are correct:

poetry run cz commit

Commitizen will prompt you for:

Type of change

Scope (optional)

Short description

Longer description (optional)

Any breaking changes

Issues closed (optional)

This ensures all commits follow the standard automatically.

Making a Pull Request

Fork the repo and create a branch based on develop.

Make your changes.

Run tests and linters locally.

Commit your changes using Commitizen or following the conventional commit style.

Push your branch to your fork.

Open a PR to develop and reference the issue number.

All PRs must pass CI (tests, linting, formatting) before they can be merged.

Code Style and Linting

We use Black for code formatting.

We use isort for import sorting.

We use flake8 + flake8-bugbear for linting.

Run locally before committing:

poetry run black typelefter tests
poetry run isort typelefter tests
poetry run flake8 typelefter tests

Tests

All new features must include tests.

Run tests locally before pushing:

poetry run pytest --cov=typelefter tests/

CI will run all tests for PRs automatically. Contributing to Typelefter

## Branches

- main = stable (release-ready)
- develop = optional integration branch
- Feature branches: feature/<name> (optional for experiments)
- Bugfix branches: bugfix/<name> (optional)

## Commits

Use Conventional Commits:

- feat: new feature
- fix: bug fix
- docs: documentation
- refactor: code change without feature
- test: add or update tests
- chore: maintenance
- style: code style changes
-

## Pull Requests

- Not required as a lone developer, but PRs can be used to trigger CI
- Ensure all tests pass before merging
