from flask import Flask, request
import sys
app = Flask (__name__)


@app.route('/home', methods = sys.argv[1])
def my_func():
    if request.method == 'GET':
        return "<h1>Hello from App Development</h1>"
    elif request.method == 'POST':
        return "<h1>Hello from POST</h1>"
    else:
        return "<h1>Please enter a valid HTTP method</h1>"
    
if __name__ == "__main__":
    
    app.run(debug=True )