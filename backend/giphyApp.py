from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'giphydb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/giphydb'
app.config['JWT_SECRET_KEY'] = 'secret'

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

CORS(app)

# Delete a gif url in favorites array from user
def deleteFavoriteFromUser(uemail, gifUrl):
    users = mongo.db.users
    response = users.find_one_and_update({'email': uemail},{'$pull': {'favorites': gifUrl}})

# Add a gif url to the favorite array to user
def addFavoriteToUser(uemail, gifUrl):
    users = mongo.db.users
    # double check if value does not exsist before adding the element to the favorite array
    check = users.find_one({'email': uemail, 'favorites':gifUrl })
    if check is None:
        users.find_one_and_update({'email': uemail}, {'$push': {'favorites': gifUrl}}, upsert = True)

# Print the information of one user
def printUser(uemail):
    users = mongo.db.users
    response = users.find_one({'email': uemail})
    if response:
       print(response)

# add, remove, return users favorites
@app.route('/users/favorites',methods=['POST'])
def userFavorites():
   users = mongo.db.users

   # check if response has an email
   checkemail = request.get_json()['email']
   if checkemail == "" or checkemail == None:
       return jsonify({'result':'error', 'description':'No email in request'})
   # check if user exsist
   checkuser = users.find_one({'email':checkemail})
   if checkuser == "" or checkuser == None:
       return jsonify({'result':'erroruser','description':'No user found with the supplied email'})

   # if method is POST, iterate the array and add/remove each item
   if request.method == 'POST':
       actiont = request.get_json()['action']
       # if action is add, iterate and add each item
       if actiont == 'add':
           uemail = request.get_json()['email']
           temparr = request.get_json()['favorites']
           # add the favorites in the array if there are not exsistent
           for urlf in temparr:
               addFavoriteToUser(uemail, urlf)
           return jsonify({'result':'success'})
       # if action is remove, iterate the array and delete each item
       if actiont == 'remove':
           uemail = request.get_json()['email']
           temparr = request.get_json()['favorites']
           for urlf in temparr:
               deleteFavoriteFromUser(uemail, urlf)
           return jsonify({'result':'success'})
       # if action is get, return the array of favorites from the user in the db
       if actiont == 'get':
           uemail = request.get_json()['email']
           response = users.find_one({'email': uemail})
           return jsonify({'result': 'success', 'favorites' : response['favorites']})

   # if not a valid method, ignore
   return jsonify({'result' : 'error', 'description':'Not a valid HTTP/S method (POST,GET,DELETE)'})


@app.route('/users/register', methods=['POST'])
def register():
    users = mongo.db.users
    first_name = request.get_json()['first_name']
    last_name = request.get_json()['last_name']
    email = request.get_json()['email']
    password = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
    created = datetime.utcnow()

    # User ID
    user_id = users.insert({
        'first_name' : first_name,
        'last_name' : last_name,
        'email' : email,
        'password' : password,
        'created' : created,
        'favorites' : []
    })
    # Create a new user
    new_user = users.find_one({'_id':user_id})
    result = {'email': new_user['email'] + 'registered'}
    return jsonify({'result':result})

@app.route('/users/login', methods=['POST'])
def login():
    users = mongo.db.users
    email = request.get_json()['email']
    password = request.get_json()['password']
    result = ""
    response = users.find_one({'email' : email})
    if response:
       if bcrypt.check_password_hash(response['password'], password):
           access_token = create_access_token(identity = {
               'first_name': response['first_name'],
               'last_name' : response['last_name'],
               'email' : response['email']
           })
           result = jsonify({'token': access_token})
       else:
           result = jsonify({'error':'Invalid username or password'})

    else:
        result = jsonify({'result' : 'No results found'})
    return result

if __name__ == '__main__':
    app.run(debug=True)

