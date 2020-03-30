from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User
from polls.models import CreateBoard, UserBoardList, UserListCard

class CreateBoardForm(forms.Form):
    title = forms.CharField()


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
        fields = ["list", "card"]
        widgets = {"list": forms.Textarea()}

class UserCardForm(forms.Form):
    description = forms.CharField()

class CardEditForm(forms.ModelForm):
    class Meta:
        model = UserListCard
        fields = ["description"]
        widgets = {"description": forms.Textarea()}