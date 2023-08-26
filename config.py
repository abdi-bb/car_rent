import os

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
# QLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@hostname/database'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://car_rent_user:car_rent_pwd@localhost/car_rent_db'

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
