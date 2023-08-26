from flask import Blueprint, render_template

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/')
def index():
    return render_template('admin/index.html')

@admin_bp.route('/users')
def users():
    return render_template('admin/users.html')
