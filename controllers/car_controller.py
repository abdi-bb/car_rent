from flask import Blueprint, render_template

car_bp = Blueprint('car', __name__)

@car_bp.route('/')
def index():
    return render_template('car/index.html')

@car_bp.route('/list')
def list_cars():
    return render_template('car/list.html')

'''
from flask import Blueprint, render_template

cars_bp = Blueprint('cars', __name__, url_prefix='/cars')

@cars_bp.route('/')
def car_list():
    # Fetch cars data from models and pass it to the template
    cars = []  # Replace with actual cars data
    return render_template('cars/list.html', cars=cars)

# More routes and view functions specific to cars
'''
