from App.database import db
from uuid import uuid4
from App.models import User
class Student(User):
    __tablename__ = 'student'
    
    studentID = db.Column(db.String, primary_key=True, default=lambda: f"S{uuid4().hex[:4].upper()}") 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key relationship
    def __init__(self, username, password, firstName, lastName, email):
        super().__init__(username, password, user_type="student", firstName=firstName, lastName=lastName, email=email)

    competitions = db.relationship('Competition', secondary='competition_participants', back_populates='participants')

    def __repr__(self):
        return f'<Student {self.studentID}>'

    def to_dict(self):
        return {
            'studentID': self.studentID,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email
        }

    __mapper_args__ = {
        "polymorphic_identity": "student",  
    }
