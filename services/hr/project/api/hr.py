from flask import Blueprint, jsonify

hr_blueprint = Blueprint('hr', __name__)


@hr_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong! hrrrrrrrrrr'
    }), 200
