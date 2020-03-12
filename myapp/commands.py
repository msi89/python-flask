import click
from flask.cli import with_appcontext
from .settings import guard, db
from accounts.models import User


@click.command(name='migrate')
@with_appcontext
def create_database():
    db.create_all()


@click.command(name='create_users')
@with_appcontext
def create_users():
    one = User(username='One', password=guard.hash_password('one'))
    two = User(username='Two', password=guard.hash_password('two'))
    three = User(username='Three', password=guard.hash_password('three'))
    db.session.add_all([one, two, three])
    db.session.commit()
