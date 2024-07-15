# trunk-ignore-all(black)
# trunk-ignore-all(isort)
from .app_expcection import BusinessValidationError, InternalError, NotFoundError
from .app_model import course, db, enrollments, student
from flask_restful import Resource, fields, marshal_with, reqparse
import logging
course_parser = reqparse.RequestParser()
course_parser.add_argument("course_id", type=int, help=' course id') 
course_resource = {  "course_id": fields.Integer,
  "course_name": fields.String,
  "course_code": fields.String,
  "course_description": fields.String}
 
 
class CourseId(Resource):
    """_summary_

    Args:
        Resource (_type_): _description_
    """
    @marshal_with(course_resource)
    def get(self, course_id: int):
      """
      GET method to retrieve course details by course_id.

      Args:
          course_id (int): The ID of the course to retrieve.

      Raises:
          NotFoundError: If the course with the given ID is not found.
          InternalError: If an internal server error occurs.

      Returns:
          dict: The course details.
      """
      try:
          course_details = db.session.query(course).filter(course.course_id == course_id).first()
          if course_details is None:
              raise NotFoundError(status_code=404)
          return course_details
      except Exception as exc:
          return "" , 500
    def put(self):
        pass
    def delete(self):
        pass 
    def post(self):
        pass 

    
class StudentId(Resource):
    """_summary_

    Args:
        Resource (_type_): _description_
    """
    def put(self):
        pass 
    def delete(self):
        pass 
    def post(self):
        pass 
    def get(self):
        pass 

class CourseNStudent(Resource):
    """_summary_

    Args:
        Resource (_type_): _description_
    """
    def delete(self):
        pass 
    def post(self):
        pass 
    def get(self):
        pass