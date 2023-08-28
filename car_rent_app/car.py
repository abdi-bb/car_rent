from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from car_rent_app.auth import login_required
from car_rent_app.db import get_db

bp = Blueprint('car', __name__)

@bp.route('/')
def index():
    return 'This is car index page'
    db = get_db()
    cars = db.execute(
        'SELECT car.name, car.model, car.seat, car.image'
        ' ORDER BY model DESC'
    ).fetchall()
    return render_template('car/index.html', cars=cars)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        name = request.form['name']
        model = request.form['model']
        error = None

        if not name:
            error = 'Name is required.'
        if not model:
            error = 'Model is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO car (name, model, admin_id)'
                ' VALUES (?, ?, ?)',
                (name, model, g.admin['id'])
            )
            db.commit()
            return redirect(url_for('car.index'))

    return render_template('car/create.html')


def get_car(id, check_author=True):
    car = get_db().execute(
        'SELECT ca.id, name, model, seat, image, admin_id'
        ' FROM car ca JOIN admin ad ON ca.admin_id = ad.id'
        ' WHERE ca.id = ?',
        (id,)
    ).fetchone()

    if car is None:
        abort(404, f"Car id {id} doesn't exist.")

    if check_author and car['admin_id'] != g.admin['id']:
        abort(403)

    return car


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    car = get_car(id)

    if request.method == 'POST':
        name = request.form['name']
        model = request.form['model']
        error = None

        if not name:
            error = 'Name is required.'
        if not model:
            error = 'Model is required.'

        if error is not None:
            flash(error)

        else:
            db = get_db()
            db.execute(
                'UPDATE car SET name = ?, model = ?'
                ' WHERE id = ?',
                (name, model, id)
            )
            db.commit()
            return redirect(url_for('car.index'))

    return render_template('car/update.html', car=car)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_car(id)
    db = get_db()
    db.execute('DELETE FROM car WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('car.index'))
