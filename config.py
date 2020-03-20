"""App configuration."""
from os import environ


class Config:
    """Set Flask configuration vars from .env file."""

    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('development')
    FLASK_DEBUG = True
    # Flask-Session
    # SESSION_TYPE = environ.get('SESSION_TYPE')
    # SESSION_REDIS = redis.from_url(environ.get('SESSION_REDIS'))
