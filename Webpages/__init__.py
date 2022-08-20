# This file makes this website a complete package
# Content of this folder can would be running as soon as we initiate this fie

'''
This actually means that we have created a package of the Webpages folder and hence
It can be imported as a package with the package name as Webpages

To take the content below:
from Webpages import initiate_app()
'''

from flask import Flask

def initiate_app():
    app = Flask(__name__);
    app.config['SECRET_KEY'] = "ifyoureadthisyoushouldn'tbehere"

    from .views import views
    from .auth import auth

    app.register_blueprint(views , url_prefix = "/")
    app.register_blueprint(auth , url_prefix = "/")

    return app;