from django.db import models
from django.utils.safestring import mark_safe

class Page(models.Model):
    title = models.CharField(max_length=250)
    alias = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.title

    @property
    def test(self):
        return f'{self.title}---{self.alias}'



class Images(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='page_images')

    @property
    def image_url(self):
        return mark_safe(f'<img height="50" src="{self.image.url}" />')






