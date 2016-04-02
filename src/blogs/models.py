# coding: utf-8

from __future__ import unicode_literals
import datetime
from django.utils import timezone
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from login.models import UserProfile


@python_2_unicode_compatible
class Blog(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Имя блога')
    descr = models.CharField(max_length=500, verbose_name=u'Краткое описание')

    def __str__(self):
        return self.name


