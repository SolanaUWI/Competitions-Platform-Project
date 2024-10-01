from App.database import db

class Results(db.Model):
    __tablename__ = 'results'
    resultID = db.Column(db.String, primary_key=True)
    competitionID = db.Column(db.String, db.ForeignKey('competitions.competitionID'), nullable=False)
    studentID = db.Column(db.String, db.ForeignKey('students.studentID'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    completionTime = db.Column(db.String, nullable=True)
    ranking = db.Column(db.Integer, nullable=False)
    
    def to_dict(self):
        return {
            "resultID": self.resultID,
            "competitionID": self.competitionID,
            "studentID": self.studentID,
            "score": self.score,
            "completionTime": self.completionTime,
            "ranking": self.ranking
        }

    def __repr__(self):
        return f'<Results {self.resultID}>'