from collections import defaultdict
from app.exceptions import ValidationError
from rest_framework import exceptions


# Validate serializer data
def validate_serializer(serializer):
    errors = defaultdict(list)
    try:
        serializer.is_valid(raise_exception=True)
    except exceptions.ValidationError as e:
        for field, list_error in e.detail.items():
            for error in list_error:
                errors[error.encode('utf-8').decode().lower()].append(field)
    #  Commit errors and throw exception
    if errors:
        raise ValidationError(', '.join([f'{fields if len(fields) > 1 else fields[0]}: {error}' for error, fields in errors.items()]))
