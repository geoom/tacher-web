from django.db import models
from django.contrib import admin

class Record(models.Model):
	puntualidad = models.SmallIntegerField()
	exigencia = models.SmallIntegerField()
	pasabilidad = models.SmallIntegerField()

	#def __unicode__(self):
	#	return self.name

admin.site.register(Record)