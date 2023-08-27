from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from car_rent_app.auth import login_required
from car_rent_app.db import get_db

bp = Blueprint('reservation', __name__)
