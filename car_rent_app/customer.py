import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort
from werkzeug.security import check_password_hash, generate_password_hash

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

# # This is customer registration controller
# @bp.route('/register', methods=('GET', 'POST'))
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         name = request.form['name']
#         last_name = request.form['last_name']
#         phone_number = request.form['phone_number']
#         email = request.form['email']
#         password = request.form['password']
#         address = request.form['address']
#         error = None

#         if not username:
#             error = 'Username is required.'
#         if not name:
#             error = 'Name is required'

#         if error is not None:
#             flash(error)
#         else:
#             db = get_db()
#             db.execute(
#                 'INSERT INTO customer (username, name, last_name, phone_number, email, password, address, admin_id)'
#                 ' VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
#                 (username, name, last_name, phone_number, email, password, address, g.admin['id'])
#             )
#             db.commit()
#             return redirect(url_for('customer.index'))

#     return render_template('customer/register.html')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        last_name = request.form['last_name']
        address = request.form['address']
        phone_number = request.form['phone_number']
        email = request.form['email']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not name:
            error = 'Name is required.'
        elif not last_name:
            error = 'Last Name is required.'
        elif not address:
            error = 'Address is required.'
        elif not phone_number:
            error = 'Phone Number is required.'
        elif not email:
            error = 'Email is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO customer (username, name, last_name, address, phone_number, email,  password) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (username, name, last_name, address, phone_number, email, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError as er:
                print(er)
#                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('customer/register.html')

# Customer login
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        customer = db.execute(
                'SELECT * FROM customer WHERE username = ?', (username,)
        ).fetchone()

        if customer is None:
            error = 'Incorrect username.'
        elif not check_password_hash(customer['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['customer_id'] = customer['id']
            return redirect(url_for('customer.index'))

        flash(error)

    return render_template('customer/login.html')

# Get logged in customer
@bp.before_app_request
def load_logged_in_customer():
    customer_id = session.get('customer_id')

    if customer_id is None:
        g.customer = None
    else:
        g.customer = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (customer_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.customer is None:
            return redirect(url_for('customer.login'))

        return view(**kwargs)

    return wrapped_view

# Create customer(admin only)
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


def get_customer(id, check_author=True):
    customer = get_db().execute(
        'SELECT cu.id, usename, name, email, admin_id'
        ' FROM customer cu JOIN admin ad ON cu.admin_id = ad.id'
        ' WHERE cu.id = ?',
        (id,)
    ).fetchone()

    if customer is None:
        abort(404, f"Customer id {id} doesn't exist.")

    if check_author and customer['admin_id'] != g.admin['id']:
        abort(403)

    return customer


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    customer = get_customer(id)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        error = None

        if not name:
            error = 'Name is required.'

        if not email:
            error = 'Email is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE customer SET name = ?, email = ?'
                ' WHERE id = ?',
                (name, email, id)
            )
            db.commit()
            return redirect(url_for('customer.index'))

    return render_template('customer/update.html', customer=customer)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_customer(id)
    db = get_db()
    db.execute('DELETE FROM customer WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('customer.index'))
