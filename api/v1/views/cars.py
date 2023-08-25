#!/usr/bin/python3
'''
Module: 'cars'
'''

from flask import request, abort, render_template
from api.v1.views import app_views
from models.cars import Car


@app_views.route('/')
def car_list():
    # Fetch cars data from models and pass it to the template
    cars = []  # Replace with actual cars data
    return render_template('cars/list.html', cars=cars)

# More routes and view functions specific to cars
