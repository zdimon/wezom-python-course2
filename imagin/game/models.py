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
    page = models.ForeignKey(Page,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='page_images')

    @property
    def image_url(self):
        return mark_safe(f'<img height="50" src="{self.image.url}" />')


class Gameuser(models.Model):
    login = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=250)
    image = models.ImageField(upload_to='user_images',null=True,blank=True)
    sids = models.TextField(default='')
    is_online = models.BooleanField(default=False)

    def add_sid(self,sid):
        sids = self.sids.split(';')
        if sid not in sids:
            sids.append(sid)
        self.sids = ';'.join(sids)
        self.save()
        self.check_online()

    @staticmethod
    def remove_sid(sid):
        user = Gameuser.objects.get(sids__contains=sid)
        sids = user.sids.split(';')
        if sid in sids:
            sids.remove(sid)
        user.sids = ';'.join(sids)
        user.save() 
        for u in Gameuser.objects.all():
            u.check_online()     

    def set_online(self,value):
        if self.is_online != value:
            from game.utils import update_online_users_in_json
            self.is_online = value
            self.save()
            update_online_users_in_json()

    def check_online(self):
        if(len(self.sids)>5):
            self.set_online(True)
        else:
            self.set_online(False)

    

