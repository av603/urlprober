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
