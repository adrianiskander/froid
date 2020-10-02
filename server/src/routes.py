from flask import redirect, request

from . import app, config, froid, utils


@app.route('/')
def index():
    """
        Render home view.
    """
    if config.DEBUG:
        return utils.load_file(config.INDEX_HTML_URI) 
    return INDEX_HTML


@app.route('/api/greeting')
def greeting():
    """
        Return random greeting.
    """
    res = froid.get_random_greeting()
    return res, 200


@app.route('/api/response')
def response():
    """
        Return random response.
    """
    res = froid.get_random_sentence()
    return res, 200


@app.route('/api/stimulus', methods=('POST', ))
def stimulus():
    """
        Receive incoming stimulus and return specific response.
    """
    stim = request.data.decode()
    res = froid.handle_stimulus(stim)
    return res, 200


@app.route('/', defaults={'path':''})
@app.route('/<path:path>')
def redirect_404(path):
    """
        Redirect all routes to index route.
    """
    return redirect('/')
