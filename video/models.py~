from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    owner = models.ForeignKey(User,related_name='video')
    uploadtime = models.DateTimeField(auto_now=True, auto_now_add=True)
    title = models.CharField(blank = True, max_length = 1000)
    description = models.CharField(blank = True, max_length = 1000)
    rating_sum = models.IntegerField(default=0)
    rating_person = models.IntegerField(default=0)
    file = models.FileField(upload_to='file/%Y/%m/%d', blank=True,null=True)


