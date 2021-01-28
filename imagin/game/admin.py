from django.contrib import admin
from .models import Page, Images, Gameuser


class ImageInlineAdmin(admin.TabularInline):
    model = Images

class PageAdmin(admin.ModelAdmin):
    #pass
    list_display = ['title', 'test', 'alias']
    inlines = [ImageInlineAdmin]
    

admin.site.register(Page, PageAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_filter = ['page']
    list_display = ['title', 'image_url']

admin.site.register(Images, ImageAdmin)

@admin.register(Gameuser)
class GameuserAdmin(admin.ModelAdmin):
    list_display = ['login', 'sids', 'image', 'is_online']