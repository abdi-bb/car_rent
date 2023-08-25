#!/usr/bin/python3
""" holds class Reservation"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from flask_sqlalchemy import SQLAlchemy


class Reservation(db.Model):
    __tablename__ = 'reservation'
    order_id = db.Column(db.Integer, primary_key=True)
    pickup_time = db.Column(db.DateTime, nullable=False)
    dropoff_time = db.Column(db.DateTime, nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.admin_id'))
