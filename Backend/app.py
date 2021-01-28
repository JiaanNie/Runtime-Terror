from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
#from flask_sqlalchemy import SQLAlchemy
from db.models import *
from routes.routes import *
import config
app = Flask(__name__)
cors =CORS(app, resources={r'/*':{'origins':'*'}})
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = config.DatabaseURI()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
with app.app_context():
    db.create_all()
api.add_resource(Image, "/image", "/image/<image_id>")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug="True")
