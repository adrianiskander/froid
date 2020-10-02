def load_file(uri):
    """
        Load file from given uri.
    """
    with open(uri) as file:
        return file.read()
