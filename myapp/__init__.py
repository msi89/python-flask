from flask import Flask
from os import environ
from .commands import create_users, create_database
from .settings import db, guard, serializer
from accounts.models import User
from .routes import api as default_routes
from posts.routes import api as posts_routes
from accounts.routes import api as accounts_routes


def create_app():
    app = Flask(__name__)
    app. config['SECRET_KEY'] = environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
        'SQLALCHEMY_DATABASE_URI')
    app.config['JWT_ACCESS_LIFESPAN'] = {'months': 1}
    db.init_app(app)
    guard.init_app(app, User)
    serializer.init_app(app)
    app.cli.add_command(create_users)
    app.cli.add_command(create_database)
    app.register_blueprint(default_routes, url_prefix='/api')
    app.register_blueprint(accounts_routes, url_prefix='/api/accounts')
    app.register_blueprint(posts_routes, url_prefix='/api/posts')
    return app
