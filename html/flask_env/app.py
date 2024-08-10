from flask import Flask, render_template, request
import logging
import sys

app = Flask(__name__)
app.config['TESTING'] = True
app.debug = True

# Set up logging
log_file = '/var/log/apache2/flask_app.log'
# file_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler(log_file)

file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('[flask] %(levelname)s: %(message)s')
file_handler.setFormatter(formatter)

# Add the handler to Flask's logger
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.propagate = False  # Ensure propagation is disabled

# Example logging within a route
@app.before_request
def log_request_info():
    app.logger.info(f"{request.method} : {request.path}")

@app.route('/')
def index():
    app.logger.info('Default route accessed')
    return "Hello, World!"

@app.route('/home')
def home():
    app.logger.info('Home route accessed')
    return "This is the home page"



if __name__ == '__main__':
    app.run()