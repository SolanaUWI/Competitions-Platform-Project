import pytest
from App.controllers import get_all_results, get_all_results_json, get_results_by_competition, get_result_details, import_results_from_file, create_admin, create_competition, create_student
from App.models import Results
from App.database import db

@pytest.fixture
def admin_data():
    import uuid
    unique_email = f"admin_{uuid.uuid4()}@example.com"
    return {
        "username": "adminuser",
        "password": "adminpass",
        "first_name": "Admin",
        "last_name": "User",
        "email": unique_email
    }

@pytest.fixture
def competition_data():
    return {
        "name": "Science Fair",
        "date_str": "2024-12-01",
        "status": "Open",
        "description": "Annual Science Fair"
    }

@pytest.fixture
def student_data():
    import uuid
    unique_email = f"student_{uuid.uuid4()}@example.com"
    return {
        "username": f"studentuser_{uuid.uuid4()}",
        "password": "studentpass",
        "first_name": "Student",
        "last_name": "User",
        "email": unique_email
    }

@pytest.fixture
def result_data(test_app, admin_data, competition_data, student_data):
    with test_app.app_context():
        # Create admin and competition
        admin_id = create_admin(**admin_data)
        competition_data["admin_id"] = admin_id
        competition_id = create_competition(**competition_data)
        
        # Create student
        student_id = create_student(**student_data)
        
        return {
            "resultID": "R001",
            "competitionID": competition_id,
            "studentID": student_id,
            "score": 95,
            "completionTime": "01:30:00",
            "ranking": 1
        }

def test_get_all_results(test_app, result_data):
    with test_app.app_context():
        # Add result manually to the database
        result = Results(**result_data)
        db.session.add(result)
        db.session.commit()

        results = get_all_results()
        assert len(results) > 0

def test_get_all_results_json(test_app, result_data):
    with test_app.app_context():
        # Add result manually to the database
        result = Results(**result_data)
        db.session.add(result)
        db.session.commit()

        results_json = get_all_results_json()
        assert isinstance(results_json, list)
        assert len(results_json) > 0

def test_get_results_by_competition(test_app, result_data):
    with test_app.app_context():
        # Add result manually to the database
        result = Results(**result_data)
        db.session.add(result)
        db.session.commit()

        results = get_results_by_competition(result_data["competitionID"])
        assert len(results) > 0
        assert results[0].competitionID == result_data["competitionID"]

def test_get_result_details(test_app, result_data):
    with test_app.app_context():
        # Add result manually to the database
        result = Results(**result_data)
        db.session.add(result)
        db.session.commit()

        result_details = get_result_details(result_data["resultID"])
        assert result_details is not None
        assert result_details.resultID == result_data["resultID"]

def test_import_results_from_file(test_app, admin_data, competition_data, student_data):
    with test_app.app_context():
        # Assuming the file path to a correctly formatted CSV file for testing
        file_path = "/path/to/test_results.csv"
        import_results_from_file(file_path)
        
        # Check if the results have been imported
        results = get_all_results()
        assert len(results) > 0
