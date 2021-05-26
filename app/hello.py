from flask import Flask
from flask import render_template
from flask import make_response

app = Flask(__name__)

@app.route("/cats")
def cats():
    resp = make_response(render_template('cats.html'));
    resp.headers["Content-Type"] = "text/html"
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)