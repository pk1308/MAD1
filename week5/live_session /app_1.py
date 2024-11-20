#Starting of the app
from flask import Flask
from  model.model import db 


app=None

def setup_app():
    app=Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///ticket_show.sqlite3" #Having db file
    db.init_app(app) #Flask app connected to db(SQL alchemy)
    app.app_context().push() #Direct access to other modules
    app.debug=True
    print("Ticket Sho")



#Call the setup
setup_app()

@app.route("/")
def home():
    return "hello"

if __name__=="__main__":
    app.run()