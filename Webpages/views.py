# This file stores all the views and the frontend of the website
'''
This file has the routes of all the pages where the 
user would be going
'''

from flask import Blueprint , render_template

from flask_login import login_required , current_user

views = Blueprint('views' , __name__);

# Tells that we need to have a previous login to redirect to this page
@views.route('/' , methods = ["GET" , "POST"])
@login_required
def home():
    return render_template("home.html" , user = current_user);


