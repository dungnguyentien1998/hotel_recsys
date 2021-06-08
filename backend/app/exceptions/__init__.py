from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions


# Base exception class
class APIException(exceptions.APIException):
    def __init__(self, message=None):
        if message:
            self.default_detail = message
        super().__init__()


# Unauthenticated exception
class Unauthenticated(APIException):
    status_code = 200
    default_code = '600'
    default_detail = _('Incorrect credentials')


# Unauthorized exception
class Unauthorized(APIException):
    status_code = 200
    default_code = '601'
    default_detail = _('You do not have permission to perform this action')


# Validation exception
class ValidationError(APIException):
    status_code = 200
    default_code = '602'
    default_detail = _('The input value is invalid')


# Token invalid exception
class InvalidToken(APIException):
    status_code = 200
    default_code = '603'
    default_detail = _('Invalid token')


# Token expired exception
class TokenExpired(APIException):
    status_code = 200
    default_code = '604'
    default_detail = _('Token expired')


# Notfound object exception
class ObjectNotFound(APIException):
    status_code = 200
    default_code = '605'
    default_detail = _('Not found')


# Input invalid exception
class InvalidInput(APIException):
    status_code = 200
    default_code = '606'
    default_detail = _('Invalid input')


class BookingError(APIException):
    status_code = 200
    default_code = '607'
    default_detail = _('The input value is invalid')


class LockError(APIException):
    status_code = 200
    default_code = '608'
    default_detail = _('This account has been locked')
