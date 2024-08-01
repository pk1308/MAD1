from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///login_db.sqlite3"
app.config["SECRET_KEY"] = "week9_aq_session_secret-key"

db = SQLAlchemy(app)

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(150), nullable=False, unique=True)
  password = db.Column(db.String(150), nullable=False)
  role = db.Column(db.String(50))

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'log_in'

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
      username = request.form.get('username')
      password = request.form.get('password')
      hashed_password = generate_password_hash(password, method='sha256')
      new_user = User(username=username, password=hashed_password)
      try:
          db.session.add(new_user)
          db.session.commit()
          flash("Registration successful! Please log in.", "success")
          return redirect(url_for('log_in'))
      except:
          flash("Username already exists. Please choose a different one.", "danger")
  return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def log_in():
  if request.method == 'POST':
      username = request.form.get('username')
      password = request.form.get('password')
      user = User.query.filter_by(username=username).first()
      if user and check_password_hash(user.password, password):
          login_user(user)
          return redirect(f"/dashboard/{username}")
      else:
          flash("Invalid username or password", "danger")
  return render_template('login.html')

@app.route('/logout')
@login_required
def log_out():
  logout_user()
  flash("You have been logged out.", "success")
  return redirect(url_for('log_in'))

@app.route("/dashboard/<username>")
@login_required
def home(username):
  user = User.query.filter_by(username=username).first()
  if user:
      return render_template("dashboard.html", user=user)
  else:
      return "User not found", 404

if __name__ == "__main__":
  with app.app_context():
      db.create_all()
  app.run(debug=True)