from flask import Blueprint, request, jsonify, send_file
from .services import generate_image_service, test_image_service, is_online_service

main_bp = Blueprint('main', __name__)

@main_bp.route('/is_online', methods=['GET'])
def is_online():
    return is_online_service()

@main_bp.route('/generate_image', methods=['POST'])
def generate_image():
    return generate_image_service(request.json)

@main_bp.route('/test_image', methods=['GET'])
def test_image():
    return test_image_service()
