from django.db import models
from django.contrib import admin
from apps.ranking.models import Record


class Teacher(models.Model):
    
    name = models.CharField(max_length=15)
    description = models.TextField()
    average_record = models.DecimalField(max_digits=5, decimal_places=3, default=0)

    def __unicode__(self):
        return self.name

admin.site.register(Teacher)




