from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User
from polls.models import Board, List, Card

class CreateBoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title']

class BoardEditForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ["username", "title"]
        widgets = {"title": forms.TextInput()}

class CreateListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['title']


class ListEditForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["title"]
        widgets = {"title": forms.TextInput()}

class CreateCardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['description']

class CardEditForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ["description"]
        widgets = {"description": forms.Textarea()}