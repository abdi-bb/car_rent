#!/usr/bin/python3
'''
Module: 'customers'
'''

from api.v1.views import app_views
from models.customers import Customer
from flask import Blueprint, render_template, request, redirect, url_for, session
from sqlalchemy.orm import sessionmaker
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash


@app_views.route('/customers')
def customer_list():
    # Fetch customers data from models and pass it to the template
    customers = []  # Replace with actual customers data
    return render_template('customers/customer_list.html', customers=customers)

@app_views.route('/customers/login', methods=['GET', 'POST'])
def customer_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        customer = Customer.query.filter_by(email=email).first()
        if customer and check_password_hash(customer.password, password):
            login_user(customer)
            return redirect(url_for('cars.car_list'))

        return 'Invalid email or password'
    
    return render_template('customers/customer_login.html')

@app_views.route('/customers/logout')
@login_required
def customer_logout():
    logout_user()
    return redirect(url_for('customers.customer_login'))

from app import login_manager
@login_manager.user_loader
def load_user(user_id):
    return Customer.query.get(int(user_id))

# More routes and view functions specific to customers
