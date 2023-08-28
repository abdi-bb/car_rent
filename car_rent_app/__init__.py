import os

from flask import Flask
from flask import render_template, url_for

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'car_rent_app.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Wel come
    @app.route('/')
    def hello():
        return render_template('index.html')

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)
    app.add_url_rule('/', endpoint='login')

    from . import admin
    app.register_blueprint(admin.bp)
    app.add_url_rule('/', endpoint='index')

    from . import car
    app.register_blueprint(car.bp)
    app.add_url_rule('/', endpoint='index')

    from . import customer
    app.register_blueprint(customer.bp)
    app.add_url_rule('/', endpoint='index')

    from . import reservation
    app.register_blueprint(reservation.bp)
    app.add_url_rule('/', endpoint='index')

    return app
