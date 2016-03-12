from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config.development')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Import a module / component
from .user import user_blueprint

# Register blueprint(s)
app.register_blueprint(user_blueprint)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()