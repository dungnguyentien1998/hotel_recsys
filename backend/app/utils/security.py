import base64
import uuid
from enum import Enum
from datetime import timedelta
from jose import jwt
from django.conf import settings
from django.utils import timezone
from app.exceptions import TokenExpired
from rest_framework.authentication import get_authorization_header, BaseAuthentication


# Create uuid for models
def generate_uuid():
    return base64.urlsafe_b64encode(uuid.uuid4().bytes).rstrip(b'=').decode('ascii')


# Create token for authentication
def generate_token(obj, _type, expires_delta=None):
    expire = timezone.now() + timedelta(minutes=expires_delta) if expires_delta else \
        timezone.now() + timedelta(minutes=settings.TOKEN_EXPIRED_AFTER_MINUTES)
    # Parameters include: expire, subject, token type, secret key, hash algorithm
    payload = {'exp': expire, 'sub': obj, 'type': _type.value}
    encoded_payload = jwt.encode(claims=payload, key=settings.SECRET_KEY, algorithm=settings.ENCRYPTION_ALGORITHM)
    return encoded_payload


# Decode token to get data
def decode_token(token, callback=None, params=None):
    try:
        payload = jwt.decode(token=token, key=settings.SECRET_KEY, algorithms=settings.ENCRYPTION_ALGORITHM)
        return payload
    except jwt.ExpiredSignatureError:
        if callback:
            callback(**params)
        raise TokenExpired


class TokenAuthentication(BaseAuthentication):
    # Get auth header
    def authenticate(self, request):
        auth_header = get_authorization_header(request).decode('utf-8')
        if not auth_header:
            return None
        try:
            decoded_token = decode_token(auth_header)
            # return User.find_by_uuid(uuid=decoded_token['sub']), auth_header
            from app.models import User
            return User.objects.get(uuid=decoded_token['sub']), auth_header
        except jwt.JWTError:
            return None


class TokenType(Enum):
    AUTHENTICATION = 'authentication'
    FORGOT_PASSWORD = 'forgot_password'
    NEW_ACCOUNT = 'new_account'

    # Get token type
    def __str__(self):
        return self.value

    # Compare token type
    def __eq__(self, other):
        if isinstance(other, Enum):
            super.__eq__(self, other)
        else:
            return self.value == other
