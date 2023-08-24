from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from app import db
from flask_login import UserMixin

class Customer(db.Model, UserMixin):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.admin_id'))

    # Define a backref to access reservations made by this customer
    reservations = relationship('Reservation', backref='customer', lazy='dynamic')

    def __init__(self, username, name, last_name, phone_number, email, password, address):
        self.username = username
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.password = password
        self.address = address

    def __str__(self):
        return self.username

    def is_active(self):
        return True
    def get_id(self):
        return self.id
    def check_password(self, password):
        return self.password == password
