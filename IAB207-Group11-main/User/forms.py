from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
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