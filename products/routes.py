from flask import Blueprint, jsonify
from .models import Product, Category
api = Blueprint('products', __name__)


@api.route('/')
def index():
	return jsonify({'data': 'Hello world'})
