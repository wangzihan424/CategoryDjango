# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Category(models.Model):
    cate_name = models.CharField(max_length=100)
    cate_pid = models.IntegerField()
    cate_level = models.SmallIntegerField()
    cate_path = models.CharField(max_length=255)
