import flask
from flask import request


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/search', methods=['GET'])
def search():
    resp = flask.Response(request.args.get('a') + request.args.get('b'))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
