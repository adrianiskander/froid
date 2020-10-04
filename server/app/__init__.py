"""
    Application factory module.
"""
from flask import Flask

from .froid import froid


app = Flask(__name__)


def create_app(config):
    """
        Create new application instance.
    """
    app.config.from_object(config)
    app.static_folder = config.STATIC_DIR

    # Passby circular dependencies
    from . import api_routes, views

    froid.create_tables(config.FROID_SCHEMA_URI)

    return app


def run_selenium():
    """
        Run Selenium and connect to Cleverbot.
    """
    froid.run_selenium()
