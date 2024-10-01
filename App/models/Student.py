from App.database import db
from uuid import uuid4

class Student(db.Model):
    __tablename__ = 'students'
    
    studentID = db.Column(db.String, primary_key=True, default=lambda: f"S{uuid4().hex[:4].upper()}") 
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

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
