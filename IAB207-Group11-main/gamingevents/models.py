from . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    first_name = db.Column(db.String(100), index=True, nullable = False)
    last_name = db.Column(db.String(100), index=True, nullable = False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(100), index=True, unique=True, nullable=False)
    address = db.Column(db.String(100), index=True, unique=True, nullable=False)
    
    comments = db.relationship('Comment', backref='user')
    events = db.relationship('Event', secondary='comments', backref=db.backref('commented_users'))
    
class Event(db.Model):
    __tablename__='events'
    id = db.Column(db.Integer, primary_key=True)
    eventName = db.Column(db.String(100))
    description = db.Column(db.String(250))
    image = db.Column(db.String(400))
    category = db.Column(db.String(100))
    date = db.Column(db.String(100))
    time = db.Column(db.String(100))
    location = db.Column(db.String(100))
    t_d = db.Column(db.Boolean, index=True, nullable=False)
    
    bookings = db.relationship('Booking', backref='event')
    comments = db.relationship('Comment', backref='event')

    def __repr__(self):
            return "<Name: {}>".format(self.name)

class Comment(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    timestamp = db.Column(db.DateTime(), default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    def __repr__(self):
        return "<Comment: {}>".format(self.text)

class Booking(db.Model):
    __tablename__ = 'booking' 
    id = db.Column(db.Integer, primary_key = True)
    eventName = db.Column(db.String(100))
    num_tickets = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Float(), index=True, nullable=False)
    date = db.Column(db.String(100))
    time = db.Column(db.String(100))

    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
