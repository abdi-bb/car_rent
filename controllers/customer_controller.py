from flask import Blueprint, render_template

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/')
def index():
    return render_template('customer/index.html')

@customer_bp.route('/list')
def list_customers():
    return render_template('customer/list.html')
