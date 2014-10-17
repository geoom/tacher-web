# -*- coding: utf-8 -*
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ....rating import make_rate
from ...models import RatingOption
from .resources import RatingOptionSerializer, RatingSerializer


class RatingOptionListView(generics.ListAPIView):
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


@api_view(['POST'])
def rating_list_view(request):
    """ Create a new rating."""

    serializer = RatingSerializer(data=request.DATA)
    if serializer.is_valid():
        try:
            rating = serializer.object
            values = {
                'evil_value': rating.evil_value,
                'easier_value': rating.easier_value,
                'vague_value': rating.vague_value,
                'brainy_value': rating.brainy_value,
            }

            make_rate(rating.teacher.id, **values)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            errors = {'global': [e.message]}
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)