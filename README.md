# URL Prober

A Python tool for network infrastructure probing and diagnostics.

## Running the Application

### Prerequisites
- Python 3.9 or higher
- Poetry (Python package manager)

### Installation

1. Clone the repository:
```bash
# Using HTTPS
git clone https://github.com/av603/url-prober.git

# OR using SSH
git clone git@github.com:av603/url-prober.git

cd url-prober
```

2. Install with Poetry:
```bash
poetry install
```

### Starting the Server

Basic usage:
```bash
poetry run url-prober serve
```

The server will start with default settings:
- Host: 127.0.0.1 (localhost only)
- Port: 5000
- Debug mode: off

### Custom Configuration

You can customize the server settings:

```bash
# Run on a different port
poetry run url-prober serve --port 8080

# Make accessible from other machines
poetry run url-prober serve --host 0.0.0.0

# Enable debug mode (auto-reload on code changes)
poetry run url-prober serve --debug

# Combine options
poetry run url-prober serve --host 0.0.0.0 --port 8080 --debug
```

### Available Endpoints

- Health Check: `http://127.0.0.1:5000/health`
  - Returns: `{"status": "healthy"}`

## Development Setup

### Pre-commit Hooks

1. Install the pre-commit hooks:
```bash
poetry run pre-commit install
```

### Code Style

The project enforces code quality through pre-commit hooks:
- Black for code formatting
- isort for import sorting
- flake8 for linting:
  - Maximum line length: 79 characters (PEP 8)
  - Maximum complexity: 10
  - Docstring checks enabled
- Basic file checks (trailing whitespace, YAML syntax, etc.)

These checks run automatically on commit. To run manually:
```bash
poetry run pre-commit run --all-files
```

### Editor Configuration

The project includes an `.editorconfig` file to maintain consistent coding styles:
- UTF-8 encoding
- Unix-style line endings
- 4 spaces for Python indentation
- 79 character line length for Python files
- 2 spaces for YAML files

## Testing

Run the test suite:
```bash
poetry run pytest
```

With coverage report:
```bash
poetry run pytest --cov=src/
```

### Managing Lock File

1. Update lock file without installing packages:
```bash
poetry lock --no-update
```

2. Update lock file and install packages:
```bash
poetry lock
```

3. Check if lock file is up to date with pyproject.toml:
```bash
poetry lock --check
```

4. Force update lock file (if you're having issues):
```bash
poetry lock --no-cache
```

Note: The lock file (`poetry.lock`) ensures that all developers use the exact same package versions. Always commit this file to version control.

## Contributing

Please see [Contributing Guidelines](CONTRIBUTING.md) for details on:

- Setting up your development environment
- Code style and standards
- Pull request process
- Running tests

# Versioning

This project follows [Semantic Versioning](https://semver.org/). For the versions available, see the [tags on this repository](https://github.com/av603/url-prober/tags).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
