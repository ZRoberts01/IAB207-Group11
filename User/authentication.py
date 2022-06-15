from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import LoginForm, RegisterForm
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash,check_password_hash
from .models import User
from . import db

bp = Blueprint('auth', __name__ )

#Registration
@bp.route('/register', methods=['GET','POST'])
def register():
    register = RegisterForm()
    if (register.validate_on_submit() == True):
                name = register.name.data
                pwd = register.password.data
                email=register.email_id.data
                Phone_Number=register.Phone_Number.data
                Address=register.Address.data
                u1 = User.query.filter_by(name).first()
                if u1:
                    flash('User name already exists, please login')
                    return redirect(url_for('auth.login'))
                pwd_hash = generate_password_hash(pwd)
                new_user = User(name, password_hash=pwd_hash, emailid=email, phone_number=Phone_Number, address = Address)
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for('auth.login'))
    else:
        return render_template('user.html', form=register, heading='Register')




@bp.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    error=None
    if(login_form.validate_on_submit()==True):
            #get the username and password from the database
            user_name = login_form.user_name.data
            password = login_form.password.data
            u1 = User.query.filter_by(name=user_name).first()
            #if there is no user with that name
            if u1 is None:
                error='Incorrect user name'
            #check the password - notice password hash function
            elif not check_password_hash(u1.password_hash, password): # takes the hash and password
                error='Incorrect password'
            if error is None:
                #all good, set the login_user of flask_login to manage the user
                login_user(u1)
                return redirect(url_for('main.index'))
            else:
                flash(error)
    return render_template('user.html', form=login_form, heading='Login')





@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return 'You have been logged out'