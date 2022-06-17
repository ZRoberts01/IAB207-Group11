from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()
app=Flask(__name__)

def create_app():
    bootstrap = Bootstrap(app)

    app.secret_key='somerandomvalue'

    #database
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///gamingevents.sqlite'


    #start database
    db.init_app(app)

    #login manager
    login_manager = LoginManager()
    login_manager.login_view='main.login'
    login_manager.init_app(app)
    
    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    #Blueprints
    from .views import mainbp
    app.register_blueprint(mainbp)
    
    return app


@app.errorhandler(404) 
# inbuilt function which takes error as parameter
def not_found(e): 
  return render_template("404.html")