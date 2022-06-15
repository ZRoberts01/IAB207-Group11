from flask import Flask
from User import create_app

if __name__=='__main__':
    n_app=create_app()
    n_app.run(debug=True)