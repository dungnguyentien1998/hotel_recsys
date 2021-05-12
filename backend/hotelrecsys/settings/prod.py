from .base import *

DEBUG = True

SECRET_KEY = os.environ.get('SECRET_KEY')

LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': f'/tmp/{PROJECT_NAME}/backend.log',
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'WARNING',
            'handlers': ['console'],
        }
    }
}

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE'),
        'HOST': os.environ.get('DB_HOST'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'NAME': os.environ.get('DB_NAME')
    }
}

SERVER_HOST = os.environ.get('SERVER_HOST')

DEFAULT_FILE_STORAGE = 'app.utils.storage_backends.S3Storage'
