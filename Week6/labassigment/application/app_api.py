from flask import current_app as app
from flask_restful import Resource, abort, fields, marshal_with, reqparse

from .app_expcection import (
    BusinessValidationError,
    Coursenotfound,
    NotFoundError,
)
from .app_model import course, db, enrollment, student

# course.get
course_parser = reqparse.RequestParser()
course_parser.add_argument("course_id", type=int, help=" course id")
course_resource = {
    "course_id": fields.Integer,
    "course_name": fields.String,
    "course_code": fields.String,
    "course_description": fields.String,
}
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

# student resource

student_resource = {
    "student_id": fields.Integer,
    "first_name": fields.String,
    "last_name": fields.String,
    "roll_number": fields.String,
}


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

#Enrollment
enroll_post = reqparse.RequestParser()
enroll_post.add_argument("course_id",type=int,help="Enter course ID",required=True)

enroll_resource =  {
    "enrollment_id": fields.Integer,
    "student_id": fields.Integer,
    "course_id": fields.Integer
  }

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
            course_details = (
                db.session.query(course).filter(course.course_id == course_id).first()
            )
            if not course_details:
                raise Coursenotfound()
            return course_details
        except Coursenotfound as e:
            raise e
        except Exception as exc:
            app.logger.debug(exc)
            # trunk-ignore(ruff/B904)
            abort(500)

    @marshal_with(course_resource)
    def put(self, course_id: int):
        try:
            args = course_post_parser.parse_args()

            # Check for missing course_code
            if not args["course_code"]:
                raise BusinessValidationError(
                    status_code=400,
                    error_code="COURSE002",
                    error_message="Course Code is required",
                )

            # Check for missing course_name
            if not args["course_name"]:
                raise BusinessValidationError(
                    status_code=400,
                    error_code="COURSE001",
                    error_message="Course Name is required",
                )

            # Check if course_code already exists
            course_data = course.query.filter_by(course_id=course_id).first()
            if not course_data:
                raise Coursenotfound()
            else:
                course_name = args["course_name"]
                course_code = args["course_code"]
                course_description = args["course_description"]

                course_data.course_code = course_code
                course_data.course_name = course_name
                course_data.course_description = course_description
                db.session.add(course_data)
                db.session.commit()
                return course_data, 200

        except NotFoundError as e:
            raise e
        except Coursenotfound as e:
            raise e
        except BusinessValidationError as e:
            raise e
        except Exception as exc:
            app.logger.debug(exc)
            abort(500)

    def delete(self, course_id):
        try:
            course_data = course.query.filter_by(course_id=course_id).first()
            if not course_data:
                raise Coursenotfound()
            db.session.delete(course_data)
            db.session.commit()
            return "Successfully Deleted", 200
        except Coursenotfound as e:
            raise e
        except BusinessValidationError as e:
            raise e
        except Exception as exc:
            app.logger.debug(exc)
            # trunk-ignore(ruff/B904)
            abort(500)

    @marshal_with(course_resource)
    def post(self):
        try:
            args = course_post_parser.parse_args()

            # Check for missing course_code
            if not args["course_code"]:
                raise BusinessValidationError(
                    status_code=400,
                    error_code="COURSE002",
                    error_message="Course Code is required",
                )

            # Check for missing course_name
            if not args["course_name"]:
                raise BusinessValidationError(
                    status_code=400,
                    error_code="COURSE001",
                    error_message="Course Name is required",
                )

            # Check if course_code already exists
            course_data = course.query.filter_by(
                course_name=args["course_name"]
            ).first()
            if course_data:
                raise Coursenotfound(
                    status_code=409,
                    error_message="Course_code already exists",
                )

            course_name = args["course_name"]
            course_code = args["course_code"]
            course_description = args["course_description"]

            new_course = course(
                course_name=course_name,
                course_code=course_code,
                course_description=course_description,
            )
            db.session.add(new_course)
            db.session.commit()
            return new_course, 201

        except BusinessValidationError as e:
            raise e
        except Coursenotfound as e:
            raise e
        except Exception as exc:
            app.logger.debug(exc)

            abort(500)


