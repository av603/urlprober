"""Flask application module for URL Prober."""
from flask import Flask


def create_app():
    """Create and configure the Flask application.

    Returns:
        Flask: Configured Flask application instance
    """
    app = Flask(__name__)

    @app.route("/health")
    def health_check():
        """Health check endpoint.

        Returns:
            dict: Status response
        """
        return {"status": "healthy"}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
