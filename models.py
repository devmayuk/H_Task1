from db import db


class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)

class User(db.Model):
    label = db.Row(db.Integer, primary_key=True)
    image_cat_1 = db.Row(db.String(256))
    image_cat_2 = db.Row(db.String(256))
    value = db.Column(db.Integer, index=True)