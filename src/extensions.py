from flask import Flask
from .apps import froid


app = Flask(__name__)
froid = froid
