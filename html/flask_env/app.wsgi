import sys
import logging
import os 


sys.path.insert(0, "/var/www/html/flask_env")

os.environ['FLASK_ENV'] = 'development'

from app import app as application
