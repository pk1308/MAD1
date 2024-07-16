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
      self.response.headers['Content-Type'] = 'application/json'

class BusinessValidationError(HTTPException):
  """Exception raised for business logic validation errors."""
  def __init__(self, status_code, error_code, error_message):
      data = {"error_code": error_code, "error_message": error_message}
      logging.error(f"BusinessValidationError: {data}")
      self.response = make_response(json.dumps(data), status_code)
      self.response.headers['Content-Type'] = 'application/json'

class NotFoundError(HTTPException):
  """Exception raised for not found errors."""
  def __init__(self, status_code, error_code, error_message):
      data = {"error_code": error_code, "error_message": error_message}
      logging.error(f"NotFoundError: {data}")
      self.response = make_response(json.dumps(data), status_code)
      self.response.headers['Content-Type'] = 'application/json'

class InternalError(HTTPException):
  """Exception raised for internal server errors."""
  def __init__(self, status_code, error_message="Internal Server Error"):
      data = {"error_message": error_message}
      logging.error(f"InternalError: {data}")
      self.response = make_response(json.dumps(data), status_code)
      self.response.headers['Content-Type'] = 'application/json'