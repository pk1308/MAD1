from flask import Flask

app = Flask(__name__)

@app.route('/mypathroute/<path:url_path>')
def mypathroute(url_path):   
    return 'The path is: ' +url_path

if __name__ == "__main__":
    app.run(debug=True)