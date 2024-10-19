from flask import Blueprint, request, jsonify

from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from App.controllers import (
    create_user, get_user_by_username, get_user, update_user
)
from App.models.user import User

user_views = Blueprint('user_views', __name__)

# Register a user
@user_views.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    try:
        user = create_user(
            username=data['username'],
            password=data['password'],
            firstName=data['firstName'],
            lastName=data['lastName'],
            email=data['email']
        )
        return jsonify(user=user.get_json()), 201
    except Exception as e:
        return jsonify(message="Username invalid or taken"), 400

# Get details of the current logged-in user
@user_views.route('/user', methods=['GET'])
@jwt_required()
def get_current_user():
    identity = get_jwt_identity()  
    user = User.query.get(identity)  

    if user:
        return jsonify(user=user.get_json()), 200  
    else:
        return jsonify(message="User not found"), 404  

