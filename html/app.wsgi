import sys
import logging
import os 

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

sys.path.insert(0, "/var/www/html")

os.environ['FLASK_ENV'] = 'development'

from app import app as application
