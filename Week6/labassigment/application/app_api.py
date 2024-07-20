from flask import current_app as app
from flask_restful import Resource, abort, reqparse
from .app_model import course, db, enrollment, student

# course.get
course_parser = reqparse.RequestParser()
course_parser.add_argument("course_id", type=int, help=" course id")

# course.put
course_put_parser = reqparse.RequestParser()
course_put_parser.add_argument("course_name", type=str, help="Enter course Name")
course_put_parser.add_argument("course_code", type=str, help="Enter course Code")
course_put_parser.add_argument(
    "course_description", type=str, help="Enter course Description"
)

# course.post
course_post_parser = reqparse.RequestParser()
course_post_parser.add_argument(
    "course_name", type=str, help="Enter course Name", required=True
)
course_post_parser.add_argument(
    "course_code", type=str, help="Enter course Code", required=True
)
course_post_parser.add_argument(
    "course_description", type=str, help="Enter course Description", required=True
)


student_post_parser = reqparse.RequestParser()
student_post_parser.add_argument(
    "first_name", type=str, help="Enter First Name", required=True
)
student_post_parser.add_argument(
    "last_name", type=str, help="Enter Last Name", required=True
)
student_post_parser.add_argument(
    "roll_number", type=str, help="Enter Roll Number", required=True
)

# Enrollment
enroll_post = reqparse.RequestParser()
enroll_post.add_argument("course_id", type=int, help="Enter course ID", required=True)


class CourseId(Resource):
    def get(self, course_id: int):
        try:
            course_details = (
                db.session.query(course).filter(course.course_id == course_id).first()
            )
            if not course_details:
                return "Course not found", 404
            return course_details.to_dict()
        except Exception as exc:
            app.logger.debug(exc)
            abort(500)

    def put(self, course_id: int):
        try:
            args = course_put_parser.parse_args()

            # Check for missing course_code
            if not args["course_code"]:
                return {"error_code":"COURSE002", "error_message":"Course Code is required"} , 400

            # Check for missing course_name
            if not args["course_name"]:
                return {"error_code": "COURSE001", "error_message":"Course Name is required", } , 400

            # Check if course exists
            course_data = course.query.filter_by(course_id=course_id).first()
            if not course_data:
                return "Course not found" , 404

            course_data.course_code = args["course_code"]
            course_data.course_name = args["course_name"]
            course_data.course_description = args["course_description"]
            db.session.add(course_data)
            db.session.commit()
            return course_data.to_dict(), 200
        except Exception as exc:
            app.logger.debug(exc)
            abort(500)

    def delete(self, course_id):
        try:
            course_data = course.query.filter_by(course_id=course_id).first()
            if not course_data:
                return  "Course not found" , 404
            db.session.delete(course_data)
            db.session.commit()
            return "Successfully Deleted", 200
        except Exception as exc:
            app.logger.debug(exc)
            abort(500)

    def post(self):
        try:
            args = course_post_parser.parse_args()

           # Check for missing course_code
            if not args["course_code"]:
                return {"error_code":"COURSE002", "error_message":"Course Code is required"} , 400

            # Check for missing course_name
            if not args["course_name"]:
                return {"error_code": "COURSE001", "error_message":"Course Name is required", } , 400

            # Check if course_code already exists
            course_data = course.query.filter_by(
                course_code=args["course_code"]
            ).first()
            if course_data:
                return "Course Code already exists",409

            new_course = course(
                course_name=args["course_name"],
                course_code=args["course_code"],
                course_description=args["course_description"],
            )
            db.session.add(new_course)
            db.session.commit()
            return new_course.to_dict(), 201
        except Exception as exc:
            app.logger.debug(exc)
            abort(500)


