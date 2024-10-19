import pytest
from App.controllers import create_student, get_all_students, get_all_students_json, view_competitions, view_results, register_for_competition
from App.models import Student
from App.models import Competition
from App.database import db

@pytest.fixture
def student_data():
    return {
        "username": "studentuser",
        "password": "studentpass",
        "first_name": "Student",
        "last_name": "User",
        "email": "student@example.com"
    }

def test_create_student(test_app, student_data):
    with test_app.app_context():
        student_id = create_student(**student_data)
        student = Student.query.filter_by(studentID=student_id).first()
        assert student is not None
        assert student.username == "studentuser"

def test_get_all_students(test_app, student_data):
    with test_app.app_context():
        create_student(**student_data)
        students = get_all_students()
        assert len(students) > 0

def test_get_all_students_json(test_app, student_data):
    with test_app.app_context():
        create_student(**student_data)
        students_json = get_all_students_json()
        assert isinstance(students_json, list)
        assert students_json[0]['firstName'] == "Student"

def test_view_competitions(test_app, student_data):
    with test_app.app_context():
        student_id = create_student(**student_data)
        competitions = view_competitions(student_id)
        assert isinstance(competitions, list)

def test_view_results(test_app, student_data):
    with test_app.app_context():
        student_id = create_student(**student_data)
        results = view_results(student_id)
        assert isinstance(results, list)

def test_register_for_competition(test_app, student_data):
    with test_app.app_context():
        student_id = create_student(**student_data)
        competition_id = "C001"  # Assume this competition is pre-created
        register_for_competition(student_id, competition_id)
        student = Student.query.filter_by(studentID=student_id).first()
        assert any(comp.competitionID == competition_id for comp in student.competitions)
