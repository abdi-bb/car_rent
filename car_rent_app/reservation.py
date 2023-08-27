from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from car_rent_app.auth import login_required
from car_rent_app.db import get_db

bp = Blueprint('reservation', __name__)

@bp.route('/')
def index():
    db = get_db()
    reservation = db.execute(
        'SELECT r.id pickup_time, dropoff_time, customer_name, email, customer_id'
        ' FROM reservation r JOIN customer cu ON r.customer_id = cu.id'
        ' ORDER BY pickup_time ASC'
    ).fetchall()
    return render_template('reservation/index.html', reservations=reservations)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        email = request.form['email']
        error = None

        if not customer_name:
            error = 'Customer name is required.'
        if not email:
            error = 'Email is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO reservation (customer_name, email, customer_id)'
                ' VALUES (?, ?, ?)',
                (customer_name, email, g.customer['id'])
            )
            db.commit()
            return redirect(url_for('reservation.index'))

    return render_template('reservation/create.html')


def get_reservation(id, check_author=True):
    reservation = get_db().execute(
        'SELECT r.id, customer_name, pickup_time, dropoff_time, customer_id'
        ' FROM reservation r JOIN customer cu ON r.customer_id =cu.id'
        ' WHERE r.id = ?',
        (id,)
    ).fetchone()

    if reservation is None:
        abort(404, f"Reservation id {id} doesn't exist.")

    if check_author and reservation['admin_id'] != g.customer['id']:
        abort(403)

    return reservation


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    reservation = get_reservation(id)

    if request.method == 'POST':
        customer_name = request.form['customer_name']
        email = request.form['email']
        error = None

        if not customer_name:
            error = 'Customer name is required.'
        if not email:
            error = 'Email is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE reservation SET customer_name = ?, email = ?'
                ' WHERE id = ?',
                (customer_name, email, id)
            )
            db.commit()
            return redirect(url_for('reservation.index'))

    return render_template('reservation/update.html', reservation=reservation)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_reservation(id)
    db = get_db()
    db.execute('DELETE FROM reservation WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('reservation.index'))
