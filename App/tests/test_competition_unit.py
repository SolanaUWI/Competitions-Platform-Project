import pytest
from datetime import date
from App.models import Competition

# Test creation of a new competition
def test_new_competition():
    newcompetition = Competition(
        competitionID="C001",
        date=date(2024, 5, 10),
        title="Meteoroid Hackathon",  
        competitionType="Open",
        description="A programming competition",
        adminID="A001"
    )

    # Assertions to check the expected output
    assert newcompetition.competitionID == "C001"
    assert newcompetition.date == date(2024, 5, 10)
    assert newcompetition.title == "Meteoroid Hackathon"  
    assert newcompetition.competitionType == "Open"
    assert newcompetition.description == "A programming competition"
    assert newcompetition.adminID == "A001"

def test_to_dict():
    # Creates a competition entry to convert to a dictionary 
    newcompetition = Competition(
        competitionID="C001",
        date=date(2024, 5, 10),
        title="Meteoroid Hackathon",  
        competitionType="Open",
        description="A programming competition",
        adminID="A001"
    )

    competition_dict = newcompetition.to_dict()

    # Check that to_dict returns the expected dictionary
    expected_output = {
        'competitionID': 'C001',
        'title': 'Meteoroid Hackathon',  
        'date': '2024-05-10',
        'description': 'A programming competition',
        'competitionType': 'Open',
        'adminID': 'A001',
    }

    assert competition_dict == expected_output


