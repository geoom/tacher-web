# -*- coding: utf-8 -*
from django.contrib import admin

from .models import RatingOption


class RatingOptionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Option information', {'fields': ['kind', 'image']}),
    ]
    list_display = ('kind', 'image')
    list_filter = ['kind']

admin.site.register(RatingOption, RatingOptionAdmin)