

from flask import Flask


app = Flask(__name__)

from routes import *
from errorhandlers import *

if __name__ == "__main__":
    app.run(port=80, debug=True)