from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from apps.ranking.models import Record


class Teacher(models.Model):
    
    name = models.CharField(_('name'), max_length=15)
    description = models.TextField(_('description'), blank=True)
    average_record = models.DecimalField(_('average record'), max_digits=5, decimal_places=3, default=0)

    class Meta:
        verbose_name = _('teacher')
        verbose_name_plural = _('teachers')
        ordering = ('name',)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('people:teacher_detail', args=(self.id,))

admin.site.register(Teacher)