class StudentId(Resource):
    """_summary_

    Args:
        Resource (_type_): _description_
    """

    @marshal_with(student_resource)
    def get(self, student_id):
        try:
            student_data = student.query.filter_by(student_id=student_id).first()
            if not student_data:
                raise NotFoundError(status_code=404, error_message="Student not found")
            return student_data
        except NotFoundError as e:
            raise e
        except Exception as e:
            app.logger.error(e)
            abort(500)

    @marshal_with(student_resource)
    def put(self, student_id):
        try:
            args = student_post_parser.parse_args()

            # Check for missing course_code
            if not args["first_name"]:
                raise BusinessValidationError(
                    status_code=400,
                    error_code="STUDENT002",
                    error_message="First Name is required",
                )

            # roll no
            if not args["roll_number"]:
                raise BusinessValidationError(
                    status_code=400,
                    error_code="Student",
                    error_message="Roll Number required",
                )

            # Check if course_code already exists
            student_data = student.query.filter_by(student_id=student_id).first()
            if not student_data:
                raise NotFoundError(status_code=404, error_message="Student not found")
            else:
                student_data.first_name = args["first_name"]
                student_data.last_name = args["last_name"]
                student_data.roll_number = args["roll_number"]
                db.session.add(student_data)
                db.session.commit()
                return student_data, 200

        except NotFoundError as e:
            raise e
        except BusinessValidationError as e:
            raise e
        except Exception as exc:
            app.logger.debug(exc)
            abort(500)

    def delete(self, student_id):
        try:
            student_data = student.query.filter_by(student_id=student_id).first()
            if not student_data:
                raise NotFoundError(status_code=404, error_message="Student not found")
            else:
                db.session.delete(student_data)
                db.session.commit()
                return "Successfully Deleted", 200
        except NotFoundError as e:
            raise e
        except BusinessValidationError as e:
            raise e
        except Exception as exc:
            app.logger.debug(exc)
            # trunk-ignore(ruff/B904)
            abort(500)

    @marshal_with(student_resource)
    def post(self):
        try:
            args = student_post_parser.parse_args()

            # Check for missing course_code
            if not args["first_name"]:
                raise BusinessValidationError(
                    status_code=400,
                    error_code="STUDENT002",
                    error_message="First Name is required",
                )

            # roll no
            if not args["roll_number"]:
                raise BusinessValidationError(
                    status_code=400,
                    error_code="Student",
                    error_message="Roll Number required",
                )

            # Check if course_code already exists
            student_data = student.query.filter_by(
                roll_number=args["roll_number"]
            ).first()
            if student_data:
                raise NotFoundError(
                    status_code=409, error_message="Student already exist"
                )
            else:
                student_new_data = student(
                    first_name=args["first_name"],
                    last_name=args["last_name"],
                    roll_number=args["roll_number"],
                )
                db.session.add(student_new_data)
                db.session.commit()
                return student_new_data, 200

        except NotFoundError as e:
            raise e
        except BusinessValidationError as e:
            raise e
        except Exception as exc:
            app.logger.debug(exc)
            abort(500)


class CourseNStudent(Resource):
    """_summary_

    Args:
        Resource (_type_): _description_
    """

    def delete(self , student_id , course_id):
        try:
            fetcher = enrollment.query.filter_by(student_id=student_id,course_id=course_id).all()
            if not fetcher:
                student_data = student.query.filter_by(student_id=student_id).first()
                if not student_data:
                    raise BusinessValidationError(status_code=400, error_code="ENROLLMENT002",
                                                  error_message="Student does not exist.")
                course_data = course.query.filter_by(course_id=course_id).first()
                if not course_data:
                    raise BusinessValidationError(status_code=400, error_code="ENROLLMENT001",
                                                  error_message="Course does not exist")
                raise NotFoundError(status_code=404,
                                    error_message="Enrollment for the student not found")
            for fetch in fetcher:
                db.session.delete(fetch)
            db.session.commit()
        except BusinessValidationError as e:
            raise e
        except NotFoundError as e :
            raise e
        except Exception as exc:
            app.logger.debug(exc)
            abort(500)

    def post(self, student_id):
        try:
            args = enroll_post.parse_args()
            course_id = args["course_id"]
            student_data = student.query.filter_by(student_id=student_id).first()
            if not student_data:
                    raise NotFoundError(status_code=404 , error_message="Student not found")
            course_data = course.query.filter_by(course_id=course_id).first()
            if not course_data:
                raise BusinessValidationError(status_code=400, error_code="ENROLLMENT001",
                                                  error_message="Course does not exist")
            en = enrollment(student_id=student_id,course_id=args["course_id"])
            db.session.add(en)
            db.session.commit()
            return self.get(student_id)
        except BusinessValidationError as e:
            raise e
        except NotFoundError as e :
            raise e
        except Exception as e:
            abort(500)

    def get(self,student_id):
        try:
            student_data = student.query.filter_by(student_id=student_id).first()
            if not student_data:
                raise BusinessValidationError(status_code=400 , error_code="ENROLLMENT002" ,
                                            error_message="Student does not exist" )
            fetcher = enrollment.query.filter_by(student_id=student_id).all()
            if not fetcher:
                raise NotFoundError(status_code=404,
                                    error_message="Student is not enrolled in any course")
            result = []
            for fetch in fetcher:
                subresult = {
                    "enrollment_id": fetch.enrollment_id,
                    "student_id": fetch.student_id,
                    "course_id": fetch.course_id
                }
                result.append(subresult)
            return result
        except BusinessValidationError as e:
            raise e
        except Exception as exc:
            app.logger.debug(exc)
            abort(500)