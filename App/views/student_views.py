from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from App.controllers import (
    create_student, get_all_students_json, view_competitions,
    view_results, register_for_competition
)
from App.models.user import User

student_views = Blueprint('student_views', __name__)

# Register a student
@student_views.route('/register/student', methods=['POST'])
def register_student():
    data = request.get_json()
    try:
        student_id = create_student(
            username=data['username'],
            password=data['password'],
            first_name=data['firstName'],
            last_name=data['lastName'],
            email=data['email']
        )
        return jsonify(message=f"Student registered with ID: {student_id}"), 201  
    except Exception as e:
        return jsonify(error=str(e)), 400

# Get all students (Admin only)
@student_views.route('/students', methods=['GET'])
@jwt_required()
def get_all_students():
    students = get_all_students_json()
    return jsonify(students), 200 

# Register a student for a competition
@student_views.route('/student/<student_id>/competition/<competition_id>', methods=['POST'])
@jwt_required()
def register_student_for_competition(student_id, competition_id):
    try:
        register_for_competition(student_id, competition_id)
        return jsonify(message=f"Student {student_id} registered for competition {competition_id}"), 201
    except Exception as e:
        return jsonify(error=str(e)), 400
