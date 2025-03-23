"""Flask application module for URL Prober."""

import importlib.metadata
import logging
from pathlib import Path

import toml
from flask import Flask

DEFAULT_TIMEOUT = 10  # seconds
ALLOWED_METHODS = {"get", "post", "put", "delete"}
DEFAULT_MAX_REDIRECTS = 5
VERIFY_SSL = True

LOG = logging.getLogger(__name__)


def get_version() -> str:
    """Read version from pyproject.toml."""
    try:
        pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
        with open(pyproject_path, "r") as f:
            pyproject = toml.load(f)
            return pyproject["tool"]["poetry"]["version"]
    except Exception as e:
        LOG.warning(f"Failed to read version from pyproject.toml: {e}")
        return "unknown"


def health_check():
    """Check the health status and version of the service.

    Returns:
        dict: Health status and version information with format:
            {"status": "healthy", "version": "x.y.z"}
    """
    version = importlib.metadata.version("url-prober")
    return {"status": "healthy", "version": version}


def create_app():
    """Create and configure the Flask application.

    Returns:
        Flask: Configured Flask application instance
    """
    app = Flask(__name__)
    app.route("/health")(health_check)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
