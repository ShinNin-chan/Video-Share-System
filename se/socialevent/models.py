from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SocialEvent(models.Model):
    user = models.ForeignKey(User)
    friend = models.ForeignKey(User)
    tag = models.CharField(null=True, blank=True)

