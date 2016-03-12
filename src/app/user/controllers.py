from flask import request
# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash
# Import the database object from the main app module
from app import db
from .models import User
from . import user_blueprint
import json

@user_blueprint.route('/test', methods=['GET', 'POST'])
def test():
    return json.dumps({'message': 'hello form users.controller'})

@user_blueprint.route('/users', methods=['GET', 'POST'])
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
