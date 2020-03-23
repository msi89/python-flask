from flask import Blueprint, jsonify, request, Response
from flask_praetorian import auth_required
from werkzeug.exceptions import BadRequest
from .models import Post
from core.exts import db
from .serializers import PostSerialiser


api = Blueprint('blog', __name__)
@api.errorhandler(BadRequest)
def handle_bad_request(e):
    return 'bad request! {}'.format(e.description), 400


api.register_error_handler(400, handle_bad_request)
post_serializer = PostSerialiser()
posts_serializer = PostSerialiser(many=True)


@api.route('/posts', methods=['GET'])
@auth_required
def get_all_posts():
    posts = Post.query.all()
    return jsonify(posts_serializer.dump(posts)), 200


@api.route('posts', methods=['POST'])
@auth_required
def create_post():
    data = request.get_json()
    errors = post_serializer.validate(data)
    if errors:
        return jsonify(errors), 400

    post = Post(title=data['title'], body=data['body'])
    db.session.add(post)
    db.session.commit()
    return jsonify(post_serializer.dump(post)), 201


@api.route('/posts/<id>', methods=['PUT', 'PATCH'])
@auth_required
def update_post(id):
    post = Post.query.get_or_404(id)
    data = request.get_json()
    errors = post_serializer.validate(data)
    if errors:
        return jsonify(errors), 400

    post.title = data['title']
    post.body = data['body']
    db.session.commit()
    return jsonify(post_serializer.dump(post)), 200


@api.route('/posts/<id>', methods=['DELETE'])
@auth_required
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return Response(None, 204)
