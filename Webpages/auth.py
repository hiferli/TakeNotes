# This file deals with the authentication of the users

from flask import Blueprint , render_template , request , flash

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
            flash("Great! Relax and Take Notes :)" , category = "success");

    return render_template("sign-up.html")
