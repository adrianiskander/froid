from flask import redirect, render_template, request
from .extensions import app, froid
from .settings import config


@app.route('/')
def index():
    """
        Render home view.
    """
    return render_template('index.html')


@app.route('/froid')
def froid_route():
    """
        Render chat view.
    """
    return render_template('froid.html')


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
def redirect_all(path):
    """
        Redirect all routes to index route.
    """
    return redirect('/')
