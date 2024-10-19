import pytest
from App.controllers import create_admin
from App.controllers import create_competition, get_competition_details, get_all_competitions_json
from App.models import Competition
from App.database import db

@pytest.fixture
def competition_data():
    return {
        "name": "Math Olympiad",
        "date_str": "2024-11-10",
        "status": "Open",
        "description": "A challenging math competition"
    }

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

def test_create_competition(test_app, competition_data, admin_data):
    with test_app.app_context():
        admin_id = create_admin(**admin_data)
        competition_data["admin_id"] = admin_id
        competition_id = create_competition(**competition_data)
        competition = Competition.query.filter_by(competitionID=competition_id).first()
        assert competition is not None
        assert competition.title == "Math Olympiad"
