# This file makes this website a complete package
# Content of this folder can would be running as soon as we initiate this fie

'''
This actually means that we have created a package of the Webpages folder and hence
It can be imported as a package with the package name as Webpages

To take the content below:
from Webpages import initiate_app()
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy();
DB_NAME = "database.db";

def create_database(app):
    if not path.exists("Webpages/" + DB_NAME):
        db.create_all(app = app);
        print("Database Created")

def initiate_app():
    app = Flask(__name__);
    app.config['SECRET_KEY'] = "ifyoureadthisyoushouldn'tbehere"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init_app(app);

    from .views import views
    from .auth import auth

    app.register_blueprint(views , url_prefix = "/")
    app.register_blueprint(auth , url_prefix = "/")

    # Importing Database Classes
    from .models import Note , User

    create_database(app);

    return app;