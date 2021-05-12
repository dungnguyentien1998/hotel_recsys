from .base import *

DEBUG = True

SECRET_KEY = '1!7o$)e_9(1^fln4pg^7orwpfn@jz)_mq54%9&nx5y0)ntoqun'

LOG_FILE = f'/tmp/backend.log'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
            'mode': 'a+',
            'formatter': 'standard',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.setdefault('DB_HOST', 'localhost'),
        'USER': os.environ.setdefault('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'NAME': os.environ.setdefault('DB_NAME', 'hotelrecsys')
    }
}

SERVER_HOST = 'localhost:8000'

DEFAULT_FILE_STORAGE = 'app.utils.storage_backends.LocalStorage'

CORS_ORIGIN_ALLOW_ALL = True

IMAGE_SEED_FOLDER = os.environ.setdefault('IMAGE_SEED_FOLDER', f'/home/{os.environ.get("USER")}/Downloads/images')
