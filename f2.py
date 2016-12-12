# f2.py
# ref:
# http://flask.pocoo.org/

# Demo:
# export FLASK_APP=f2.py
# flask run
# curl 127.0.0.1:5000/

# import pdb
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    # pdb.set_trace()
    return "Hello World!\n"

'bye'
