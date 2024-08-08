from flask import Flask, render_template
import logging
import sys

app = Flask(__name__)
app.config['TESTING'] = True
app.debug = True

#handler = logging.StreamHandler(sys.stdout)
#handler.setLevel(logging.INFO)
#app.logger.addHandler(handler)
#app.logger.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stderr, level=logging.INFO)

@app.route('/')
def index():
    logging.info("Home page accessed")
    print("index accessed", file=sys.stdout)
    return "Hello, Flask running on Apache also ?"

@app.route('/home')
def home():
    print("home route", file=sys.stderr)
    return "This is an another route"



@app.route('/other')
def other():
    return "and an antoher one here"
