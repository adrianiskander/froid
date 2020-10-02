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
    from . import routes

    return app


def run_selenium():
    """
        Run Selenium and connect to Cleverbot.
    """
    froid.run_selenium()
