# URL Prober

This tool helps test complex cloud network setups, like those with private services that have specific exit points. It's especially useful for checking if your cloud services can talk to each other within a virtual private cloud and those services can make requests to the outside world as expected.

**Use Case** Say you have a Cloud Load Balancer, two Cloud Run services (Service A and Service B) and a Cloud Subnetwork with a static egress IP. You have deployed this infrastructure and want to verify that the Cloud Load Balancer can access Service A, that Service A can access Service B and that requests from Service B appear from the subnetwork static egress IP.

```
                                      Internet
                                          |
                                          |
                                      +-------+
                                      |       |
                                      | Cloud |
                                      |  Run  |  (A) - Publicly Accessible
                                      +-------+
                                          | (Target URL Parameter)
                                          |
                                          v (Internal Network Traffic)
                                      +-------+
                                      |       |
                                      | Cloud |
                                      |  Run  |  (B) - Internal Service
                                      +-------+
                                          | (Outbound Request via Static IP)
                                          |
                                          v
                                      +---------------+
                                      | External      |
                                      | Target Server |
                                      +---------------+
```

The network connectivity and the public IP can be verified by deploying the `url-prober` tool to Service A and Service B and sending a chained `curl` request to the exposed service and requesting the public IP from `https://api.ipify.org` as the last step in the chain. For example, if the network is configured as per this use case, a `curl` request:

```bash
curl -s http://external-cloud-run-service-a-ip/?url=http://internal-cloud-run-service-b-ip/?url=https://api.ipify.org?format=json
```

will be received at Service A, then at Service B and finally at `https://api.ipify.org` will return the public IP.

## Installation

The `url-prober` tool is available on PiPy and can be installed via pip:

1.  **Install Python 3.9+:** Ensure you have Python 3.9 or a later version installed.
2.  **Install the package via pip:**

    ```bash
    pip install url-prober
    ```

How you deploy the `url-prober` tool depends on the type of infrastructure under test e.g. packaged as a `Docker` image or deployed as a cloud function.

## Usage

### Running as a standalone application

1.  **Run the server:**

```bash
python -m url_prober --host 0.0.0.0 --port 5000
```

2.  **Send a GET request to the server with the `url` parameter:**

    ```bash
    curl -s "http://<edge-service-ip>:5000/?url=https://<internal-service-ip>"
    ```

    Replace `<edge-service-ip>` with the IP address or hostname of your externally accessible edge service.

## Output

The server will return a JSON object containing detailed information the request chain, including:

* **Edge Service Response:** Status code, headers, and body from the target service."
* **Error Messages:** Detailed error messages for any failures encountered during the request chain.

## Development Setup

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
