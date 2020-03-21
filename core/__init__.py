from flask import Flask
from os import environ
from .console import create_database, start_application, create_seeders
from .extensions import db, guard, serializer
from accounts.models import User
from .routes import api as default_routes
from blog.routes import api as blog_routes
from products.routes import api as products_routes
from accounts.routes import api as accounts_routes


def create_app():
    app = Flask(__name__)
    app. config['SECRET_KEY'] = environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = get_database_uri()
    app.config['JWT_ACCESS_LIFESPAN'] = {'months': 1}

    db.init_app(app)
    guard.init_app(app, User)
    serializer.init_app(app)

    app.cli.add_command(create_database)
    app.cli.add_command(start_application)
    app.cli.add_command(create_seeders)

    app.register_blueprint(default_routes, url_prefix='/api')
    app.register_blueprint(accounts_routes, url_prefix='/api/accounts')
    app.register_blueprint(blog_routes, url_prefix='/api/blog')
    app.register_blueprint(products_routes, url_prefix='/api/products')

    return app


def get_database_uri():
    driver = environ.get('DB_DRIVER')
    if driver.lower() == 'pgsql':
        URL = environ.get('POSTGRES_URL')
        USER = environ.get('POSTGRES_URL')
        PWD = environ.get('POSTGRES_URL')
        DB = environ.get('POSTGRES_URL')
        return 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
            user=USER, pw=PWD, url=URL, db=DB)
    return environ.get('SQLITE')
