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
    root = os.getcwd()
    app_name = input("Enter app name: ")
    app_path = os.path.join(root, app_name.lower())

    static = input('Would you generate static folder?(y/N)')
    template = input('Would you generate templates folder?(y/N)')

    create_folder(app_path)

    if static.lower() == 'y':
        create_folder(os.path.join(app_path, 'static'))
    if template.lower() == 'y':
        create_folder(os.path.join(app_path, 'templates'))

    create_files([
        os.path.join(app_path, '__init__.py'),
        os.path.join(app_path, 'models.py'),
        os.path.join(app_path, 'routes.py'),
        os.path.join(app_path, 'serializers.py'),
        os.path.join(app_path, 'seeders.py'),
    ])


@click.command(name='seed')
@with_appcontext
def create_seeders():
    create_categories_seeder()
    create_products_seeder()
    create_posts_seeder()
