# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import views
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from polls.models import CreateBoard, UserBoardDetail, UserBoardList, UserCardDetail
from polls.forms import CreateBoardForm
from django.http import HttpResponseRedirect, request
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserListForm, UserCardForm


# Create your views here.

class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'

class CreateBoardView(CreateView, LoginRequiredMixin):
    form_class = CreateBoardForm
    template_name = 'boards/board.html'

class UserDetailView(views.View, LoginRequiredMixin):
    def get(self, request, id):
        username = CreateBoard.objects.select_related("user").get(id=id)
        return render(request, "boards/detail.html", {"User": username, "form": CreateBoardForm()})

# class UserBoardList(CreateView, LoginRequiredMixin):
#     form_class = UserListForm
#     template_name = "boards/list.html"

class UserListDetail(ListView, LoginRequiredMixin):
    form_class = UserListForm
    template_name = "boards/list.html"
    list = UserBoardDetail.objects.all()

# class UserListCard(CreateView, LoginRequiredMixin):
#     form_class = UserCardForm
#     template_name = "boards/card.html"

class UserCardDetail(ListView, LoginRequiredMixin):
    form_class = UserCardForm
    template_name = "boards/card.html"
    card = UserCardDetail.objects.all()