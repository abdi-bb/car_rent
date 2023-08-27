from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from car_rent_app.auth import login_required
from car_rent_app.db import get_db

bp = Blueprint('admin', __name__)

@bp.route('/')
def index():
    db = get_db()
    orders = db.execute(
        'SELECT ca.id, name, model, customer_id'
        ' FROM car ca JOIN customer cu ON ca.customer_id = cu.id'
        ' ORDER BY pickup_time ASC'
    ).fetchall()
    return render_template('admin/index.html', orders=orders)
