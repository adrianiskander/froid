from flask import request

from . import app, froid


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
