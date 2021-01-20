from django.contrib import admin
from .models import Page, Images
class PageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Page, PageAdmin)


class ImageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Images, ImageAdmin)

