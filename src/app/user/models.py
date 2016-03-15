from sqlalchemy.dialects.postgresql import JSON

from .. import db
from ..general.models import Base


# Define a User table
class User(Base):
    __tablename__ = 'user'
    name = db.Column(db.String(100), unique=True)
    age = db.Column(db.Integer)
    new_field = db.Column(db.Integer)
    json_field = db.Column(JSON)
    email = db.Column(db.String(200))

    def __init__(self, data):
        try:
            self.name = data['name']
            self.json_field = data['json']
        except KeyError as e:
            raise Exception('Invalid user: missing ' + e.args[0])
