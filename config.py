import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SECRET KEY'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CSRF_ENABLED = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEVELOPMENT_DATABASE_URI') or 'postgresql://postgres:postgres@localhost:2101/flask-blog'


class TestingConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TESTING_DATABASE_URI') or 'postgresql://postgres:postgres@localhost:2101/flask-blog'


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'PRODUCTION_DATABASE_URI') or 'postgresql://postgres:postgres@localhost:2101/flask-blog'
