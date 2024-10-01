from App.database import db
from uuid import uuid4

class Admin(db.Model):
    __tablename__ = 'admins'
    
    adminID = db.Column(db.String, primary_key=True, default=lambda: f"A{uuid4().hex[:4].upper()}") 
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Admin {self.adminID}>'

    def to_dict(self):
        return {
            'adminID': self.adminID,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email
        }
