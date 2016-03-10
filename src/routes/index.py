from flask import request
from app import app, db
from models.user import User
import json

@app.route('/')
def index():
    return json.dumps({'message': 'this is json'})

@app.route('/hello/<message>/<message2>/')
def hello(message, message2):
    return 'Hello %s, %s' % (message, message2)

@app.route('/users', methods=['GET', 'POST'])
def create_user():
    data = json.loads(request.data.decode('utf-8'))
    user = User(data['name'])
    db.session.add(user)
    db.session.commit()

    return json.dumps(
        {
            'test': 'test message',
            'data': data
        }
    )