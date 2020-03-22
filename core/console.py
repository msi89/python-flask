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
    try:
       db.create_all()
       print("database successfully migrated")
    except Exception as e:
        print(e)


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

    try:
        with open(os.path.join(app_path, 'routes.py'), "a") as f:
            f.write("from flask import Blueprint, jsonify\n")
            f.write('\n')
            f.write(
                "app = Blueprint('{}', __name__)\n\n".format(app_name.lower()))
            f.write('')
            f.write('@app.route(\'/\')\n')
            f.write('def index():\n')
            f.write('\treturn jsonify({\'data\': \'Hello world\'})\n')
            f.close()
    except Exception as e:
        print(e)


@click.command(name='seed')
@with_appcontext
def create_seeders():
    create_categories_seeder()
    create_products_seeder()
    create_posts_seeder()
