#pip install flask
from flask import Flask,render_template,request
app = Flask(__name__)#variable and module name can be anthing

@app.route("/h")#maps url with def just written below it
@app.route("/one")
def home():
    return "<h1>My first Webpage</h1>" 

#two routes can take same defination but converse is not true
@app.route("/second")
def second():
    return "<h1>My second Webpage</h1>"

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method =="POST":
        form_data= request.form.get("course")
        return render_template("course.html",jinja=form_data)

    return render_template("home.html")


#get >>get me some data, post>> post data
app.run(debug=True)#detects changes, gives debug info, so should be used on in development stage only



