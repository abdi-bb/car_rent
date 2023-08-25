#!/usr/bin/python3

import os
from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
'''The Flask web application instance.'''
app_host = os.getenv('HBNB_API_HOST', '0.0.0.0')
app_port = int(os.getenv('HBNB_API_PORT', '5000'))
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
CORS(app, resources={'/*': {'origins': app_host}})

# Configure your SQLAlchemy and other app settings
#app.config['SECRET_KEY'] = 'customer_pwd'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username@localhost/car_rent'


#from views import admin_bp, cars_bp, customers_bp, reservations_bp

# Register blueprints
#app.register_blueprint(admin_bp)
#app.register_blueprint(cars_bp)
#app.register_blueprint(customers_bp)
#app.register_blueprint(reservations_bp)

'''@app.route('/')

def home():
    return render_template('index.html')
'''
# More routes and view functions for other parts of your app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
