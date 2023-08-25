#from models.admin import Admin
#from models.cars import Car
#from models.customers import Customer
#from models.reservations import Reservation

from api.v1.app import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Configure your SQLAlchemy and other app settings
app.config['SECRET_KEY'] = 'customer_pwd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username@localhost/car_rent'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
