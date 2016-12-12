# f2.py
# ref:
# http://flask.pocoo.org/

# Demo:
# export FLASK_APP=f2.py
# flask run
# curl 127.0.0.1:5000/

# import pdb
import os
from   flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    # pdb.set_trace()
    return "Hello World!\n"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
'bye'
