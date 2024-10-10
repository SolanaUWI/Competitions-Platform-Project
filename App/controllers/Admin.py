import csv
from datetime import datetime
from sqlalchemy import func
from App.models import Admin
from App.models import Competition 
from App.models import Results
from App.models import db 

#Function to create an admin
def create_admin(username, password, first_name, last_name, email):
    existing_admin = Admin.query.filter_by(email=email).first()
    if existing_admin:
        raise ValueError(f"An admin with email '{email}' already exists.")
    
    admin_id = f"A{len(Admin.query.all()) + 1:03d}"
    
    new_admin = Admin(
        #adminID=admin_id, #removed adminID
        firstName=first_name,
        lastName=last_name,
        username = username,
        password = password,
        email=email
    )
    
    db.session.add(new_admin)
    db.session.commit()
    
    return admin_id

#Function return admins
def get_all_admins():
    return Admin.query.all()

#Function return admins as json
def get_all_admins_json():
    return [admin.to_dict() for admin in Admin.query.all()]

#Function to create a competition
def create_competition(name, date_str, status, description):
    competition_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    
    max_id = db.session.query(func.max(Competition.competitionID)).scalar()
    
    if max_id is None:
        new_id_number = 1
    else:
        new_id_number = int(max_id[1:]) + 1
    
    competition_id = f"C{new_id_number:03d}"
    
    new_competition = Competition(
        competitionID=competition_id,
        title=name,
        date=competition_date,
        competitionType=status,
        description=description,
        adminID=None 
    )
    
    db.session.add(new_competition)
    db.session.commit()
    
    return competition_id

#Function to update the details of a competition
def update_competition_details(competition_id, **kwargs):
    competition = Competition.query.get(competition_id)
    if competition is None:
        print(f"Competition with ID {competition_id} not found.")
        return
    
    for key, value in kwargs.items():
        setattr(competition, key, value)

    db.session.commit()
    print(f"Competition {competition_id} updated successfully.")

#Function to import results from a CSV file
def import_results_from_file(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                result_id = row['resultID']

                if db.session.query(Results).filter_by(resultID=result_id).first() is not None:
                    print(f"Skipping duplicate resultID: {result_id}")
                    continue 

                competition_id = row['competitionID']
                student_id = row['studentID']
                score = int(row['score'])
                completion_time = row['completionTime']
                ranking = int(row['ranking'])
                competition_date = row['date']  

                competition = db.session.query(Competition).filter_by(competitionID=competition_id).first()
                if competition is None:
                    try:
                        parsed_date = datetime.strptime(competition_date, "%Y-%m-%d").date()
                    except ValueError:
                        parsed_date = datetime.strptime("2024-01-01", "%Y-%m-%d").date()

                    competition = Competition(
                        competitionID=competition_id,
                        title=row.get('name', 'Imported Competition'),
                        date=parsed_date,
                        description="Imported competition",
                        competitionType=row.get('status', 'Closed'), 
                        adminID=None 
                    )
                    db.session.add(competition)
                    print(f"Imported new competition with ID: {competition_id}")

                result = Results(
                    resultID=result_id,
                    competitionID=competition_id,
                    studentID=student_id,
                    score=score,
                    completionTime=completion_time,
                    ranking=ranking
                )
                
                db.session.add(result)
            
            db.session.commit()
            print(f'Results imported from {file_path}')
    except Exception as e:
        print(f"An error occurred while importing results: {e}")

