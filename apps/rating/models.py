# -*- coding: utf-8 -*
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from .utils import UploadTo


option_upload_dir = UploadTo('option')


class RatingOption(models.Model):

    KIND_EVIL = 1
    KIND_EASIER = 2
    KIND_VAGUE = 3
    KIND_BRAINY = 4

    KIND_OPTION_CHOICES = (
        (KIND_EVIL, _('evil')),
        (KIND_EASIER, _('easier')),
        (KIND_VAGUE, _('vague')),
        (KIND_BRAINY, _('brainy')),
    )

    kind = models.PositiveSmallIntegerField(_('kind'), choices=KIND_OPTION_CHOICES)
    image = models.ImageField(_('image'), upload_to=option_upload_dir)

    class Meta:
        verbose_name = _('rating option')
        verbose_name_plural = _('rating options')

    def __unicode__(self):
        return "%s: %s" % (self.get_kind_display().upper(), self.get_image_url())

    def get_image_url(self):
        return str(self.image)

