from django.db import models
from django.contrib.auth.models import User
from video.models import Video
# Create your models here.

class Comment(models.Model):
    author = models.ForeignKey(User)
    video = models.ForeignKey(Video)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True, auto_now_add=True)

