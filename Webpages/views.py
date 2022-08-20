# This file stores all the views and the frontend of the website
'''
This file has the routes of all the pages where the 
user would be going
'''

from flask import Blueprint , render_template

views = Blueprint('views' , __name__);

@views.route('/')
def home():
    return render_template("home.html");