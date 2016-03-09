from app import app
import json

@app.route('/')
def index():
    return json.dumps({'message': 'this is json'})

@app.route('/hello/<message>/<message2>/')
def hello(message, message2):
    return 'Hello %s, %s' % (message, message2)