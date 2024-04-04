from app import db


class PledgeSign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(150))
    promo_email = db.Column(db.Boolean, default=False)
    profession = db.Column(db.String(100))
    sign_name = db.Column(db.String(100))
    certification = db.Column(db.String(1000))
    sector = db.Column(db.String(100))
    age = db.Column(db.String(15))
    gender = db.Column(db.String(100))
    race = db.Column(db.String(100))
    ethn_hisp = db.Column(db.String(5))
