from flask import Flask,jsonify
from flask_restful import Resource,Api,reqparse
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import json
app = Flask(__name__)
api = Api(app)


register_args = reqparse.RequestParser()
register_args.add_argument("username",type = str, help = "Type your username")
register_args.add_argument("password",type = str, help = "Type your password")
register_args.add_argument("clientid",type = str, help = "Discord client ID")
register_args.add_argument("iqemail",type = str,help = "IQ OPTION EMAIL")


# connecting to mongodb
client = MongoClient("mongodb+srv://jeanpaulsb:tomyandres12@cluster0.jo1qw9s.mongodb.net/test")

db = client.users
collection = db.users


users = {}
class Register(Resource):
    # args :
    # username
    # password
    # discord client id
    def post(self):
        args = register_args.parse_args()
        try:
            collection.insert_one(dict(args))
        except DuplicateKeyError:
            return {"message":"this username is not available!"}

        return {"message": "welcome to iqoption BOT! "}

api.add_resource(Register,"/register")



app.run(debug = True)