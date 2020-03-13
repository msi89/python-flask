import click
import os
from flask.cli import with_appcontext
from .extensions import db
from .helpers import create_folder, create_files
from blog.seeders import create_posts_seeder
from products.seeders import create_categories_seeder, create_products_seeder


@click.command(name='migrate')
@with_appcontext
def create_database():
    db.create_all()


@click.command(name='startapp')
@with_appcontext
def start_application():
    app_name = create_folder()
    create_files([
        os.path.join(app_name, '__init__.py'),
        os.path.join(app_name, 'models.py'),
        os.path.join(app_name, 'routes.py'),
        os.path.join(app_name, 'serializers.py'),
        os.path.join(app_name, 'seeders.py'),
    ])


@click.command(name='seed')
@with_appcontext
def create_seeders():
    create_categories_seeder()
    create_products_seeder()
    create_posts_seeder()
