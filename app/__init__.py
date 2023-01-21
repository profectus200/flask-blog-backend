from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message = 'Authorize to access'
login_manager.login_message_category = 'success'

migrate = Migrate()

menu = [{'url': 'posts', 'title': 'Posts'},
        {'url': 'profile', 'title': 'Profile'},
        {'url': 'login', 'title': 'Login'},
        {'url': 'logout', 'title': 'Logout'}]


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    from app.blueprints.posts.views import posts
    from app.blueprints.profiles.views import profiles
    from app.blueprints.users.views import users

    app.register_blueprint(posts)
    app.register_blueprint(profiles)
    app.register_blueprint(users)

    return app
