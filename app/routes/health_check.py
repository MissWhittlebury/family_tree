from flask import blueprints
from flask import jsonify

bp = blueprints.Blueprint('health_check', __name__)


@bp.route('/health_check', methods=['GET'])
def health_check():
    return jsonify(True)
