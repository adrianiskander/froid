from .services import create_app
from .settings import config


application = create_app(config)
