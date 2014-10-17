# -*- coding: utf-8 -*
from rest_framework import serializers

from ...models import RatingOption, Rating, GlobalRating


class RatingOptionSerializer(serializers.ModelSerializer):
    kind_name = serializers.Field(source='get_kind_name')
    image = serializers.Field(source='get_image_url')

    class Meta:
        model = RatingOption


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating


class GlobalRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = GlobalRating
