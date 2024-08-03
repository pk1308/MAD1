# from flask import Flask, request, url_for, redirect

# app = Flask(__name__)

# @app.route('/dashboard')
# def dashboard():
#   return 'This is the dashboard'

# @app.route('/user/<username' , methods = ["POST"])
# def user(username):
#   return f'This is {username} profile'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#   if request.method == 'POST':
#       return redirect(url_for('user', username='your_name'))
#   else:
#       return url_for('dashboard')

# if __name__ == '__main__':
#   app.run(debug=True)
  
from flask import Flask

app = Flask(__name__)

@app.route('/aboutpage')
def Home():
    return 'This is my home page'

@app.route('/projectpage/')
def projects():
    return 'The project page'

@app.route('/aboutpage/projectpage//')
def result():
    return 'This is about the project page'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)