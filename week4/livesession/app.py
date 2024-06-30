from flask import Flask, render_template, request, jsonify , url_for , redirect

app = Flask(__name__)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        # form_data = request.form 
        return render_template("review.html", )
@app.route("/" )
def home():
    return url_for("register")
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    