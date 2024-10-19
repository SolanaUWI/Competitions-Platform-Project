import pytest
from App.models import Results

# Test creation of new results entry
def test_new_result():
    result = Results(
        resultID="R001",
        competitionID="C001",
        studentID="S001",
        score=85,
        completionTime="01:30:00",
        ranking=1
    )

    # Assertions to check the expected output
    assert result.resultID == "R001"
    assert result.competitionID == "C001"
    assert result.studentID == "S001"
    assert result.score == 85
    assert result.completionTime == "01:30:00"
    assert result.ranking == 1

def test_to_dict():
    result = Results(
        resultID="R001",
        competitionID="C001",
        studentID="S001",
        score=85,
        completionTime="01:30:00",
        ranking=1
    )

    result_dict = result.to_dict()

    # Check that to_dict returns the expected dictionary
    expected_output = {
        "resultID": "R001",
        "competitionID": "C001",
        "studentID": "S001",
        "score": 85,
        "completionTime": "01:30:00",
        "ranking": 1
    }

    assert result_dict == expected_output


