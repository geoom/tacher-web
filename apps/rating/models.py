# -*- coding: utf-8 -*
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from apps.people.models import Teacher

from .utils import UploadTo
from .validators import validate_rating_value
from .managers import RandomManager


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

    objects = RandomManager()

    class Meta:
        verbose_name = _('rating option')
        verbose_name_plural = _('rating options')

    def __unicode__(self):
        return "%s: %s" % (self.get_kind_display().upper(), self.get_image_url())

    def get_image_url(self):
        return self.image.url

    def get_kind_name(self):
        return self.get_kind_display()


class Rating(models.Model):
    teacher = models.ForeignKey(Teacher, related_name='ratings')
    user = models.ForeignKey(User, related_name='ratings', null=True, blank=True)

    evil_value = models.SmallIntegerField(_('evil value'), validators=[validate_rating_value])
    easier_value = models.SmallIntegerField(_('easier value'), validators=[validate_rating_value])
    vague_value = models.SmallIntegerField(_('vague value'), validators=[validate_rating_value])
    brainy_value = models.SmallIntegerField(_('brainy value'), validators=[validate_rating_value])


class GlobalRating(models.Model):
    teacher = models.OneToOneField(Teacher, related_name='global_rating')

    total_evil_value = models.IntegerField(_('total evil value'), default=0, validators=MinValueValidator(0))
    total_easier_value = models.IntegerField(_('total easier value'), default=0, validators=MinValueValidator(0))
    total_vague_value = models.IntegerField(_('total vague value'), default=0, validators=MinValueValidator(0))
    total_brainy_value = models.IntegerField(_('total brainy value'), default=0, validators=MinValueValidator(0))

    average_record = models.DecimalField(_('average record'), max_digits=5, decimal_places=3,
                                         default=0, validators=MinValueValidator(0))

    def calculate_raking(self):
        """ Perform the teacher rate

        Returns:
            average_record (DecimalField): teacher average record

        """
        self.average_record = self.total_evil_value * 0.25 + self.total_easier_value * 0.25 + self.total_vague_value * 0.25 + self.total_brainy_value * 0.25