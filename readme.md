Competition Platform CLI system:
This system allows you to manage competitions, students, admins, and competition results via a command-line interface (CLI) using Flask commands.
For readability look at the readme in code mode.

Installation:
-pip install -r requirements.txt
-You may need to activate the virtual environment.

Available CLI Commands:

flask init 
-Initializes the database.

Student Commands

flask student create <username> <password> <first_name> <last_name> <email>
E.g.- flask student create JohnDoe password1 John Doe john.doe@example.com
-Creates a Student

flask student list
-List all Students

flask student registerCompetition <StudentID> <CompetitionID>
E.g.- flask student registerCompetition S001 C001 
-Registers a created student to a existing competition

Admin Commands

flask admin create <username> <password> <first_name> <last_name> <email>
E.g.- flask admin create JaneSmith password1 Jane Smith jane.smith@example.com
-Creates an Admin

flask admin list
-List all Admins

flask admin import <file_path>
E.g.- flask admin import "Data/results.csv"
-Imports Results from CSV file

flask admin createCompetition <name> <date> <status> <description> <adminID>
E.g.- flask admin createCompetition "Coding Contest" "2024-05-10" "Open" "A programming competition" "A001"
-Creates a Competition with an existing admin

flask admin update_competition <competition_id> <new_name> <new_date> <new_status>
E.g.- flask admin update_competition C001 "New Competition Name" "2024-10-01" "Closed"
-Updates a Competition


Competition Commands

flask competition list
-List Competitions


Results Commands

flask results list
-Lists All Results

flask results competition <competition_id>
E.g.- flask results competition C005
-List Results for a Competition




#   C o m p e t i t i o n - p l a t f o r m - t e s t 
 
 
