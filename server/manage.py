import sys

from app import run_selenium
from app.wsgi import application as app


COMMANDS = {
    'runserver': app.run,
    'runselen': run_selenium
}


if __name__ == '__main__':
    COMMANDS[sys.argv[1]]()