class StudentId(Resource):
    def get(self, student_id):
        try:
            student_data = student.query.filter_by(student_id=student_id).first()
            if not student_data:
                return "Student not found" , 404
            return student_data.to_dict()
        except Exception as e:
            app.logger.error(e)
            abort(500)

    def put(self, student_id):
        try:
            args = student_post_parser.parse_args()
            # Check for missing roll_number
            if not args["roll_number"]:
                return {"error_code": "STUDENT001", "error_message": "Roll Number required"} , 400

            # Check for missing first_name
            if not args["first_name"]:
                return {"error_code": "STUDENT002", "error_message": "First Name is required"} , 400

            # Check if student exists
            student_data = student.query.filter_by(student_id=student_id).first()
            if not student_data:
                return "Student not found", 404
            else:
                student_data.first_name = args["first_name"]
                student_data.last_name = args["last_name"]
                student_data.roll_number = args["roll_number"]
                db.session.add(student_data)
                db.session.commit()
                return student_data.to_dict(), 200

        except Exception as exc:
            app.logger.debug(exc)
            abort(500)

    def delete(self, student_id):
        try:
            student_data = student.query.filter_by(student_id=student_id).first()
            if not student_data:
                return "Student not found", 404
            else:
                db.session.delete(student_data)
                db.session.commit()
                return "Successfully Deleted", 200
        except Exception as exc:
            app.logger.debug(exc)
            abort(500)

    def post(self):
        try:
            args = student_post_parser.parse_args()
             # Check for missing roll_number
            if not args["roll_number"]:
                return {"error_code": "STUDENT001", "error_message": "Roll Number required"} , 400

            if not args["first_name"]:
                return {"error_code": "STUDENT002", "error_message": "First Name is required"} , 400

            # Check if roll_number already exists
            student_data = student.query.filter_by(
                roll_number=args["roll_number"]
            ).first()
            if student_data:
                return "Student already exists",409
            else:
                student_new_data = student(
                    first_name=args["first_name"],
                    last_name=args["last_name"],
                    roll_number=args["roll_number"],
                )
                db.session.add(student_new_data)
                db.session.commit()
                return student_new_data.to_dict(), 201
        except Exception as exc:
            app.logger.debug(exc)
            abort(500)


class CourseNStudent(Resource):
    def delete(self, student_id, course_id):
      try:
          fetcher = enrollment.query.filter_by(
              student_id=student_id, course_id=course_id
          ).all()
          if not fetcher:
              # If no enrollment found, raise a 404 error
              return "Enrollment not found", 404

          for fetch in fetcher:
              db.session.delete(fetch)
          db.session.commit()
          return "Successfully Deleted", 200
      except Exception as exc:
          app.logger.debug(exc)
          abort(500)
    def post(self, student_id):
      try:
          args = enroll_post.parse_args()
          course_id = args["course_id"]
          student_data = student.query.filter_by(student_id=student_id).first()
          if not student_data:
              return {"error_code":"ENROLLMENT002",
                    "error_message":"Student does not exist"} , 400
          course_data = course.query.filter_by(course_id=course_id).first()
          if not course_data:
              return {"error_code":"ENROLLMENT001",
                    "error_message":"Course does not exist"} , 400
          en = enrollment(student_id=student_id, course_id=args["course_id"])
          db.session.add(en)
          db.session.commit()
          # Return a 201 status code on successful enrollment creation
          return {"message": "Enrollment successful"}, 201
      except Exception as e:
          abort(500)
    def get(self, student_id):
        try:
            student_data = student.query.filter_by(student_id=student_id).first()
            if not student_data:
                return {"error_code":"ENROLLMENT002",
                    "error_message":"Student does not exist"} , 400
            fetcher = enrollment.query.filter_by(student_id=student_id).all()
            if not fetcher:
                return "Student is not enrolled in any course",404
            result = []
            for fetch in fetcher:
                subresult = {
                    "enrollment_id": fetch.enrollment_id,
                    "student_id": fetch.student_id,
                    "course_id": fetch.course_id,
                }
                result.append(subresult)
            return result
        except Exception as exc:
            app.logger.debug(exc)
            abort(500)
