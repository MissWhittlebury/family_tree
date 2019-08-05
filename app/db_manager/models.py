from app import db



class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    ##TODO(dwojtak): Make PhoneNumber Model
    phone_number = db.Column(db.String(20))
    email_address = db.Column(db.String(255))
    ##TODO(dwojtak): Make Address model
    address_id = db.Column(db.Integer)
    birth_date = db.Column(db.DateTime, nullable=False)
    ##TODO(dwojtak): set up relationship
    parents_id = db.Column(db.Integer, nullable=False)


class Parents(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ##TODO(dwojtak): Set up relationships
    mother_person_id = db.Column(db.Integer)
    father_person_id = db.Column(db.Integer)
