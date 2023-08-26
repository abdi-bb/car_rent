from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base_model import BaseModel, Base
from flask_login import UserMixin
from app import db

class Admin(db.Model, UserMixin):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    cars = db.relationship('Car', backref='admin', lazy=True)
    customers = db.relationship('Customer', backref='admin', lazy=True)
    reservations = db.relationship('Reservation', backref='admin', lazy=True)

    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<Admin {}>'.format(self.username)

    def is_active(self):
        return True
    def get_id(self):
        return self.id
    def check_password(self, password):
        return self.password == password
