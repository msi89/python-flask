from .models import User
from core.extensions import guard, db


def create_users_eeder():
    one = User(username='Toto', password=guard.hash_password('toto'))
    two = User(username='Pojo', password=guard.hash_password('pojo'))
    three = User(username='Hello', password=guard.hash_password('hello'))
    db.session.add_all([one, two, three])
    db.session.commit()
