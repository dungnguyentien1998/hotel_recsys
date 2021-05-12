from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from enum import Enum
from app.utils.model_maker import BaseModel
from safedelete.models import SafeDeleteManager


# User manager
class UserManager(BaseUserManager, SafeDeleteManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Create user with email password and user fields
    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)


# Role model
class Role(models.TextChoices):
    USER = 'user', _('user')
    HOTELIER = 'hotelier', _('hotelier')
    ADMIN = 'admin', _('admin')

    def __eq__(self, other):
        if isinstance(other, Enum):
            super.__eq__(self, other)
        else:
            return self.value == other


# User model
class User(BaseModel, AbstractBaseUser):
    email = models.EmailField('email', unique=True, max_length=settings.CHAR_FIELD_MAX_LEN,
                              error_messages={'unique': _('An user with that email already exists.'), }, )
    password = models.CharField(blank=False, max_length=settings.CHAR_FIELD_MAX_LEN)
    name = models.CharField(blank=True, max_length=settings.CHAR_FIELD_MAX_LEN)
    tel = models.CharField(blank=True, max_length=settings.TEL_LEN, null=True)
    city = models.CharField(blank=True, max_length=settings.CHAR_FIELD_MAX_LEN, null=True)
    district = models.CharField(blank=True, max_length=settings.CHAR_FIELD_MAX_LEN, null=True)
    ward = models.CharField(blank=True, max_length=settings.CHAR_FIELD_MAX_LEN, null=True)
    address = models.CharField(blank=True, max_length=settings.CHAR_FIELD_MAX_LEN, null=True)
    image = models.ImageField(null=True)
    birthday = models.DateField(null=True)
    role = models.CharField(max_length=8, choices=Role.choices, default=Role.USER)
    is_active = models.BooleanField(default=False)

    objects = UserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'user'
