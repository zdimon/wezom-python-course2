from django.contrib import admin
from .models import Page, Images, Gameuser, Card, Card2User


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

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['image_tag', 'on_hand']

@admin.register(Card2User)
class Card2UserAdmin(admin.ModelAdmin):
    list_display = ['card', 'user']