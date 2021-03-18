from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class User(db.Model):
    __tablename__ = 'User'
    uuid = db.Column(db.String(128), primary_key=True)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    images = db.relationship('ImageEntry')


class ImageEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.Text,  nullable=False)
    mime_type = db.Column(db.Text, nullable=False)
    file_name = db.Column(db.Text, nullable=False)
    image_path = db.Column(db.Text, nullable=False)
    favorite = db.Column(db.Boolean)
    user_id = db.Column(db.String(128), db.ForeignKey('User.uuid'), nullable=False)
