from flask import Blueprint

user_blueprint = Blueprint('user_blueprint', __name__, url_prefix='/api/v1')

from . import controllers