#!flask/bin/python
from game import *
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello I'm anno domini's server\n"

if __name__ == '__main__':
	app.run()