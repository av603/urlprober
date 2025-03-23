# url-prober
Requests a specified `url` and returns the response. Used for network infrastructure probing and diagnostics.

## Development Setup

### Prerequisites
- Python 3.9 or higher
- Poetry (Python package manager)

### Installation

1. Install Poetry if you haven't already:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Install dependencies:
```bash
poetry install
```

### Pre-commit Hooks

We use pre-commit hooks to ensure code quality. To set up:

1. Install the pre-commit hooks:
```bash
poetry run pre-commit install
```

2. (Optional) Run hooks against all files:
```bash
poetry run pre-commit run --all-files
```

To skip pre-commit hooks temporarily:
```bash
git commit -m "Your message" --no-verify
```

### Development Commands

- Run tests:
```bash
poetry run pytest
```

- Run linting:
```bash
poetry run flake8
```

- Run the tool:
```bash
poetry run url-prober <url>
```

### Building and Publishing

1. Build the package:
```bash
poetry build
```

2. Publish to PyPI (requires appropriate credentials):
```bash
poetry publish

```

### Code Style

The project uses flake8 for linting with the following configuration:
- Maximum line length: 79 characters (PEP 8 standard)
- Maximum complexity: 10
- Ignores E203 (whitespace before ':') to work with Black
- Excludes common directories and allows unused imports in `__init__.py` files

To run linting manually:
```bash
poetry run flake8
```
