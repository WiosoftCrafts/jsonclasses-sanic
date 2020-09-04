from sanic.request import Request
from sanic.exceptions import SanicException
from jsonclasses.exceptions import ObjectNotFoundException, ValidationException
from sanic.response import json
from traceback import extract_tb

class UnsupportedMediaTypeException(Exception):

  def __init__(self, content_type: str):
    self.message = f'Content-Type \'{content_type}\' is not supported.'
    super().__init__(self.message)

class NotAcceptableException(Exception):

  def __init__(self, accept: str):
    self.message = f'Accept \'{accept}\' is not supported.'
    super().__init__(self.message)

def exception_handler(request: Request, exception: Exception):
  code = exception.status_code if isinstance(exception, SanicException) else 500
  code = 415 if isinstance(exception, UnsupportedMediaTypeException) else code
  code = 406 if isinstance(exception, NotAcceptableException) else code
  code = 404 if isinstance(exception, ObjectNotFoundException) else code
  code = 400 if isinstance(exception, ValidationException) else code
  return json({
    'error': {
      'type': exception.__class__.__name__,
      'message': exception.message if hasattr(exception, 'message') else str(exception),
      'traceback': [ f'file {f.filename} line {f.lineno} in {f.name}' for f in extract_tb(exception.__traceback__) ]
    }
  }, status=code)
