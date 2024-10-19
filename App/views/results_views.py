from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from App.controllers import (
    get_all_results_json,
    get_results_by_competition,
    get_result_details,
)

results_views = Blueprint('results_views', __name__)

# Get all results
@results_views.route('/results', methods=['GET'])
def get_all_results():
    results = get_all_results_json()
    return jsonify(results), 200

# Get details of a specific result
@results_views.route('/results/<result_id>', methods=['GET'])
def get_result(result_id):
    result = get_result_details(result_id)
    if result:
        return jsonify(result.to_dict()), 200
    return jsonify({'error': 'Result not found'}), 404
