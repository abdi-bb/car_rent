#!/usr/bin/python
""" holds class Admin"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


class Admin(models.db.Model, UserMixin):
    __tablename__ = 'admin'
    id = models.db.Column(models.db.Integer, primary_key=True)
    name = models.db.Column(models.db.String(50), nullable=False)
    username = models.db.Column(models.db.String(50), unique=True, nullable=False)
    email = models.db.Column(models.db.String(100), unique=True, nullable=False)
    password = models.db.Column(models.db.String(100), nullable=False)

    cars = models.db.relationship('Car', backref='admin', lazy=True)
    customers = models.db.relationship('Customer', backref='admin', lazy=True)
    reservations = models.db.relationship('Reservation', backref='admin', lazy=True)

    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password

    def __str__(self):
        return self.usename

    def __str__(self):
        return self.username

    def is_active(self):
        return True
    def get_id(self):
        return self.id
    def check_password(self, password):
        return self.password == password
