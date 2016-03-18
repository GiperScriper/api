"""User Controller."""
from flask import jsonify, request
# Import password / encryption helper tools
# from werkzeug import check_password_hash, generate_password_hash
# Import the database object from the main app module
from . import user_blueprint
from .models import User
from .. import db


@user_blueprint.route('/users/', methods=['GET'])
def get_users():
    """Get all users."""
    users_urls = [user.get_url() for user in User.query.all()]
    return jsonify({'users': users_urls})


@user_blueprint.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    """Get a specific user."""
    user = User.query.get_or_404(id).export_data()
    return jsonify(user)


@user_blueprint.route('/users/', methods=['POST'])
def create_user():
    """Create user."""
    data = request.get_json()
    user = User(data)
    db.session.add(user)
    db.session.commit()
    return jsonify({}), 201, {'Location': user.get_url()}


@user_blueprint.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    """Update user."""
    data = request.get_json()
    db.session.query(User).filter_by(id=id).update(data)
    db.session.commit()

    return jsonify({}), 200


@user_blueprint.route('/users/<int:id>', methods=['DELETE'])
def remove_user(id):
    """Remove user."""
    User.query.filter_by(id=id).delete()
    db.session.commit()

    return jsonify({}), 204
