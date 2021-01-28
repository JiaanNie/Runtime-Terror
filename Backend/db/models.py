from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class ImageEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.Text,  nullable=False)
    mime_type = db.Column(db.Text, nullable=False)
    file_name = db.Column(db.Text, nullable=False)
    image_path = db.Column(db.Text, nullable=False)
