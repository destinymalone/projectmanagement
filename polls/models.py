# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE, PROTECT

# Create your models here.

class Board(models.Model):
    username = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"
  
class List(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, default=1) 
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.board} | {self.title}"

class Card(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, default=1)
    description = models.TextField()

    def __str__(self):
        return f"{self.description}"
 