from flask import jsonify, request
# Import password / encryption helper tools
# from werkzeug import check_password_hash, generate_password_hash
# Import the database object from the main app module
from . import user_blueprint
from .models import User
from .. import db


@user_blueprint.route('/test', methods=['GET', 'POST'])
def test():
    """Return some json."""
    return jsonify({'message': 'hello form users.controller'})


@user_blueprint.route('/users', methods=['GET', 'POST'])
def create_user():
    """Create user."""
    data = request.get_json()
    user = User(data)
    db.session.add(user)
    db.session.commit()

    return jsonify(
        {
            'data': data,
            'status': 'success'
        }
    ), 201
