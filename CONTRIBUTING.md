# Contributing to URL Prober

This document provides guidelines and steps for contributing.

## Development Setup

1. Fork the repository and clone your fork:
```bash
# Using SSH (recommended)
git clone git@github.com:your-username/url-prober.git

# OR using HTTPS
git clone https://github.com/your-username/url-prober.git

cd url-prober
```

2. Install dependencies with Poetry:
```bash
poetry install
```

3. Install pre-commit hooks:
```bash
poetry run pre-commit install
```

## Code Style

This project uses several tools to maintain code quality:
- Black for code formatting
- isort for import sorting
- flake8 for linting with PEP 8 standards
- pre-commit hooks for automated checks

To run all checks manually:
```bash
poetry run pre-commit run --all-files
```

## Making Changes

1. Create a new branch:
```bash
git checkout -b feature-or-fix-name
```

2. Make your changes and ensure all tests pass:
```bash
poetry run pytest
```

3. Commit your changes:
```bash
git add .
git commit -m "Description of changes"
```

Your commit will automatically trigger pre-commit hooks to check code quality.

4. Push to your fork:
```bash
git push origin feature-or-fix-name
```

5. Open a Pull Request on GitHub

## Pull Request Guidelines

- Fill in the provided PR template
- Include tests for new features
- Update documentation as needed
- Ensure all checks pass
- Keep PRs focused - one feature or fix per PR

## Running Tests

```bash
# Run all tests
poetry run pytest

# Run with coverage report
poetry run pytest --cov=src/
```

## Getting Help

If you have questions or need help:
1. Check existing issues
2. Open a new issue
3. Reach out to maintainers

## License

By contributing, you agree that your contributions will be licensed under the MIT License. See the [LICENSE](LICENSE) file for full details.
