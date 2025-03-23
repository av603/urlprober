"""Flask application module for URL Prober."""

import importlib.metadata
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict

import requests
import toml
from flask import Flask, jsonify, request

from url_prober.utils import get_bool_from_arg, is_valid_url

# Configure logging at module level
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

DEFAULT_TIMEOUT = 10  # seconds
ALLOWED_METHODS = ["GET", "POST", "PUT"]
VERIFY_SSL = True


@dataclass
class Probe:
    """Probe data structure.

    Attributes:
        probe_url: URL that was probed
        probe_method: HTTP method used
        probe_timeout: Timeout for the request
        probe_verify: Whether to verify SSL certificates

        probe_response_status_code: HTTP status code from the response
        probe_response_elapsed_ms: Response time in milliseconds
        probe_response_final_url: Final URL after redirects
        probe_response_headers: Response headers
        probe_response_body: Response body
    """

    probe_url: str
    probe_method: str
    probe_timeout: int
    probe_verify: bool

    probe_response_status_code: int = 0
    probe_response_elapsed_ms: int = 0
    probe_response_final_url: str = ""
    probe_response_headers: Dict[str, str] = field(default_factory=dict)
    probe_response_body: str = ""

    def to_json(self):
        """Convert Probe to json."""
        return jsonify(self.__dict__)


def get_version() -> str:
    """Read version from pyproject.toml."""
    try:
        pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
        with open(pyproject_path, "r") as f:
            pyproject = toml.load(f)
            return pyproject["tool"]["poetry"]["version"]
    except Exception as e:
        logger.warning(f"Failed to read version from pyproject.toml: {e}")
        return "unknown"


def handle_invalid_arg(logger, error_msg, code):
    """Handle invalid args."""
    logger.error(error_msg)
    return {"error": error_msg}, code


def handle_request():
    """Handle probe requests.

    Returns:
        Probe: Object containing response information
    """
    url = request.args.get("url")
    method = request.args.get("method", "get").upper()
    timeout = request.args.get("timeout", DEFAULT_TIMEOUT)
    verify = request.args.get("verify", True)

    if not is_valid_url(url):
        return handle_invalid_arg(logger, f"Invalid URL format: {url}", 400)

    if method not in ALLOWED_METHODS:
        return handle_invalid_arg(
            logger,
            (
                f"Method {method} not allowed.",
                f"Allowed methods: {', '.join(ALLOWED_METHODS)}",
            ),
            405,
        )

    try:
        timeout = float(timeout)
    except ValueError:
        return handle_invalid_arg(logger, f"Invalid timeout: {timeout}", 400)

    try:
        verify = get_bool_from_arg(verify)
    except ValueError:
        return handle_invalid_arg(logger, f"Invalid verify: {verify}", 400)

    # send request to the URL and get the response
    logger.info("Probing URL: %s", url)
    resp = requests.request(
        method=method, url=url, timeout=timeout, verify=verify
    )

    probe_response = Probe(
        probe_url=url,
        probe_method=method,
        probe_timeout=timeout,
        probe_verify=verify,
        probe_response_status_code=resp.status_code,
        probe_response_body=resp.text,
        probe_response_headers=dict(resp.headers),
        probe_response_elapsed_ms=resp.elapsed.total_seconds(),
        probe_response_final_url=resp.url,
    )

    return probe_response.to_json()


def health_check():
    """Check the health status and version of the service.

    Returns:
        dict: Health status and version information with format:
            {"status": "healthy", "version": "x.y.z"}
    """
    version = importlib.metadata.version("url-prober")
    logger.info("Health check requested, version: %s", version)

    return {
        "status": "healthy",
        "version": version,
    }


def create_app():
    """Create and configure the Flask application.

    Returns:
        Flask: Configured Flask application instance
    """
    app = Flask(__name__)
    logger.info("Creating Flask application")

    app.route("/", methods=ALLOWED_METHODS)(handle_request)
    app.route("/health")(health_check)

    return app


if __name__ == "__main__":
    app = create_app()
    logger.info("Starting Flask application")
    app.run(debug=True)
