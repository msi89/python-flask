from flask import Blueprint, jsonify, request
from flask_praetorian import auth_required
from .models import Post
from myapp.settings import db
from .serializers import PostSerialiser

api = Blueprint('posts', __name__)
post_serializer = PostSerialiser()
posts_serializer = PostSerialiser(many=True)


@api.route('/', methods=['GET'])
@auth_required
def get_all_posts():
    posts = Post.query.all()
    return jsonify(posts_serializer.dump(posts))


@api.route('', methods=['POST'])
@auth_required
def create_posts():
    data = request.get_json()
    post = Post(title=data['title'], body=data['body'])
    db.session.add(post)
    db.session.commit()
    return post_serializer.dump(post)
