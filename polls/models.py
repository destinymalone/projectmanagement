# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CreateBoard(models.Model):
    username = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
