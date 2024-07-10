from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# config
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sampledb.sqllite3"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sampledbmm.sqllite3"

db = SQLAlchemy(app)

app.app_context().push()

# ======================================================================================================================
## one to many relationship "sqlite:///sampledb.sqllite3"

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(), unique=True, nullable=False)
#     password = db.Column(db.String(), nullable=False)
#     email = db.Column(db.String())
#     roles = db.relationship("Role", backref="user1")


# class Role(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     r_name = db.Column(db.String(), unique=True, nullable=False)
#     user = db.Column(db.Integer, db.ForeignKey("user.id"))

# ======================================================================================================================

## many to many relationship "sqlite:///sampledbmm.sqllite3"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    email = db.Column(db.String())
    roles = db.relationship("Role" , backref = "bearer" , secondary = "association")


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    r_name = db.Column(db.String(), unique=True, nullable=False)


class Association(db.Model):
    User_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True) #composite primary key
    role_id = db.Column(db.Integer,db.ForeignKey("role.id"), primary_key=True)


if __name__ == "__main__":

    # trunk-ignore(bandit/B201)
    app.run(debug=True)
