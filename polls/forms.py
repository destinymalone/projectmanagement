from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User
from polls.models import CreateBoard, UserBoardList, UserListCard

class CreateBoardForm(forms.ModelForm):
    class Meta:
        model = CreateBoard
        fields = ['title']

class BoardEditForm(forms.ModelForm):
    class Meta:
        model = CreateBoard
        fields = ["username", "title"]
        widgets = {"title": forms.TextInput()}

class UserListForm(forms.Form):
    list = forms.CharField()
    card = forms.CharField()


class ListEditForm(forms.ModelForm):
    class Meta:
        model = UserBoardList
        fields = ["title", "card"]
        widgets = {"title": forms.Textarea()}

class UserCardForm(forms.Form):
    description = forms.CharField()

class CardEditForm(forms.ModelForm):
    class Meta:
        model = UserListCard
        fields = ["description"]
        widgets = {"description": forms.Textarea()}