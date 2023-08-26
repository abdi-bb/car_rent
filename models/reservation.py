from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base_model import Base
from app import db

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

#    car_id = db.Column(db.Integer, db.ForeignKey('car.id'))

    def __repr__(self):
        return '<Reservation {}>'.format(self.id)
