from App.models import Student
from App.models import Competition
from App.models import Results
from App.models import db
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError

#Function for creating a student
def create_student(username, password, first_name, last_name, email):
    try:
        if db.session.query(Student).filter_by(username=username).first() is not None:
            raise ValueError("Username already exists")
        if db.session.query(Student).filter_by(email=email).first() is not None:
            raise ValueError("Email already exists")

        existing_students = Student.query.all()
        student_id = f"S{len(existing_students) + 1:03d}"

        hashed_password = generate_password_hash(password)

        new_student = Student(
            username=username,
            password=hashed_password, 
            firstName=first_name,
            lastName=last_name,
            email=email,
            studentID=student_id 
        )

        db.session.add(new_student)
        db.session.commit()

        return student_id

    except Exception as e:
        db.session.rollback()
        print(f"Error creating student: {e}")
        raise e  
def get_all_students():
    return Student.query.all()

def get_all_students_json():
    return [student.to_dict() for student in Student.query.all()]

#Function for viewing all competitions
def view_competitions(student_id):
    student = Student.query.get(student_id)
    if student:
        return Competition.query.all()

#Function for viewing results for a student
def view_results(student_id):
    student = Student.query.get(student_id)
    if student:
        return Results.query.filter_by(studentID=student_id).all()

#Function for registering a student for a competition
def register_for_competition(student_id, competition_id):
    student = Student.query.filter_by(studentID=student_id).first()
    competition = Competition.query.get(competition_id)

    if student is None:
        print(f"Student ID {student_id} does not exist.")
        return
    if competition is None:
        print(f"Competition ID {competition_id} does not exist.")
        return

    if student not in competition.participants:
        competition.participants.append(student)
        db.session.commit()
        print(f"Student {student_id} registered for competition {competition_id}.")
    else:
        print(f"Student {student_id} is already registered for competition {competition_id}.")

