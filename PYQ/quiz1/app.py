from flask import Flask, url_for
import sys

def create_path():
    if len(sys.argv) < 2:
        return '/static'
    else:
        return f'/{sys.argv[1]}'

app = Flask(__name__, static_url_path = create_path() , static_folder='STATIC_FOLDER' , template_folder="template_dir")

@app.route('/home')
def display():
    return f"<h3>static url path: {app.static_url_path}</h3> <h3>static folder: {app.static_folder}</h3></h3><h3>static folder: {app.template_folder}</h3>"

app.run(debug = True)
