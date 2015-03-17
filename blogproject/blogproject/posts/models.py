from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _


# class Category(models.Model):

#     class Meta:
#         verbose_name = _('Category')
#         verbose_name_plural = _('Categories')

#     name = models.CharField(_('name'), max_length=255)


class Post(models.Model):

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ['-created_at']

    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), max_length=1000)
    content = models.TextField(_('content'))

    created_at = models.DateTimeField(_('created at'),
                                      auto_now_add=True)

    # category = models.ForeignKey('Category', verbose_name=_('category'))

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk' : self.pk})

    def __str__(self):
        return '{title} @ {time}'.format(
            title=self.title,
            time=self.created_at.isoformat()
        )