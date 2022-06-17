from flask import Blueprint,render_template, redirect, url_for, request, flash
from .forms import LoginForm, RegisterForm
from . import db
# from .models import users, User
from flask_login import login_required, current_user

mainbp = Blueprint('main', __name__)

@mainbp.route('/user', methods = ['GET', 'POST'])
def login():
    error = None
    email = request.values.get("email")
    password = request.values.get("password")
    print ("email: {}\npassword= {}".format(email,password))
    return render_template('user.html')


