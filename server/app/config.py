import os

from . import confsec, utils


DEBUG = confsec.DEBUG

PROJECT_DIR = os.path.dirname(os.getcwd())
APP_DIR = os.path.join(os.getcwd(), 'app')
PUBLIC_DIR = os.path.join(PROJECT_DIR, 'public')
STATIC_DIR = os.path.join(PUBLIC_DIR, 'static')

FROID_DIR = os.path.join(APP_DIR, 'froid')
FROID_SCHEMA_URI = os.path.join(FROID_DIR, 'froid.sql')

INDEX_HTML_URI = os.path.join(PUBLIC_DIR, 'index.html')
INDEX_HTML = utils.load_file(INDEX_HTML_URI)
