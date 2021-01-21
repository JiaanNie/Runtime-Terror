from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class boo(db.Model):
    name = db.Column(db.String(20))
    id = db.Column(db.Integer, primary_key=True)

class doo(db.Model):
    product = db.Column(db.String(20))
    id = db.Column(db.Integer, primary_key=True)
