from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sampledb.sqllite3"

db = SQLAlchemy(app)

app.app_context().push()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    email = db.Column(db.String())

class Roles(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     r_name = db.Column(db.String(), unique=True, nullable=False)



if __name__ == "__main__":

    # trunk-ignore(bandit/B201)
    app.run(debug=True)
