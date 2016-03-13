from .. import db
from ..general.models import Base

from sqlalchemy.dialects.postgresql import JSON

# Define a User table
class User(Base):
    __tablename__ = 'user'
    name = db.Column(db.String(100), unique=True)
    age = db.Column(db.Integer)
    new_field = db.Column(db.Integer)
    json_field = db.Column(JSON)
    email = db.Column(db.String(200))

    def __init__(self, name, json):
        self.name = name
        self.json_field = json