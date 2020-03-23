from flask import Blueprint, jsonify

api = Blueprint('default', __name__)


@api.route('/test')
def index():
    return jsonify({'result': 'Hello'})
