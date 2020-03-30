# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import views
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from polls.models import CreateBoard, UserBoardList, UserListCard
from polls.forms import CreateBoardForm, BoardEditForm, UserListForm, ListEditForm, UserCardForm, CardEditForm
from django.http import HttpResponseRedirect, request
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserListForm, UserCardForm


# Create your views here.

class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'

class CreateBoardView(CreateView, LoginRequiredMixin):
    form_class = CreateBoardForm
    template_name = 'boards/board/board.html'

class UserDetailView(views.View, LoginRequiredMixin):
    def get(self, request, id):
        username = CreateBoard.objects.select_related("user").get(id=id)
        return render(request, "boards/board/detail.html", {"User": username, "form": CreateBoardForm()})

class BoardEditView(LoginRequiredMixin, UpdateView):
    model = CreateBoard
    form_class = BoardEditForm
    pk_url_kwarg = "id"
    template_name = "boards/board/edit.html"
    success_url = reverse_lazy("board")


class BoardDeleteView(LoginRequiredMixin, DeleteView):
    model = CreateBoard
    pk_url_kwarg = "id"
    success_url = reverse_lazy("board")

# class UserBoardList(CreateView, LoginRequiredMixin):
#     form_class = UserListForm
#     template_name = "boards/list.html"

class UserListDetail(ListView, LoginRequiredMixin):
    form_class = UserListForm
    template_name = "boards/list/list.html"
    list = UserBoardList.objects.all()

class ListEditView(LoginRequiredMixin, UpdateView):
    model = UserBoardList
    form_class = ListEditForm
    pk_url_kwarg = "id"
    template_name = "boards/list/edit.html"
    success_url = reverse_lazy("list")


class ListDeleteView(LoginRequiredMixin, DeleteView):
    model = UserBoardList
    pk_url_kwarg = "id"
    success_url = reverse_lazy("list")

# class UserListCard(CreateView, LoginRequiredMixin):
#     form_class = UserCardForm
#     template_name = "boards/card.html"

class UserCardDetail(ListView, LoginRequiredMixin):
    form_class = UserCardForm
    template_name = "boards/card/card.html"
    card = UserListCard.objects.all()

class CardEditView(LoginRequiredMixin, UpdateView):
    model = UserListCard
    form_class = CardEditForm
    pk_url_kwarg = "id"
    template_name = "boards/card/edit.html"
    success_url = reverse_lazy("card")


class CardDeleteView(LoginRequiredMixin, DeleteView):
    model = UserListCard
    pk_url_kwarg = "id"
    success_url = reverse_lazy("card")