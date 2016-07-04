import OS

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
SQLALCHEMY_ECHO = False
BCRYPT_LEVEL = 12 #configuration for the Flask-Bcrypt extension
