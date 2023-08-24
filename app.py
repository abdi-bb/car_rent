from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from views.admin import admin_bp
from views.cars import cars_bp
from views import customers_bp
from views.reservations import reservations_bp

app = Flask(__name__)

# Configure your SQLAlchemy and other app settings
app.config['SECRET_KEY'] = 'customer_pwd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username@localhost/car_rent'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

#from views import admin_bp, cars_bp, customers_bp, reservations_bp

# Register blueprints
app.register_blueprint(admin_bp)
app.register_blueprint(cars_bp)
app.register_blueprint(customers_bp)
app.register_blueprint(reservations_bp)

'''@app.route('/')

def home():
    return render_template('index.html')
'''
# More routes and view functions for other parts of your app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
