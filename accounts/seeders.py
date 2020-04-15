from .models import User
from core.exts import guard, db


def create_users_seeder():
    one = User(email='toto@test.com', password=guard.hash_password('toto'))
    two = User(email='pojo@test.com', password=guard.hash_password('pojo'))
    three = User(email='hello@test.com', password=guard.hash_password('hello'))
    db.session.add_all([one, two, three])
    db.session.commit()
    print('users seeder successfuly created')
