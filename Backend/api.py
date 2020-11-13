from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
app = Flask(__name__)
cors =CORS(app)
api = Api(app)


class Book(Resource):
    def get(self):
        return {"data": {
            "name": "wilson",
            "id": "123"}, "meta": "sdfsdf" }

api.add_resource(Book, "/book")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug="True")
