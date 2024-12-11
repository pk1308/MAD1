#pip install flask
from flask import Flask, render_template, request

app = Flask(__name__)#whatever module name is there just take it, this module will act as my server code
#app is variable, this can be anything but use same variable throughtout your code

#application, make url , interaction will be through browser  

# def home():
#     print("Hello from home function")
#url, webpage, def

@app.route('/')# '/' = http://127.0.0.1:5000
@app.route('/home')
def home():
    return "<h1>My first Webpage with debug mode on</h1>"

@app.route('/my_app',methods=["GET","POST"])#url,http method> resource
def my_app():
    # if request.method =="GET":
    #     return render_template("home.html")
    if request.method =="POST":
        form_data= request.form.get("course")
        return render_template("course.html",jinja=form_data)#x=3
    
    return render_template("home.html")

@app.route('/second')
def seconds():
    return "im here. second page"

@app.route('/second')
def second():
    
    if request.method =="POST":
        form_data= request.form.get("course")
        return render_template("course.html",jinja=form_data)#x=3
    
    return render_template("home.html")
#get by default, get resource, post> send some data

#request, header, body, response header body



app.run(debug=True)

#debug= true>take care of changes in code, errors , developement