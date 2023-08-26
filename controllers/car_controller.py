from flask import Blueprint, render_template

car_bp = Blueprint('car', __name__)

@car_bp.route('/')
def index():
    return render_template('car/index.html')

@car_bp.route('/list')
def list_cars():
    return render_template('car/list.html')
