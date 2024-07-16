from flask import current_app as app
from flask import jsonify
from flask_restful import Resource, abort, fields, marshal_with, reqparse

from .app_expcection import BusinessValidationError, InternalError, NotFoundError
from .app_model import course, db, enrollments, student

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
                raise NotFoundError(
                    status_code=404,
                    error_code="COURSE_NOT_FOUND",
                    error_message="Course not found",
                )
            return course_details
        except NotFoundError as e:
            raise e
        except Exception as exc:
            app.logger.debug(exc)
            # trunk-ignore(ruff/B904)
            raise InternalError(status_code=500, error_message="Internal Server Error")

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
                raise NotFoundError(
                    status_code=404,
                    error_code="COURSE_NOT_FOUND",
                    error_message="Course not found",
                )
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

        except BusinessValidationError as e:
            raise e
        except Exception as exc:
            app.logger.debug(exc)
            # trunk-ignore(ruff/B904)
            raise InternalError(status_code=500, error_message="Internal Server Error")

    def delete(self):
        pass

    @marshal_with(course_resource)
    def post(self, course_id):
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
            if course_data:
                raise BusinessValidationError(
                    status_code=409,
                    error_code="COURSE003",
                    error_message="Course code already exists",
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
        except Exception as exc:
            app.logger.debug(exc)
            # trunk-ignore(ruff/B904)
            raise InternalError(status_code=500, error_message="Internal Server Error")


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
