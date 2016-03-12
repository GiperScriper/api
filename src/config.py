import os
# Statement for enabling the development environment
DEBUG = True

# Define the application directory

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://localhost/api'
SQLALCHEMY_TRACK_MODIFICATIONS = False
