from django.contrib import admin
from .models import Contact, Image

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']

admin.site.register(Contact, ContactAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']

admin.site.register(Image, ImageAdmin)
