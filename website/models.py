from django.db import models
from django.template.loader import render_to_string

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

import os


class Photo(models.Model):
    original = models.ImageField(upload_to='media')
    large = ImageSpecField(source='original', processors=[ResizeToFit(1200, 1200)])
    medium = ImageSpecField(source='original', processors=[ResizeToFit(720, 720)])
    small = ImageSpecField(source='original', processors=[ResizeToFit(320, 320)], options={'quality': 60})

    name = models.CharField(max_length=255, default='<Noname>')
    description = models.TextField(blank=True, null=True)

    @property
    def photo_name(self):
        name = os.path.basename(self.original.name)
        return name

    def thumb(self):
        return render_to_string('admin/thumb.html', {
            'image': self.small,
        })
    thumb.allow_tags = True

    def __str__(self):
        return self.name
