from . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__='accounts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(100), index=True, unique=True, nullable=False)
    address = db.Column(db.String(100), index=True, unique=True, nullable=False)
    
class Events(db.Model):
    __tablename__='events'
    creatorName = db.Column(db.String(100), primary_key=True, unique=True)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    eventName = db.Column(db.String(100), index=True, nullable=False)
    category = db.Column(db.String(100), index=True, nullable=False)
    description = db.Column(db.VARCHAR, index=True, nullable=False)
    date = db.Column(db.String(100), index=True, nullable=False)
    time = db.Column(db.String(100), index=True, nullable=False)
    location = db.Column(db.String(100), index=True, nullable=False)
    #Amount of tickets to buy
    ticketlimit = db.Column(db.Integer, index=True, nullable=False)
    price = db.Column(db.Float, index=True, nullable=False)
    t_d = db.Column(db.Boolean, index=True, nullable=False)
