from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base_model import BaseModel, Base
from app import db

class Car(db.Model):
    __tablename__ = 'car'
    car_id = db.Column(db.Integer, primary_key=True)
    car_name = db.Column(db.String(100), nullable=False)
    car_model = db.Column(db.String(100), nullable=False)
    car_status = db.Column(db.String(20), nullable=False)
    car_seat = db.Column(db.Integer, nullable=False)
    car_door = db.Column(db.Integer, nullable=False)
    car_gearbox = db.Column(db.String(20), nullable=False)
    car_image = db.Column(db.String(100))
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.admin_id'))

    reservations = db.relationship('Reservation', backref='car', lazy=True)

    def __repr__(self):
        return '<Car {}>'.format(self.make + ' ' + self.model)
