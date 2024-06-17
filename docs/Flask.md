comprehensive Flask cheat sheet :

````markdown
# Flask Cheat Sheet

## Setup

### Installation

```sh
pip install Flask
````

### Basic Structure

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

## Routes

### Basic Route

````python
@app.route('/')
def home():
    return "Home Page

### Route with Variable

```python
@app.route('/user/<username>')
def show_user(username):
    return f"User: {username}"
````

### Variable Types

```python
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Post ID: {post_id}"
```

## HTTP Methods

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Logging in..."
    else:
        return "Login Page"
```

## Rendering Templates

### HTML Template

Create a directory called `templates` and a file `index.html` inside it:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Home Page</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>{{ message }}</p>
</body>
</html>
```

### Render Template

```python
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html', title='Home', message='Welcome to Flask!')
```

## Template Inheritance

### Base Template (`base.html`)

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

### Child Template (`child.html`)

```html
{% extends "base.html" %}

{% block title %}Child Page{% endblock %}

{% block content %}
    <h1>This is the child page.</h1>
{% endblock %}
```

### Render Child Template

```python
@app.route('/child')
def child():
    return render_template('child.html')
```

## Static Files

### Serving Static Files

Place your static files (CSS, JS, images) in the `static` directory.

### Accessing Static Files

```html
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
```

## Forms and Request Data

### Simple Form

```html
<form method="POST" action="/submit">
    <input type="text" name="username">
    <input type="submit" value="Submit">
</form>
```

### Handling Form Submission

```python
from flask import request

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    return f"Submitted: {username}"
```

## Redirects and URLs

### Redirect

```python
from flask import redirect

@app.route('/go-to-home')
def go_to_home():
    return redirect('/')
```

### URL Generation

```python
from flask import url_for

@app.route('/admin')
def admin():
    return redirect(url_for('home'))
```

## Flash Messages

### Setting Up Flash Messages

```python
from flask import flash

@app.route('/flash-example')
def flash_example():
    flash('This is a flash message.')
    return redirect('/')
```

### Displaying Flash Messages

In your template (e.g., `index.html`):

```html
{% with messages = get_flashed_messages() %}
  {% if messages %}
    <ul>
    {% for message in messages %}
      <li>{{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
```

## Sessions

### Using Sessions

```python
from flask import session

app.secret_key = 'supersecretkey'

@app.route('/set-session')
def set_session():
    session['username'] = 'admin'
    return 'Session set!'

@app.route('/get-session')
def get_session():
    username = session.get('username')
    return f'Session username: {username}'
```

## Error Handling

### Custom Error Pages

```python
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
```

### 404 Template (`404.html`)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
</body>
</html>
```

## JSON Responses

### Returning JSON

```python
from flask import jsonify

@app.route('/api/data')
def get_data():
    data = {'key': 'value'}
    return jsonify(data)
```

## Database Integration (Flask-SQLAlchemy)

### Installation

```sh
pip install Flask-SQLAlchemy
```

### Setup

```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)

@app.route('/add-user')
def add_user():
    user = User(username='admin')
    db.session.add(user)
    db.session.commit()
    return 'User added!'
```

## Flask Extensions

### Flask-Migrate

```sh
pip install Flask-Migrate
```

### Setup Flask-Migrate

```python
from flask_migrate import Migrate

migrate = Migrate(app, db)

# Run migrations
# flask db init
# flask db migrate -m "Initial migration."
# flask db upgrade
```

## Running the App

### Run the Development Server

```sh
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

This cheat sheet covers the essential elements and features of Flask for quick reference. Feel free to expand it with more specific use cases and Flask extensions as needed!

```

```
