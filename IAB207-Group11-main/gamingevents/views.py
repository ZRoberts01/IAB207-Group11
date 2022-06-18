from fileinput import filename
from tabnanny import check
from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from .forms import CommentsForm, LoginForm, RegisterForm, EventForm
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash,check_password_hash
from .models import User, Event, Comment
from . import db
from werkzeug.utils import secure_filename
import os

mainbp = Blueprint('main', __name__, url_prefix='/')

#Index Page
@mainbp.route('/')
def index():
    if 'name' in session:
        str='<h1>Welcome ' + session['name' + '</h1>']
    else:
        str='<h1>Welcome </h1>'
    events=Event.query.all()
    return render_template('index.html', events = events)

#Categories Page
@mainbp.route('/categories')
def category():
    return render_template('category.html')


#Event Details
@mainbp.route('/details')
def eventDetails():
    cform = CommentsForm()
    return render_template('eventDetails.html', form=cform)


#Comment
@mainbp.route('/comment', methods=['GET','POST'])
def Comment(event):
    form = CommentsForm()
    event_obj = Comment.query.filter_by(id = event).first()
    if form.validate_on_submit():
        comment = Comment(text=form.text.data, 
                            event=event_obj)
        db.session.add(comment)
        db.session.commit()
        print("Comment Submitted")
    return redirect(url_for('main.eventDetails.html'))
    


#User History Page
@mainbp.route('/userhistory')
def userHistory():
    return render_template('userHistory.html')

#Create Event
@mainbp.route('/eventCreation', methods = ['GET', 'POST'])
def eventCreation():
    print('Method type: ', request.method)
    form = EventForm()
    if form.validate_on_submit():
            db_file_path=check_upload_file(form)
            new_event = Event(eventName= form.eventName.data,
            description = form.description.data,
            image = db_file_path,
            category = form.category.data,
            date = form.date.data,
            time = form.date.data,
            location = form.location.data,
            num_tickets = form.num_tickets.data,
            price = form.price.data,
            t_d = form.t_d.data)
            db.session.add(new_event)
            db.session.commit()
            return redirect (url_for('main.index'))
    else:
        print("Nope")
        return render_template('eventCreation.html', form=form)

#Check file
def check_upload_file(form):
    fp=form.image.data
    filename=fp.filename
    BASE_PATH=os.path.dirname(__file__)
    upload_path=os.path.join(BASE_PATH, 'static/img', secure_filename(filename))
    db_upload_path='static/img/' + secure_filename(filename)
    fp.save(upload_path)
    return db_upload_path



#Registration
@mainbp.route('/register', methods=['GET','POST'])
def register():
    register = RegisterForm()
    if (register.validate_on_submit() == True):
            user_name = register.user_Name.data
            first_name = register.first_name.data
            last_name = register.last_name.data
            pwd = register.password.data
            email=register.email_id.data
            Phone_Number=register.Phone_Number.data
            Address=register.Address.data
            u1 = User.query.filter_by(user_name = user_name).first()
            if u1:
                flash('User name already exists')
                return redirect(url_for('main.login'))
            pwd_hash = generate_password_hash(pwd)
            new_user = User(user_name = user_name, 
                            first_name = first_name,    
                            last_name = last_name,  
                            password_hash=pwd_hash,     
                            emailid=email,  
                            phone_number=Phone_Number,  
                            address = Address)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('main.login'))
    else:
        return render_template('user.html', form=register, heading='Register')

#Login
@mainbp.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    error=None
    if(login_form.validate_on_submit()==True):
            #get the username and password from the database
            user_name = login_form.user_name.data
            password = login_form.password.data
            u1 = User.query.filter_by(user_name=user_name).first()
            if u1 is None:
                error='Incorrect user name'
            elif not check_password_hash(u1.password_hash, password):
                error='Incorrect password'
            if error is None:
                login_user(u1)
                return redirect(url_for('main.index'))
            else:
                flash(error)
    return render_template('user.html', form=login_form, heading='Login')

#Logout
@mainbp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))
