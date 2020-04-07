# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import views
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from polls.models import CreateBoard, UserBoardList, UserListCard
from polls.forms import CreateListForm, CreateCardForm, CreateBoardForm, BoardEditForm, ListEditForm, CardEditForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, request
from django.urls import reverse_lazy


# Create your views here.

class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("board")

class CreateBoardView(LoginRequiredMixin, CreateView):
    form_class = CreateBoardForm
    template_name = 'boards/board/board.html'
    success_url = reverse_lazy("board")

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_create'] = CreateListForm()
        context['list_edit'] = ListEditForm()
        context['card_create'] = CreateCardForm()
        context['card_edit'] = CardEditForm()
        return context


class BoardDetailView(LoginRequiredMixin, DetailView):
    template_name = "boards/board/detail.html"
    context_object_name = 'board'
    pk_url_kwarg = "id"

    def get_queryset(self):
        return self.request.user.createboard_set.all()

class BoardEditView(LoginRequiredMixin, UpdateView):
    model = CreateBoard
    form_class = BoardEditForm
    pk_url_kwarg = "id"
    # template_name = "boards/board/edit.html"
    success_url = reverse_lazy("board")


class BoardDeleteView(LoginRequiredMixin, DeleteView):
    model = CreateBoard
    pk_url_kwarg = "id"
    success_url = reverse_lazy("board")

class BoardListView(LoginRequiredMixin, CreateView):
    form_class = CreateListForm
    template_name = "boards/board/board.html"
    success_url = reverse_lazy("list_create")

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class ListDetailView(LoginRequiredMixin, DetailView):
    form_class = CreateListForm
    template_name = 'boards/board/detail.html'
    context_object_name = 'list_detail'
    pk_url_kwarg = "id"

    def get_queryset(self):
        return self.request.user.userboardlist_set.all()



class ListEditView(LoginRequiredMixin, UpdateView):
    model = UserBoardList
    form_class = ListEditForm
    pk_url_kwarg = "id"
    # template_name = "boards/board/board.html"
    success_url = reverse_lazy("board")


class ListDeleteView(LoginRequiredMixin, DeleteView):
    model = UserBoardList
    pk_url_kwarg = "id"
    success_url = reverse_lazy("board")

class ListCardView(CreateView, LoginRequiredMixin):
    form_class = CreateCardForm
    template_name = "boards/board/board.html"
    success_url = reverse_lazy("board")

class CardDetailView(ListView, LoginRequiredMixin):
    form_class = CreateCardForm
    template_name = "boards/board/detail.html"
    context_object_name = 'card_detail'
    pk_url_kwarg = "id"

    def get_queryset(self):
        return self.request.user.userboardlist_set.all()
   

class CardEditView(LoginRequiredMixin, UpdateView):
    model = UserListCard
    form_class = CardEditForm
    pk_url_kwarg = "id"
    # template_name = "boards/card/edit.html"
    success_url = reverse_lazy("board")


class CardDeleteView(LoginRequiredMixin, DeleteView):
    model = UserListCard
    pk_url_kwarg = "id"
    success_url = reverse_lazy("board")