import pytest
from App.controllers import create_admin, get_all_admins, get_all_admins_json, update_competition_details
from App.models import Admin, Competition
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

def test_create_admin(test_app, admin_data):
    with test_app.app_context():
        admin_id = create_admin(**admin_data)
        admin = Admin.query.filter_by(adminID=admin_id).first()
        assert admin is not None
        assert admin.username == "adminuser"

def test_get_all_admins(test_app, admin_data):
    with test_app.app_context():
        create_admin(**admin_data)
        admins = get_all_admins()
        assert len(admins) > 0

def test_get_all_admins_json(test_app, admin_data):
    with test_app.app_context():
        create_admin(**admin_data)
        admins_json = get_all_admins_json()
        assert isinstance(admins_json, list)
        assert admins_json[0]['username'] == "adminuser"

def test_update_competition_details(test_app, admin_data):
    with test_app.app_context():
        admin_id = create_admin(**admin_data)
        competition_id = "C001"  # Mock or create a competition with this ID
        update_competition_details(competition_id, title="Updated Competition")
        competition = db.session.query(Competition).filter_by(competitionID=competition_id).first()
        assert competition.title == "Updated Competition"
