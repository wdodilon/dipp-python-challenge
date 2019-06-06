"""
Text Blueprint
"""
from flask import Blueprint, jsonify
from config.config import Config
bp_text = Blueprint('text', __name__, url_prefix='/') # pylint: disable=invalid-name

@bp_text.route('/' + Config.API_BASE_PATH + '/boxfit', methods=['POST'])
def api_box_fit():
    """
    API Fit the text inside the box route
    """
    return jsonify("This should be your output")
