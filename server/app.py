from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
CORS(app)


users = [
    {
        "name": "Matt",
        "age": 20
    },
    {
        "name": "Christina",
        "age": 19
    }
]

class User(Resource):
    def get(self, name):
        for user in users:
            if (name == user["name"]):
                return user, 200
        return "User not found", 404
        
api.add_resource(User, "/user/<string:name>")
app.run(debug=True)
