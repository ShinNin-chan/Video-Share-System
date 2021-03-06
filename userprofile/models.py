from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # Other fields here
    birthday = models.DateField(null=True)
    
    
    def __unicode__(self):
        return unicode(self.user)
