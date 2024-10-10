from App.database import db
from uuid import uuid4
from App.models import User
class Admin(User):
    __tablename__ = 'admin'
    
    adminID = db.Column(db.String, primary_key=True, default=lambda: f"A{uuid4().hex[:4].upper()}") 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key relationship

    def __init__(self, username, password, firstName, lastName, email):
        super().__init__(username, password, user_type="admin", first_name=first_name, last_name=last_name, email=email)
        
    def __repr__(self):
        return f'<Admin {self.adminID}>'

    def to_dict(self):
        return {
            'adminID': self.adminID,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email
        }
    __mapper_args__ = {
        "polymorphic_identity": "admin", 
    }
