from app import db

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(64), index=True)
    model = db.Column(db.String(64), index=True)
    year = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<Car {}>'.format(self.make + ' ' + self.model)
