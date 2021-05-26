from flask import Flask
from flask import render_template
from flask import make_response

def create_app():
   # create a minimal app
   app = Flask(__name__)
   app.debug = False

   # returns cat giphy
   @app.route('/cats')
   def cats():
    resp = make_response(render_template('cats.html'));
    resp.headers["Content-Type"] = "text/html"
    return resp


   return app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)