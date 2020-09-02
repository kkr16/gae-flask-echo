import flask
import json


app = flask.Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True



@app.route('/')
def hello():
    """Return a dump of HTTP headers."""
    headers = dict(flask.request.headers)
    return headers



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
