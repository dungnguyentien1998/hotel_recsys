from django.conf import settings
from django.db import models
from safedelete.models import SafeDeleteManager, SafeDeleteModel, SOFT_DELETE_CASCADE
from app.utils.security import generate_uuid
from app.exceptions import ObjectNotFound, InvalidInput
from django.core.exceptions import ObjectDoesNotExist
import json
from safedelete.queryset import SafeDeleteQueryset


# Custom abstract query set
class BaseQuerySet(SafeDeleteQueryset):
    def get(self, *args, **kwargs):
        try:
            obj = super().get(*args, **kwargs)
        except ObjectDoesNotExist:
            raise ObjectNotFound
        return obj


# Custom abstract manager
class BaseManager(SafeDeleteManager):
    def __init__(self, queryset_class=BaseQuerySet, *args, **kwargs):
        super().__init__(queryset_class, *args, **kwargs)


# Custom abstract model
class BaseModel(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    uuid = models.CharField(primary_key=True, max_length=settings.CHAR_FIELD_MAX_LEN, default=generate_uuid)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    objects = BaseManager()

    # All model fields
    @classmethod
    def get_fields(cls):
        return [field.name for field in cls._meta.fields]

    # Fields for relation
    @classmethod
    def relation_fields(cls):
        return [field.name for field in cls._meta.local_fields if field.is_relation]

    # Fields created automatically
    @classmethod
    def auto_fields(cls):
        return [field for field in ['uuid', 'last_login', 'booked_count', 'created', 'updated', 'deleted', 'is_active']
                if field in cls.get_fields()]

    # Remaining fields
    @classmethod
    def editable_fields(cls):
        return list(set(cls.get_fields()) - set(cls.auto_fields()) - set(cls.relation_fields()))

    # Serialize model
    def __str__(self):
        obj_str = {}
        for field in list(set(self.get_fields()) - set(self.relation_fields())):
            value = getattr(self, field)
            obj_str[field] = str(value) if not isinstance(value, str) else value
        return json.dumps(obj_str, indent=4, sort_keys=True)

    # Update fields
    def update(self, **kwargs):
        if all([field in self.get_fields() for field in kwargs.keys()]):
            raise InvalidInput
        [setattr(self, field, value) for field, value in kwargs.items()]
        self.full_clean()
        self.save()

