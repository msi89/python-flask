from flask import Blueprint

api = Blueprint('products', __name__)


@api.route('/')
def test():
    return {'sjhg': 'products'}
