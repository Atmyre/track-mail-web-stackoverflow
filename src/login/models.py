from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractBaseUser
import os

def get_image_path(instance, filename):
    return os.path.join('users', str(instance.user.id), 'ava.jpg')

class UserProfile(models.Model):

    user = models.OneToOneField(User)
    #avatar = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __unicode__(self):
        return self.user.username
