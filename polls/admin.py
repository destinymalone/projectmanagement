# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from polls.models import User, CreateBoard, UserBoardList, UserListCard

# Register your models here.
admin.site.register(CreateBoard)
admin.site.register(UserBoardList)
admin.site.register(UserListCard)