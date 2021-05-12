import os
import hashlib
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from storages.backends.s3boto3 import S3Boto3Storage


class LocalStorage(FileSystemStorage):
    # Get file and create new filename
    def generate_filename(self, filename):
        name, extension = os.path.splitext(filename)
        hashed = hashlib.md5(f'{name}{datetime.now()}'.encode('utf-8')).hexdigest()
        return f'{hashed}{extension}'


# Storage to save file
class S3Storage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False
