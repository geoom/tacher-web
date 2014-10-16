
from django.db import models


class RandomQuerySet(models.query.QuerySet):

    def random(self):
        return self.order_by('?')[:1]


class RandomManager(models.Manager):

    def get_query_set(self):
        return RandomQuerySet(self.model, using=self._db)

    def random(self):
        return self.get_query_set().random()
