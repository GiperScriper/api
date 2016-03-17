"""User Model Module."""
from sqlalchemy.dialects.postgresql import JSON
from flask import url_for

from .. import db
from ..general.models import Base


class User(Base):
    """User Model."""

    __tablename__ = 'user'
    name = db.Column(db.String(100), unique=True)
    age = db.Column(db.Integer)
    new_field = db.Column(db.Integer)
    json_field = db.Column(JSON)
    email = db.Column(db.String(200))

    def get_url(self):
        """Get user url."""
        return url_for('user_blueprint.get_user', id=self.id, _external=True)

    def __init__(self, data):
        """User constructor."""
        try:
            self.name = data['name']
            self.json_field = data['json']
        except KeyError as e:
            raise Exception('Invalid user: missing ' + e.args[0])

    def export_data(self):
        """Export user data object."""
        return {
            'name': self.name,
            'date_created': self.date_created,
            'date_modified': self.date_modified,
            'json': self.json_field,
            'email': self.email
        }

    def __repr__(self):
        """Representation for user object."""
        return self.name
