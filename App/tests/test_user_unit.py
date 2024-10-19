# App/tests/test_user_unit.py
import pytest
from werkzeug.security import generate_password_hash
from App.models import User

# Test creation of a new user
def test_new_user():
    newuser = User(
        username="bob",
        password=generate_password_hash("bobpass"),  # Hash the password here
        user_type="user",  
        firstName="Bob",
        lastName="Smith",
        email="bob@mail.com"
    )

    assert newuser.username == "bob"
    assert newuser.firstName == "Bob"
    assert newuser.lastName == "Smith"
    assert newuser.email == "bob@mail.com"
    assert newuser.user_type == "user"  

def test_get_json():
    user = User(
        username="bob",
        password=generate_password_hash("bobpass"),
        user_type="user",
        firstName="Bob",
        lastName="Smith",
        email="bob@mail.com"
    )
    
    expected_json = {
        'id': None,  # This will be None until the user is added to the session and committed
        'username': 'bob',
        'user_type': 'user',
        'firstName': 'Bob',
        'lastName': 'Smith',
        'email': 'bob@mail.com'
    }
    
    assert user.get_json() == expected_json

def test_hashed_password():
    password = "mypass"
    hashed = generate_password_hash(password)
    
    user = User(
        username="bob",
        password=hashed,
        user_type="user",
        firstName="Bob",
        lastName="Smith",
        email="bob@mail.com"
    )

    assert user.password != password

def test_check_password():
    password = "mypass"
    hashed = generate_password_hash(password)
    
    user = User(
        username="bob",
        password=hashed,
        user_type="user",
        firstName="Bob",
        lastName="Smith",
        email="bob@mail.com"
    )
    
    assert user.check_password(password)
