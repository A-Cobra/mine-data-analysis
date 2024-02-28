from flask import Blueprint, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/api/v1/load', methods=['POST'])
def home():
    return jsonify({'message': 'Loaded successfully'})

@main_bp.route('/api/v1/list', methods=['GET'])
def about():
    return jsonify({'message': 'This is a list'})