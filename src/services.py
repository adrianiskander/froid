from . import routes
from .extensions import app, froid
from .settings import config


def create_app(config):
    """
        Return new application instance.
    """
    app.config.from_object(config)

    app.static_folder = config.STATIC_DIR

    froid.create_tables(config.FROID_SCHEMA_URL)

    return app


def run_dev_server():
    """
        Run Flask development server.
    """
    app = create_app(config)
    app.run()


def run_selenium():
    """
        Run Selenium and connect to Cleverbot.
    """
    froid.run_selenium()
