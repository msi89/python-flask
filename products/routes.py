from flask import Blueprint, jsonify
from .models import Product, Category
api = Blueprint('products', __name__)


@api.route('/')
def index():
	products = Product.query.all()
