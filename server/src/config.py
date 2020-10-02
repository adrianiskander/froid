import os

from . import confsec, utils


DEBUG = confsec.DEBUG

PROJECT_DIR = os.path.dirname(os.getcwd())
PUBLIC_DIR = os.path.join(PROJECT_DIR, 'public')
STATIC_DIR = os.path.join(PUBLIC_DIR, 'static')

APP_DIR = os.path.join(os.getcwd(), 'src')
APPS_DIR = os.path.join(APP_DIR, 'apps')

FROID_DIR = os.path.join(APPS_DIR, 'froid')
FROID_SCHEMA_URL = os.path.join(FROID_DIR, 'froid.sql')

INDEX_HTML_URI = os.path.join(PUBLIC_DIR, 'index.html')
INDEX_HTML = utils.load_file(INDEX_HTML_URI)
