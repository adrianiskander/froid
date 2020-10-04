from flask import redirect

from . import app, config, utils


@app.route('/')
def index_view():
    """
        Serve client app.
    """
    if config.DEBUG:
        return utils.load_file(config.INDEX_HTML_URI)
    return INDEX_HTML


@app.route('/', defaults={'path':''})
@app.route('/<path:path>')
def redirect_404(path):
    """
        Redirect non-existing views to index view.
    """
    return redirect('/')
