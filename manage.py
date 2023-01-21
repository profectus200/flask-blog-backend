import os

from flask_script import Manager, Shell

from app import create_app, db
from app.blueprints.posts.models import Posts
from app.blueprints.profiles.models import Profiles
from app.blueprints.users.models import Users

app = create_app(os.getenv('FLASK_ENV') or 'config.DevelopmentConfig')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, Users=Users, Posts=Posts, Profiles=Profiles)


manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
