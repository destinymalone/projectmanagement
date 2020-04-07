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

class CreateListForm(forms.ModelForm):
    class Meta:
        model = UserBoardList
        fields = ['list_title', 'card']


class ListEditForm(forms.ModelForm):
    class Meta:
        model = UserBoardList
        fields = ["list_title", "card"]
        widgets = {"list_title": forms.Textarea()}

class CreateCardForm(forms.Form):
    description = forms.CharField()

class CardEditForm(forms.ModelForm):
    class Meta:
        model = UserListCard
        fields = ["description"]
        widgets = {"description": forms.Textarea()}