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

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #date
    cabin = db.Column(db.string(120))
    service = db.Column(db.string(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    updated_at = db.Column(db.DateTime(), default=db.func.now(), onupdate=db.func.now())

# Default route to /orders
@app.route("/orders", methods = ['GET', 'POST', 'PUT', 'DELETE'])
def order():
    order = []
    
    # GET all orders
    if request.method == 'GET':
        # Loop for every line in the User-column and add them to ret
        for u in Order.query.all():
            order.append({'id': u.id, 'cabin': u.cabin, 'service': u.service, 'email': u.email, 'updated_at': u.updated_at})
    
    # POST/Create a new user
    if request.method == 'POST':
        body = request.get_json()
        new_order = Order(
            cabin=body['cabin'],
            service=body['service'],
            email=body['email']
        )
        db.session.add(new_order)
        db.session.commit()
        order = [ "New order added" ]

    # PUT/Update user
    if request.method == 'PUT':
        order = [ "PUT" ]

    if request.method == 'DELETE':
        order = [ "DELETE" ]
    
    return jsonify(order)