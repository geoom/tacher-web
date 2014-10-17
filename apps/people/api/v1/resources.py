# -*- coding: utf-8 -*
from rest_framework import serializers

from apps.rating.api.v1.resources import GlobalRatingSerializer

from ...models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    global_rating = GlobalRatingSerializer()

    class Meta:
        model = Teacher
        fields = ('id', 'name', 'description', 'avatar_url', 'global_rating')
