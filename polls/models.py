# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Board(models.Model):
    username = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=65)

    def __str__(self):
        return {self.title}
  
class List(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE) 
    title = models.CharField(max_length=65)

    def __str__(self):
        return {self.title}

class Card(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    description = models.CharField(max_length=160)

    def __str__(self):
        return {self.description}