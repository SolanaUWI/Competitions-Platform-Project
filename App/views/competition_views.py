from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from App.controllers import (
    Competition,
    generate_competition_id,
    get_competition_details,
    get_all_competitions_json,
    update_competition_details,
)
from App.database import db

competition_views = Blueprint('competition_views', __name__)

# Get details of a specific competition
@competition_views.route('/competitions/<competition_id>', methods=['GET'])
def get_competition(competition_id):
    competition = get_competition_details(competition_id)
    if competition:
        return jsonify(competition), 200
    return jsonify({'error': 'Competition not found'}), 404

# Get all competitions
@competition_views.route('/competitions', methods=['GET'])
def get_all_competitions():
    competitions = get_all_competitions_json()
    return jsonify(competitions), 200
