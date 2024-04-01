from app import app, db
from app.forms import SignForm
from app.models import PledgeSign
from flask import render_template, redirect, url_for, session, request, flash


@app.route("/", methods=["GET", "POST"])
def start_page():
    return render_template("start_page.html")


@app.route("/background", methods=["GET", "POST"])
def background_page():
    return render_template("background_page.html")


@app.route("/faqs", methods=["GET", "POST"])
def faq_page():
    return render_template("faq_page.html")


@app.route("/thanks", methods=["GET", "POST"])
def thank_page():
    return render_template("thank_page.html")


@app.route("/sign_form", methods=["GET", "POST"])
def sign_form():
    signform = SignForm()
    if signform.validate_on_submit():
        pledge_sign = PledgeSign()
        signform.populate_obj(pledge_sign)
        db.session.add(pledge_sign)
        db.session.commit()
        return redirect(url_for("thank_page"))
    else:
        if signform.errors:
            flash(signform.errors)
    return render_template("sign_form_page.html", signform=signform)
