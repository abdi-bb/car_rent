from flask import Blueprint, render_template

reservation_bp = Blueprint('reservation', __name__)

@reservation_bp.route('/')
def index():
    return render_template('reservation/index.html')

@reservation_bp.route('/list')
def list_reservations():
    return render_template('reservation/list.html')

'''
from flask import Blueprint, render_template

reservations_bp = Blueprint('reservations', __name__, url_prefix='/reservations')

@reservations_bp.route('/')
def reservation_list():
    # Fetch reservations data from models and pass it to the template
    reservations = []  # Replace with actual reservations data
    return render_template('reservations/list.html', reservations=reservations)

# More routes and view functions specific to reservations
'''
