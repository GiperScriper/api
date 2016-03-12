from flask import Blueprint
from ..general import Constants

user_blueprint = Blueprint('user_blueprint', __name__, url_prefix=Constants.API_PREFIX)

from . import controllers