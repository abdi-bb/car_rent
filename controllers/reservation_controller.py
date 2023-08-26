from flask import Blueprint, render_template

reservation_bp = Blueprint('reservation', __name__)

@reservation_bp.route('/')
def index():
    return render_template('reservation/index.html')

@reservation_bp.route('/list')
def list_reservations():
    return render_template('reservation/list.html')
