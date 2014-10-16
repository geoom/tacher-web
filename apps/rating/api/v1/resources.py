# -*- coding: utf-8 -*
from rest_framework import serializers

from ...models import RatingOption


class RatingOptionSerializer(serializers.ModelSerializer):
    kind_name = serializers.Field(source='get_kind_name')
    image = serializers.Field(source='get_image_url')

    class Meta:
        model = RatingOption
