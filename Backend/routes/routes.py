from flask_restful import Api, Resource
from flask import request
from db.models import *
class Book(Resource):
    def get(self):
        return {"data": {
            "name": "wilson",
            "id": "123"}, "meta": "sdfsdf" }

class Foo(Resource):
    def post(self):
        new_entry = doo(
            product = request.json['product']
        )
        print(request.json)
        db.session.add(new_entry)
        db.session.commit()
