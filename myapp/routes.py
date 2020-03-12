from flask import Blueprint, jsonify

api = Blueprint('default', __name__)


@api.route('/test')
def open():
    return jsonify({'result': 'Hello'})
