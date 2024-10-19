import pytest
from werkzeug.security import generate_password_hash
from App.models import Admin  

class TestAdminUnit:

    def test_new_admin(self):
       
        #Create the Admin instance, passing required parameters
        admin = Admin(
            username="jane", 
            password=generate_password_hash("jane123"), 
            firstName="Jane", 
            lastName="Doe", 
            email="JaneDoe@mail.com",
            adminID="A001"
        )
        # Assertions for the Admin instance
        assert admin.username == "jane"
        assert admin.firstName == "Jane"
        assert admin.lastName == "Doe"
        assert admin.email == "JaneDoe@mail.com"
        assert admin.adminID == "A001"
def test_to_dict():
    admin = Admin(
        username="jane",
        password=generate_password_hash("jane123"),
        firstName="Jane",
        lastName="Doe",
        email="JaneDoe@mail.com",
        adminID="A001"
    )
    
    admin_dict = admin.to_dict()
    
    assert admin_dict == {
        'adminID': 'A001',          
        'firstName': 'Jane',        
        'lastName': 'Doe',          
        'email': 'JaneDoe@mail.com' 
    }

def test_hashed_password():
    password = "mypass"
    hashed = generate_password_hash(password, method='sha256')
    admin = Admin(
        username="jane",
        password=hashed,
        firstName="Jane",
        lastName="Doe",
        email="JaneDoe@mail.com",
        adminID="A001"
    )

    # Assert that the hashed password is not equal to the plain password
    assert admin.password != password

def test_check_password():
    password = "mypass"
    hashed = generate_password_hash(password, method='sha256')
    
    # Initialize the Admin object with the hashed password
    admin = Admin(
        username="jane",
        password=hashed,
        firstName="Jane",
        lastName="Doe",
        email="JaneDoe@mail.com",
        adminID="A001"
    )
    
    # Check if the password matches the hashed password
    assert admin.check_password(password)
