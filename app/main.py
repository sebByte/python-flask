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
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('FDB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cabin = db.Column(db.String(120))
    service = db.Column(db.String(120))
    updated_at = db.Column(
        db.DateTime(), default=db.func.now(), onupdate=db.func.now())


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(120))


# Route to /orders
@app.route("/orders", methods=['GET', 'POST'])
def order():
    a = []

    if request.method == 'GET':
        for i in Order.query.all():
            a.append({'id': i.id, 'cabin': i.cabin,
                      'service': i.service, 'updated_at': i.updated_at})

    if request.method == 'POST':
        body = request.get_json()
        new_order = Order(
            cabin=body['cabin'],
            service=body['service'],
        )
        db.session.add(new_order)
        db.session.commit()

        a = ["New order added"]

    return jsonify(a)

@app.route("/orders/<id>", methods=['PUT', 'DELETE'])
def order_by(id):
    b = []

    if request.method == 'PUT':
        b = ["Order not working"]

    if request.method == 'DELETE':
        delete_order = Order.query.get(id)
        db.session.delete(delete_order)
        db.session.commit()

        b = ["Order was succesuflly deleted"]

    return jsonify(b)


# Default route to /services
@app.route("/services", methods=['GET', 'POST'])
def service():
    c = []

    if request.method == 'GET':
        for j in Service.query.all():
            c.append({'id': j.id, 'service': j.service})

    if request.method == 'POST':
        body = request.get_json()
        new_service = Service(service=body['service'])
        db.session.add(new_service)
        db.session.commit()

        c = ["New service added"]

    return jsonify(c)


@app.route("/services/<id>", methods=['PUT', 'DELETE'])
def service_by(id):
    d = []

    if request.method == 'PUT':
        d = ["Service not working"]

    if request.method == 'DELETE':
        delete_service = Service.query.get(id)
        db.session.delete(delete_service)
        db.session.commit()

        d = ["Service was succesuflly deleted"]

    return jsonify(d)
