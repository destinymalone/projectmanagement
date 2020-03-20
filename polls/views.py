# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpRespone

# Create your views here.

def index(request):
    return HttpRespone("Hello, world. You're at the polls index.")
