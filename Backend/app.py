from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
#from flask_sqlalchemy import SQLAlchemy
from db.models import *
from routes.routes import *
app = Flask(__name__)
cors =CORS(app)
api = Api(app)
#db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:1RTTDJ8GmeUSbUtJkQPH@localhost:3306/test'

db.init_app(app)
with app.app_context():
    db.create_all()
api.add_resource(Image, "/image", "/image/<image_id>")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug="True")
