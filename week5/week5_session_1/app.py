from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///onemany.sqlite3"

db = SQLAlchemy(app)

app.app_context().push()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False, unique = True)
    password = db.Column(db.String(), nullable = False)

#create another element role, --> id, role_name 
class Role(db.Model):
    id =  db.Column(db.Integer, primary_key = True)
    role_name = db.Column(db.String(20), nullable = False)

# # "/" - base url - http://127.0.0.1:5000
# @app.route('/')
# def my_func():ei
#     print("I am triggered")
#     return render_template("index.html")


# # "/hello"  http://127.0.0.1:5000/hello
# @app.route("/hello")
# def my_func_2():
#     return "hello users from flask"

# app.run()

# my_dict["my_key"] = "value"


# username = request.form.get("username") or null # backend validation


