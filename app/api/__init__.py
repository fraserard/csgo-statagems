from flask import Blueprint

from app.api.resources import MapsAPI, PlayersAPI

api_bp = Blueprint('api', __name__, url_prefix='/api/v1') # /api/v1

api_bp.add_url_rule('/maps', view_func=MapsAPI.as_view('maps')) # /api/v1/maps
api_bp.add_url_rule('/players', view_func=PlayersAPI.as_view('players')) # /api/v1/players


# @api_bp.errorhandler(ValidationError)
# def handle_marshmallow_error(e):
#     """Return json error for marshmallow validation errors.

#     This will avoid having to try/catch ValidationErrors in all endpoints, returning
#     correct JSON response with associated HTTP 400 Status (https://tools.ietf.org/html/rfc7231#section-6.5.1)
#     """
#     return jsonify(e.messages), 400

# @api_bp.before_request
# @token_required
# def before_request():
#     """ Protect all of the admin endpoints. """
#     pass 