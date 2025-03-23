"""Tests for the Flask application."""
from url_prober.app import create_app


def test_health_endpoint():
    """Test the health check endpoint returns correct response."""
    app = create_app()
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}
