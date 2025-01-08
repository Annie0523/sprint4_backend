import jwt
from flask import Blueprint, request, jsonify, current_app, Response, g
from flask_restful import Api, Resource  # used for REST API building
from datetime import datetime
from __init__ import app
from api.jwt_authorize import token_required
from model.channel import Channel
from model.group import Group
from model.user import User


comment_api = Blueprint("comment_api", __name__, url_prefix='/api')

api = Api(comment_api)

comments = []

class CommentAPI:
    """
    Define the API CRUD endpoints for the Comment model.
    There are four operations that correspond to common HTTP methods:
    - post: create a new comment
    - get: get all the comments
    """
    class _CRUD(Resource):
        def post(self):
            """
            Create a new comment.
            """
            global comments
            print("test")
            
            # Getting the information sent w/ request
            data = request.get_json()

            # Validate data
            if not data:
                return {'message': 'No input data provided'}, 400
            if data.get('comment', '').strip() == '':
                return {'message': 'Empty comment was provided'}, 400

            comments.append(data.get('comment', ''))
            return "success!", 200

    class _BULK_CRUD(Resource):
        def get(self):
            """
            Retrieve all comments.
            """
            return jsonify(comments)

    api.add_resource(_CRUD, '/comment')
    api.add_resource(_BULK_CRUD, '/comment')