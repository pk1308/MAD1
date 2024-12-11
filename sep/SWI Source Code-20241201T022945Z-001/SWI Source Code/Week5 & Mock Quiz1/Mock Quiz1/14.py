from flask import Flask, request
app = Flask(__name__)
@app.route('/get_value')
def get_value():
    val1 = request.args.get("val1")
    # val1 = request.args.get("val1","20")
    return "The value is "+ val1
app.run(port= 5000,debug=True)