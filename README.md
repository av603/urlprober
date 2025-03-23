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

1. Install pre-commit in your poetry environment:
```bash
poetry add --group dev pre-commit
```

2. Install the pre-commit hooks:
```bash
poetry run pre-commit install
```

3. (Optional) Run hooks against all files:
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
