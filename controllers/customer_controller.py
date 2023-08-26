from flask import Blueprint, render_template

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/')
def index():
    return render_template('customer/index.html')

@customer_bp.route('/list')
def list_customers():
    return render_template('customer/list.html')

'''
from flask import Blueprint, render_template, request, redirect, url_for, session
from sqlalchemy.orm import sessionmaker
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

customers_bp = Blueprint('customers', __name__, url_prefix='/customers')


@customers_bp.route('/')
def customer_list():
    # Fetch customers data from models and pass it to the template
    customers = []  # Replace with actual customers data
    return render_template('customers/customer_list.html', customers=customers)

@customers_bp.route('/login', methods=['GET', 'POST'])
def customer_login():
    from models.customers import Customer
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        customer = Customer.query.filter_by(email=email).first()
        if customer and check_password_hash(customer.password, password):
            login_user(customer)
            return redirect(url_for('cars.car_list'))

        return 'Invalid email or password'

    return render_template('customers/customer_login.html')

@customers_bp.route('/logout')
@login_required
def customer_logout():
    logout_user()
    return redirect(url_for('customers.customer_login'))

from app import login_manager
@login_manager.user_loader
def load_user(user_id):
    from models.customers import Customer
    return Customer.query.get(int(user_id))

# More routes and view functions specific to customers
'''
