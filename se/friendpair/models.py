from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class FriendPair(models.Model):
	follower = models.ForeignKey(User,related_name='follower')
	master = models.ForeignKey(User,related_name='master')
	