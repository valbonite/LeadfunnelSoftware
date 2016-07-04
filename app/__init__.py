from flask import Flask
from .util import ListConverter
from .util import filters
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config') #load default configuration
app.config.from_pyfile('config.py') #load configuration from the instance folder
app.config.from_envvar('APP_CONFIG_FILE') #load file specified by the APP_CONFIG_FILE environment variable
app.url_map.converters['list'] = ListConverter

db = SQLAlchemy(app)