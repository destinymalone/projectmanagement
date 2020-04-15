# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from polls.models import User, Board, List, Card

# Register your models here.
admin.site.register(Board)
admin.site.register(List)
admin.site.register(Card)