
from django.core.exceptions import ValidationError


def validate_rating_value(value):
    if value < 0 or value > 1:
        raise ValidationError('%s is not an valid value' % value)
