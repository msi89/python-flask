from flask import Blueprint, jsonify, request
from flask_praetorian import auth_required
from core.exts import guard, db
from .serializers import UserSerializer
from .models import User

api = Blueprint('accounts', __name__)

user_serializer = UserSerializer()
users_serializer = UserSerializer(many=True)


@api.route('/login', methods=['POST'])
def login():
    json_data = request.get_json()
    email = json_data['email']
    password = json_data['password']
    user = guard.authenticate(email, password)
    token = guard.encode_jwt_token(user)
    return jsonify({'meta': user_serializer.dump(user), 'access_token': token})


@api.route('/register', methods=['POST'])
def register():
    json_data = request.get_json()
    user = User(email=json_data['email'], password=guard.hash_password(
        json_data['password']))
    db.session.add(user)
    db.session.commit()
    return jsonify(user_serializer.dump(user))


@api.route('/')
@auth_required
def get_all_users():
    users = User.query.all()
    return jsonify(users_serializer.dump(users))


@api.route('/refresh')
@auth_required
def refresh():
    json_data = request.get_json()
    token = guard.refresh_jwt_token(json_data['token'])
    return jsonify({'access_token': token})
