# -*- coding: utf-8 -*
from rest_framework import generics

from ...models import RatingOption
from .resources import RatingOptionSerializer


class RatingOptionList(generics.ListAPIView):
    serializer_class = RatingOptionSerializer

    def get_queryset(self):
        queryset = RatingOption.objects.all()
        kind = self.request.QUERY_PARAMS.get('kind', None)
        random = self.request.QUERY_PARAMS.get('random', '')
        if kind is not None:
            queryset = queryset.filter(kind=kind)
            if random == 'true':
                queryset = queryset.random()
        return queryset