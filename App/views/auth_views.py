from flask import Blueprint, render_template, jsonify, request, flash, redirect, url_for
from flask_jwt_extended import jwt_required, unset_jwt_cookies, set_access_cookies, get_jwt_identity
from App.controllers.auth import login 
from App.models import User

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')

'''
Page Routes
'''
@auth_views.route('/login', methods=['POST'])
def login_action():
    data = request.form
    token = login(data['username'], data['password']) 
    response = redirect(request.referrer)  
    if not token:
        flash('Invalid username or password'), 401  
    else:
        flash('Login Successful')
        set_access_cookies(response, token)  
    return response

@auth_views.route('/logout', methods=['GET'])
def logout_action():
    response = redirect(request.referrer) 
    flash("Logged Out!")
    unset_jwt_cookies(response)  
    return response

@auth_views.route('/identify', methods=['GET'])
@jwt_required() 
def identify_page():
    current_user_id = get_jwt_identity() 
    user = User.query.get(current_user_id)  
    return render_template('message.html', title="Identify", message=f"You are logged in as {user.id} - {user.username}")

'''
API Routes
'''
@auth_views.route('/api/login', methods=['POST'])
def user_login_api():
    data = request.json
    token = login(data['username'], data['password'])  
    if not token:
        return jsonify(message='Invalid username or password'), 401
    response = jsonify(access_token=token) 
    set_access_cookies(response, token)  
    return response

@auth_views.route('/api/identify', methods=['GET'])
@jwt_required()  
def identify_user():
    current_user_id = get_jwt_identity() 
    user = User.query.get(current_user_id)
    return jsonify({'message': f"username: {user.username}, id: {user.id}"})

@auth_views.route('/api/logout', methods=['GET'])
def logout_api():
    response = jsonify(message="Logged Out!")
    unset_jwt_cookies(response) 
    return response
