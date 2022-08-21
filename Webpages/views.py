# This file stores all the views and the frontend of the website
'''
This file has the routes of all the pages where the 
user would be going
'''

from flask import Blueprint , render_template , flash , request

from flask_login import login_required , current_user

from .models import Note
from . import db

views = Blueprint('views' , __name__);

# Tells that we need to have a previous login to redirect to this page
@views.route('/' , methods = ["GET" , "POST"])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get("note");

        if len(note) < 1:
            flash("Note is too short to be noted!" , category="error")
        else :
            new_note = Note(data = note , user_id = current_user.id);
            db.session.add(new_note);
            db.session.commit();
            flash("Note Added!" , category="success")

    return render_template("home.html" , user = current_user);


