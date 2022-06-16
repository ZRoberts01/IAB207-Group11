from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, BooleanField, FileField, DateField, TimeField, IntegerField 
from wtforms.validators import InputRequired, Length, Email, EqualTo

#Login Form
class LoginForm(FlaskForm):
    user_name=StringField("Username", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit=SubmitField("Login")

#Register Form
class RegisterForm(FlaskForm):
    user_Name=StringField("User Name", validators=[InputRequired()])

    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    #Password Creation and confirmation
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Re-enter Password")])
    confirm = PasswordField("Confirm Password")
    #Phone Number
    Phone_Number=StringField("Phone Number", validators=[InputRequired()])
    #Address
    Address=StringField("Address", validators=[InputRequired()])
    #Submit Details
    submit = SubmitField("Register")

#Create Event Form
class EventForm(FlaskForm):
    creatorName = StringField('Company/Creator Name', validators=[InputRequired()])
    email = StringField('Email Address', validators=[InputRequired()])
    eventName = StringField('Event Name', validators=[InputRequired()])
    image = FileField('Event Banner', validators=[InputRequired()])
    category = StringField('Event Category', validators=[InputRequired()])
    description = TextAreaField('Event Description', validators=[InputRequired()])
    date = DateField('Event Date', validators=[InputRequired()])
    time = TimeField('Event Time', validators=[InputRequired()])
    location = StringField('Event Address', validators=[InputRequired()])
    ticketlimit = IntegerField('Booking Limit', validators=[InputRequired("Please use numbers only")])
    price = StringField('Ticket Price', validators=[InputRequired()])
    t_d = BooleanField('I accept all terms and conditions', validators=[InputRequired()])
    submit = SubmitField('Create Event')