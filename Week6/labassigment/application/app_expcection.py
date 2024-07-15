import json
from flask import make_response
from werkzeug.exceptions import HTTPException
import logging

class SchemaValidationError(HTTPException):
  """Exception raised for schema validation errors."""
  def __init__(self, status_code, error_code, error_message):
      data = {"error_code": error_code, "error_message": error_message}
      logging.error(f"SchemaValidationError: {data}")
      self.response = make_response(json.dumps(data), status_code)

class BusinessValidationError(HTTPException):
  """Exception raised for business logic validation errors."""
  def __init__(self, status_code, error_code, error_message):
      data = {"error_code": error_code, "error_message": error_message}
      logging.error(f"BusinessValidationError: {data}")
      self.response = make_response(json.dumps(data), status_code)

class NotFoundError(HTTPException):
  """Exception raised for not found errors."""
  def __init__(self, status_code):
      logging.error(f"NotFoundError: Status code {status_code}")
      self.response = make_response("", status_code)

class InternalError(HTTPException):
  """Exception raised for internal server errors."""
  def __init__(self, status_code, exc):
      logging.error(f"InternalError: {exc}")
      self.response = make_response("Internal Server Error", status_code)
