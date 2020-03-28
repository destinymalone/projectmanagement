from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User
from polls.models import CreateBoard

class CreateBoardForm(forms.ModelForm):
    title = forms.CharField()

