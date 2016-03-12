from flask import Blueprint, request
# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash
# Import the database object from the main app module
from app import db
from app.users.models import User
import json

# Define the blueprint:
users_blueprint = Blueprint('users_blueprint', __name__, url_prefix='/api')

@users_blueprint.route('/test', methods=['GET', 'POST'])
def test():
    return json.dumps({'message': 'hello form users.controller'})

@users_blueprint.route('/users', methods=['GET', 'POST'])
def create_user():
    data = json.loads(request.data.decode('utf-8'))
    user = User(data['name'], data['json'])
    db.session.add(user)
    db.session.commit()

    return json.dumps(
        {
            'test': 'test message',
            'data': data
        }
    )
