from flask import Flask, request, render_template, redirect
from flask import session

app = Flask(__name__)
app.config["SECRET_KEY"] = "thisisasecretkey"

@app.route('/login', methods = ['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # loading user credentials into the session
        session["username"] = username 
        session["password"] = password
        return redirect('/dashboard')
    return render_template('login_form.html')

@app.route('/dashboard')
def dashboard():
    username = session.get("username")
    if username:
    # user = User.query.filter_by(username = username).first()
        return f"""<h1>{username} has logged in successfully.</h1>
                    <a href='/logout'>Log out</a>"""
    else:
        return "You are not logged-in please login first"

@app.route('/logout')
def user_logout():
    session.pop("username", None)
    session.pop("password", None)
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug = True)


