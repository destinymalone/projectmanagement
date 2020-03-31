# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE, PROTECT

# Create your models here.

class CreateBoard(models.Model):
    username = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
  
class UserBoardList(models.Model):
    title = models.CharField(max_length=100)
    card = models.CharField(max_length=100)

class UserListCard(models.Model):
    description = models.TextField()
