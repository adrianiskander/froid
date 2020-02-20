import sys
from src import services


COMMANDS = {
    'runserver': services.run_dev_server,
    'runselenium': services.run_selenium
}


if __name__ == '__main__':
    COMMANDS[sys.argv[1]]()
