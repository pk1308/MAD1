from flask import Flask, request , jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sampledb.sqlite3"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sampledbmm.sqlite3"

db = SQLAlchemy(app)

app.app_context().push()

# ======================== connected with one-to-many relationship ====================================

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.String(), unique = True, nullable = False)
#     password = db.Column(db.String(), nullable = False) # default value for unique is "False"
#     email = db.Column(db.String()) # default value for nullable is "True"
#     roles = db.relationship("Role", backref = 'bearer')

# class Role(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     r_name = db.Column(db.String(), unique = True, nullable = False)
#     user = db.Column(db.Integer, db.ForeignKey('user.id')) # user is table not class

# mad1 ----> [admin, instructor, student] -- correct
# mad2 ----> [ta, intern] -- correct
# mad3 ----> [admin, ta]  -- incorrect -- violating one-to-many
# mad3 ----> [staff]  -- correct

# =========================================================================================================

# ======================== connected with many-to-many relationship ====================================


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True) 
    username = db.Column(db.String(), unique = True, nullable = False)
    password = db.Column(db.String(), nullable = False) # default value for unique is "False"
    email = db.Column(db.String()) # default value for nullable is "True"
    roles = db.relationship("Role", backref = 'bearer', secondary = "association")
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

    # db.relationship -- class
    # secondary -- table name 
    # ForeignKey -- table name

class Role(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    r_name = db.Column(db.String(), unique = True, nullable = False)
    # bearer = db.relationship("User", backref = 'roles', secondary = 'association')

class Association(db.Model):
    # id = db.Column(db.Integer, primary_key = True) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True) # acting as composite primary key 
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), primary_key = True)

# data = [
#     {"username": "mad1", "pass": "12345", "course": "MADI"},
#     {"username": "mad2", "pass": "1234dd5", "course": "MADII"},
#     {"username": "test_user2", "pass": "1234DDD5", "course": "DBMS"},
#     {"username": "TEST_USER4", "pass": "12345", "course": "PDSA"},
# ]


@app.route("/my_data")
def get_data():
    users = User.query.all()
    
    return jsonify([user.to_dict() for user in users])


@app.route("/user_data/<user_name>")
def get_user_data(user_name):
    data = User.query.filter_by(username= user_name)
    app.logger.debug(data)
    if not data:
        return {"message": "User not found"}, 404
    return data


@app.route("/adduser", methods=["POST"])
def add_user():
    new_user = request.json
    for user in data:
        if user["username"] == new_user["username"]:
            return {"message": "user already present"}, 400
    data.append(new_user)
    return {"message": "user added successfully"}, 201


if __name__ == "__main__":
    app.run()
