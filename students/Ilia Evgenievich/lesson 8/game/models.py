from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()



class Images(models.Model):
    title = models.CharField(max_length=250)
    page = models.ForeignKey(Page,on_delete=models.CASCADE)

