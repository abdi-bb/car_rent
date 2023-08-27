from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from car_rent_app.auth import login_required
from car_rent_app.db import get_db

bp = Blueprint('customer', __name__)

@bp.route('/')
def index():
    db = get_db()
    customers = db.execute(
        'SELECT customer.username, customer.name, customer.email'
        ' ORDER BY name DESC'
    ).fetchall()
    return render_template('customer/index.html', customers=customers)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        password = request.form['password']
        address = request.form['address']
        error = None

        if not username:
            error = 'Username is required.'
        if not name:
            error = 'Name is required'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO customer (username, name, last_name, phone_number, email, password, address, admin_id)'
                ' VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                (username, name, last_name, phone_number, email, password, address, g.admin['id'])
            )
            db.commit()
            return redirect(url_for('customer.index'))

    return render_template('customer/create.html')
