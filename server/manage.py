import sys

from src import run_selenium
from src.wsgi import application as app


COMMANDS = {
    'runserver': app.run,
    'runselen': run_selenium
}


if __name__ == '__main__':
    COMMANDS[sys.argv[1]]()
