import pytest
from werkzeug.security import generate_password_hash
from App.models import Student

# Test creation of a new student
def test_new_student():
    new_student = Student(
        username="alice", 
        password=generate_password_hash("alicepass"), 
        firstName="Alice", 
        lastName="Smith", 
        email="alice@mail.com",
        studentID="S001" 
    )

    assert new_student.studentID == "S001", "Testing student ID"
    assert new_student.username == "alice", "Testing username"
    assert new_student.firstName == "Alice", "Testing first name"
    assert new_student.lastName == "Smith", "Testing last name"
    assert new_student.email == "alice@mail.com", "Testing email"

# Test creation of converting to a dictionary 
def test_to_dict():
    student = Student(
        username="alice",
        password=generate_password_hash("alicepass"),
        firstName="Alice",
        lastName="Smith",
        email="alice@mail.com",
        studentID="S001"  # Fixed studentID
    )
    
    student_dict = student.to_dict()
    
    assert student_dict == {
        'studentID': 'S001',            
        'firstName': 'Alice',            
        'lastName': 'Smith',            
        'email': 'alice@mail.com'        
    }

def test_hashed_password():
    password = "alicepass"
    hashed = generate_password_hash(password, method='sha256')
    
    # Initialize the Student object with the hashed password
    student = Student(
        username="alice",
        password=hashed,
        firstName="Alice",
        lastName="Smith",
        email="alice@mail.com",
        studentID="S001"  
    )

    # Assert that the hashed password is not equal to the plain password
    assert student.password != password

def test_check_password():
    password = "alicepass"
    hashed = generate_password_hash(password, method='sha256')
    
    # Initialize the Student object with the hashed password
    student = Student(
        username="alice",
        password=hashed,
        firstName="Alice",
        lastName="Smith",
        email="alice@mail.com",
        studentID="S001"  
    )
    
    # Check if the password matches the hashed password
    assert student.check_password(password)


