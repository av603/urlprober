"""Tests for the Flask application."""
import importlib.metadata

from url_prober.app import create_app


def test_health_endpoint():
    """Test the health check endpoint returns correct response."""
    app = create_app()
    client = app.test_client()
    version = importlib.metadata.version("url-prober")

    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy", "version": version}
