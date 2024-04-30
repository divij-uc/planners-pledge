from app import app, db
from app.forms import SignForm
from app.models import PledgeSign
from flask import render_template, redirect, url_for, session, request, flash


def name_fix(name):
    if name.isupper():
        return name.title()
    return name


@app.route("/", methods=["GET"])
def start_page():
    return render_template("start_page.html")


@app.route("/background", methods=["GET"])
def background_page():
    return render_template("background_page.html")


@app.route("/faqs", methods=["GET"])
def faq_page():
    return render_template("faq_page.html")

@app.route("/signatories", methods=["GET"])
def signatory_page():
    sign = request.args.get('sign', type=bool, default=False)
    signatories = PledgeSign.query.all()
    id_names = [(s.id, name_fix(s.sign_name)) for s in signatories]
    return render_template("signatory_page.html", sign=sign, id_names=id_names)


@app.route("/sign_form", methods=["GET", "POST"])
def sign_form():
    signform = SignForm()
    if signform.validate_on_submit():
        pledge_sign = PledgeSign()
        signform.populate_obj(pledge_sign)
        pledge_sign.certification = "; ".join(pledge_sign.certification)
        pledge_sign.race = "; ".join(pledge_sign.race)
        if signform.sector_other.data:
            pledge_sign.sector += "; " + signform.sector_other.data
        if signform.profession_other.data:
            pledge_sign.profession += "; " + signform.profession_other.data
        if signform.gender_other.data:
            pledge_sign.gender += "; " + signform.gender_other.data
        if signform.race_other.data:
            pledge_sign.race += signform.race_other.data
        if signform.certification_other.data:
            pledge_sign.certification += signform.certification_other.data
        
        db.session.add(pledge_sign)
        db.session.commit()
        return redirect(url_for("signatory_page", sign = True))
    else:
        if signform.errors:
            flash(signform.errors)
    return render_template("sign_form_page.html", signform=signform)
