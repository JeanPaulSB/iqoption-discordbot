from flask import Flask,jsonify,make_response
from flask_restful import Resource,Api,reqparse
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import json
import secrets
app = Flask(__name__)
api = Api(app)


register_args = reqparse.RequestParser()
register_args.add_argument("username",type = str, help = "Type your username")
register_args.add_argument("password",type = str, help = "Type your password")
register_args.add_argument("clientid",type = str, help = "Discord client ID")
register_args.add_argument("iqemail",type = str,help = "IQ OPTION EMAIL")
register_args.add_argument("token",type = str, help = "Token credential for your bot session")

# connecting to mongodb
client = MongoClient("mongodb+srv://jeanpaulsb:tomyandres12@cluster0.jo1qw9s.mongodb.net/test")

db = client.users
collection = db.users

settings = client.settings
token = settings.token







class Register(Resource):
    # args :
    # username
    # password
    # discord client id
    
    def post(self):
        current_token = token.find_one()['token']
        args = register_args.parse_args()
        if args['token'] != current_token:
            return make_response(jsonify({'Message': 'Invalid Token'}),401)
        try:
            collection.insert_one(dict(args))
        except DuplicateKeyError:
            return make_response(jsonify({'Message': 'Username is not available'}),401)
        return make_response(jsonify({'Message': 'Sucess'}),200)


login_args = reqparse.RequestParser()
login_args.add_argument("username",type = str, help = "Type your username")
login_args.add_argument("password",type = str, help = "Type your password")
login_args.add_argument("iqemail",type = str,help = "IQ OPTION EMAIL")
class Login(Resource):
    def post(self):
        args = login_args.parse_args()
        obj = collection.find_one(args)
        if obj:
            return make_response(jsonify({'Message':'Login Sucess'}),200)
        else:
            return make_response(jsonify({'Message': 'Wrong credentials'}),401)
api.add_resource(Register,"/register")
api.add_resource(Login,"/login")



app.run(debug = True)