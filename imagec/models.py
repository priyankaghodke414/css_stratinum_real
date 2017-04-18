from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import Permission, User

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default='description default text')

    def __unicode__(self):
        return self.name

class Post(models.Model):
    user = models.OneToOneField(User)
    Penname = models.CharField(max_length=200)
    AboutMe = models.CharField(max_length=200)
    def __str__(self):
        return self.Penname


class Album(models.Model):
    user = models.OneToOneField(User)
    image = models.FileField()
