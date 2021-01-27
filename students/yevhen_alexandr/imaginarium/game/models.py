from django.db import models
from django.utils.safestring import mark_safe


class Page(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

    
class Image(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to='images')

    @property
    def image_tag(self):
        return mark_safe(f'<img height="50" src="{self.image.url}" />')


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.CharField(max_length=255)
