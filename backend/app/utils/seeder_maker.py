import os
import random
from abc import ABC, abstractmethod
from django.conf import settings
from django.core.files import File


class BaseSeeder(ABC):
    REQUIRED_SEEDERS = []
    OBJECT_NUMBER = 1

    # Function used for create image for models
    @classmethod
    def image_maker(cls, name, obj, folder=None):
        # Get right image folder
        images_folder = settings.IMAGE_SEED_FOLDER
        if folder == 'room':
            images_folder = f'/home/{os.environ.get("USER")}/Downloads/room_images'
        elif folder == 'user':
            images_folder = f'/home/{os.environ.get("USER")}/Downloads/user_images'
        elif folder == 'complaint':
            images_folder = f'/home/{os.environ.get("USER")}/Downloads/room_test'
        # if folder == 'room':
        #     images_folder = '/home/tiendung/Downloads/room_images'
        # elif folder == 'user':
        #     images_folder = '/home/tiendung/Downloads/user_images'
        # elif folder == 'complaint':
        #     images_folder = '/home/tiendung/Downloads/room_test'

        # Get random image and save
        with open(os.path.join(images_folder, random.choice(os.listdir(images_folder))), 'rb') as file:
            image = File(file)
            obj.image.save(name, image)

    @abstractmethod
    def run(self, stdout, stderr):
        pass
