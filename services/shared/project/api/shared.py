from flask import Blueprint, jsonify

shared_blueprint = Blueprint('shared', __name__)


@shared_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong! sharedddddddddddddd'
    }), 200
