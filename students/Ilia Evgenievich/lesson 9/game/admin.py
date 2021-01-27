from django.contrib import admin
from .models import Page, Images

class PageAdmin(admin.ModelAdmin):
    #pass
    list_display = ['title', 'test']
    

admin.site.register(Page, PageAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_url']

admin.site.register(Images, ImageAdmin)

