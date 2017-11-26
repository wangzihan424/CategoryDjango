# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone
# Create your models here.


class UserInfo(models.Model):
    user_name = models.CharField(max_length=100)
    user_psw = models.CharField(max_length=32)
    regist_time = models.DateTimeField(default=timezone.now)
    user_head = models.CharField(max_length=255)
    login_time = models.DateTimeField(default=timezone.now)
    email = models.EmailField(null=True)



