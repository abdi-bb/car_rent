from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.route('/admin')
@login_required
def admin_home():
    return render_template('admin_home.html')

@admin_bp.route('/login', methods=['GET', 'POST'])
def admin_login():
    from models.admin import Admin
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        admin = Admin.query.filter_by(username=username).first()
        if admin and check_password_hash(admin.password, password):
            login_user(admin)
            return redirect(url_for('admin.admin_home'))
        
        return 'Invalid username or password'
    
    return render_template('admin/admin_login.html')

@admin_bp.route('/logout')
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for('admin.admin_login'))

from app import login_manager
@login_manager.user_loader
def load_user(user_id):
    from models.admin import Admin
    return Admin.query.get(int(user_id))
# More routes and view functions specific to admin panel
