from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User
from polls.models import CreateBoard, UserBoardList, UserCardDetail

class CreateBoardForm(forms.ModelForm):
    class Meta:
        model = CreateBoard
        fields = ["username", "title"]
        widgets = {"title": forms.TextInput()}


class UserListForm(forms.ModelForm):
    class Meta:
        model = UserBoardList
        fields = ["list", "card"]
        widgets = {"list": forms.Textarea()}

class UserCardForm(forms.ModelForm):
    class Meta:
        model = UserCardDetail
        fields = ["description"]
        widgets = {"description": forms.Textarea()}