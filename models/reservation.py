from app import db

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<Reservation {}>'.format(self.id)
