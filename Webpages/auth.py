# This file deals with the authentication of the users

from flask import Blueprint , render_template , request , flash , redirect , url_for
from .models import User

from . import db

# Hashing a password
from werkzeug.security import generate_password_hash , check_password_hash

from Webpages.models import User

auth = Blueprint('auth' , __name__);

@auth.route("/login" , methods = ["GET" , "POST"])
def login():
    data = request.form;
    print(data);
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return render_template("logout.html")

@auth.route("/sign-up" , methods = ["GET" , "POST"])
def signun():
    if request.method == "POST":
        email = str(request.form.get("email"));
        firstName = str(request.form.get("firstName"));
        password1 = str(request.form.get("password1"));
        password2 = str(request.form.get("password2"));

        if len(email) < 4:
            flash("Please check your email address once again" , category = "error");
        elif len(firstName) < 2:
            flash("Please check your name once again" , category = "error");
        elif password1 != password2:
            flash("Passwords don't match. Please check again!" , category = "error");
        elif len(password1) < 7:
            flash("Passwords is too short! Please enter a password greater than 7 characters" , category = "error");
        else :
            new_user = User(email = email , firstName = firstName , password = generate_password_hash(password1 , method = "sha256"));
            db.session.add(new_user);
            db.session.commit()
            flash("Great! Relax and Take Notes :)" , category = "success");

            return redirect(url_for("views.home"))

    return render_template("sign-up.html")
