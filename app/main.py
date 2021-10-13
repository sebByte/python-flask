#pylint: disable=no-member

import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

# Load variables from .env
load_dotenv()

# Create Flask instance
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    updated_at = db.Column(db.DateTime(), default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return '<User {}>'.format(self.email())

# Default route to /
@app.route("/", methods = ['GET', 'POST', 'PUT', 'DELETE'])
def index():
    ret = []
    # GET all users
    if request.method == 'GET':
        # Loop for every line in the User-column and add them to ret
        for u in User.query.all():
            ret.append({'id': u.id, 'email': u.email, 'updated_at': u.updated_at})
    
    # POST/Create a new user
    if request.method == 'POST':
        body = request.get_json()
        new_user = User(email=body['email'])
        db.session.add(new_user)
        db.session.commit()
        ret = [ "New user added" ]

    # PUT/Update user
    if request.method == 'PUT':
        ret = [ "PUT" ]

    if request.method == 'DELETE':
        ret = [ "DELETE" ]
    
    return jsonify(ret)

'''
# Notes, function
def get_notes():
    return [
        { "text": "foo"},
        { "text": "bar"}
    ]

# Route: /notes
@app.route("/notes")
def notes():
    print("Hello notes") # "ConsoleLog"
    return jsonify(get_notes())

# Run app if called directly
if __name__ == "__main__":
    app.run()
'''