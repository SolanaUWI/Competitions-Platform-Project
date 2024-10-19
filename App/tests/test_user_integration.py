import pytest
from App.controllers import create_user, get_user_by_username, get_user, get_all_users, get_all_users_json, update_user
from App.models import User
from App.database import db

@pytest.fixture
def user_data():
    import uuid
    unique_username = f"user_{uuid.uuid4()}"
    unique_email = f"{unique_username}@example.com"
    return {
        "username": unique_username,
        "password": "password123",
        "firstName": "Test",
        "lastName": "User",
        "email": unique_email
    }

def test_create_user(test_app, user_data):
    with test_app.app_context():
        user = create_user(**user_data)
        assert user is not None
        assert user.username == user_data["username"]

def test_get_user_by_username(test_app, user_data):
    with test_app.app_context():
        create_user(**user_data)
        user = get_user_by_username(user_data["username"])
        assert user is not None
        assert user.username == user_data["username"]

def test_get_user(test_app, user_data):
    with test_app.app_context():
        user = create_user(**user_data)
        retrieved_user = get_user(user.id)
        assert retrieved_user is not None
        assert retrieved_user.username == user.username

def test_get_all_users(test_app, user_data):
    with test_app.app_context():
        create_user(**user_data)
        users = get_all_users()
        assert len(users) > 0

def test_get_all_users_json(test_app, user_data):
    with test_app.app_context():
        create_user(**user_data)
        users_json = get_all_users_json()
        assert isinstance(users_json, list)
        assert users_json[0]['username'] == user_data["username"]

def test_update_user(test_app, user_data):
    with test_app.app_context():
        user = create_user(**user_data)
        update_user(user.id, "updatedusername")
        updated_user = get_user(user.id)
        assert updated_user is not None
        assert updated_user.username == "updatedusername"
