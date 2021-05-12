from django.conf import settings
from django.core.management.base import CommandError, BaseCommand
import os
import glob


class Command(BaseCommand):
    help = 'Remove all images in public folder'

    # Remove image files in folder
    def handle(self, *args, **options):
        if os.environ.get('DJANGO_SETTINGS_MODULE').split('.')[-1] == 'prod':
            raise CommandError('Can\'t run this command in production environment')
        # Remove file in public
        [os.remove(file) for file in glob.glob(f'{settings.MEDIA_ROOT}/*')]
