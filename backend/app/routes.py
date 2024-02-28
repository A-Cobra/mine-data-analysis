from flask import Blueprint, jsonify, request
from app.utils.get_analysis_report import get_analysis_report

main_bp = Blueprint('main', __name__)

@main_bp.route('/api/v1/load', methods=['POST'])
def home():
    data = request.get_json()
    print("Loading")
    print(data[0])

    response = get_analysis_report(data)
    return jsonify({'transformed': response})

@main_bp.route('/api/v1/list', methods=['GET'])
def about():
    return jsonify({'message': 'This is a list'})