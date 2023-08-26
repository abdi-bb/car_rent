from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from controllers.admin_controller import admin_bp
from controllers.car_controller import car_bp
from controllers.customer_controller import customer_bp
from controllers.reservation_controller import reservation_bp

app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(car_bp, url_prefix='/car')
app.register_blueprint(customer_bp, url_prefix='/customer')
app.register_blueprint(reservation_bp, url_prefix='/reservation')

if __name__ == '__main__':
    app.run()
