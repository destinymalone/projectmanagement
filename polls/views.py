# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import views
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
# from polls.models import CreateBoard
from polls.forms import CreateBoardForm
from django.http import HttpResponseRedirect, request
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'

class CreateBoardView(CreateView, LoginRequiredMixin):
    form_class = CreateBoardForm
    template_name = 'boards/board.html'

class UserDetailView(views.View):
    def get(self, request, id):
        board = CreateBoard.objects.select_related("user").get(id=id)
        return render(request, "boards/detail.html", {"board": board, "form": CreateBoardForm()}) 