#pylint: disable=no-member

import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

# Load variables from .env
load_dotenv()
#print(os.environ.get('HELLO'))

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
@app.route("/")
def index():
    ret = []
    for u in User.query.all():
        ret.append({'email': u.email})

        return jsonify(ret)


# Run app if called directly
if __name__ == "__main__":
    app.run()