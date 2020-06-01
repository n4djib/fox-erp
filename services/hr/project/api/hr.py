from flask import Blueprint, jsonify

hr_blueprint = Blueprint('hr', __name__)


@hr_blueprint.route('/hr/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong! hr'
    }), 200
