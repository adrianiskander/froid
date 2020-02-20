import os
from . import confsec


DEBUG = confsec.DEBUG


BASE_DIR = os.getcwd()

APP_DIR = os.path.join(os.getcwd(), 'src')
APPS_DIR = os.path.join(APP_DIR, 'apps')

PUBLIC_DIR = os.path.join(BASE_DIR, 'public')
STATIC_DIR = os.path.join(PUBLIC_DIR, 'static')

FROID_DIR = os.path.join(APPS_DIR, 'froid')
FROID_SCHEMA_URL = os.path.join(FROID_DIR, 'froid.sql')
