import os

from flask import Flask
from flask_restful import Api
from application import db , StudentId, CourseId, CourseNStudent


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api_database.sqlite3'

db.init_app(app)
api = Api(app)

app.app_context().push()


api.add_resource(CourseId, "/api/course/<int:course_id>", "/api/course")
api.add_resource(StudentId, "/api/student/<int:student_id>", "/api/student")
api.add_resource(CourseNStudent, "/api/student/<int:student_id>/course" ,
                 "/api/student/<int:student_id>/course/<int:course_id>")

if __name__ == "__main__":
    # Run the Flask app
    app.run()