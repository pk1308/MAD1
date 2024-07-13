from flask import Flask, redirect, render_template, request, url_for
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
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(
        db.String(), nullable=False
    )  # default value for unique is "False"
    email = db.Column(db.String())  # default value for nullable is "True"
    roles = db.relationship("Role", backref="bearer", secondary="association")

    # db.relationship -- class
    # secondary -- table name
    # ForeignKey -- table name


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    r_name = db.Column(db.String(), unique=True, nullable=False)
    # bearer = db.relationship("User", backref = 'roles', secondary = 'association')


class Association(db.Model):
    # id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id"), primary_key=True
    )  # acting as composite primary key
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), primary_key=True)


# s1 ---- [s2, s3]
# s2 -----[s1, s3]
# s3 ---- [s1, s2]

# mad1 ----> [admin, instructor, student] -- correct
# mad2 ----> [ta, intern] -- correct
# mad3 ----> [admin, ta]  -- correct
# mad3 ----> [staff]

# admin ---> [mad1, mad3]


# ///////////////////////////////////////////////////////////////////////


@app.route("/users")
def get_users():
    users = User.query.all()
    return render_template("home.html", users=users)


@app.route("/")
def home():
    return redirect("/users")


@app.route("/user_details/<username>")
def user_details(username):
    user = User.query.filter_by(username=username).first()
    if user:
        roles = user.roles
        return render_template("roles.html", user=user, roles=roles)
    else:
        return "User not found", 404


@app.route("/update/<int:myid>", methods=["GET", "POST"])
def update_user(myid):
  user = User.query.filter_by(id=myid).first()
  
  if request.method == "POST":
      user_name = request.form.get("username")
      pwd = request.form.get("password")
      email = request.form.get("email")
      
      if user_name and pwd:
          user.username = user_name
          user.password = pwd
          user.email = email
          db.session.commit()
          return redirect("/users")
      else:
          return "Invalid input", 400
  else:
      return render_template("update.html", user=user)


if __name__ == "__main__":
    # trunk-ignore(bandit/B201)
    app.run(debug=True)
