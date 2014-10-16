from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse


class Teacher(models.Model):
    
    name = models.CharField(_('name'), max_length=15)
    description = models.TextField(_('description'), blank=True)
    avatar_url = models.URLField(_('avatar url'), max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = _('teacher')
        verbose_name_plural = _('teachers')
        ordering = ('name',)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('people:teacher_detail', args=(self.id,))

admin.site.register(Teacher)




