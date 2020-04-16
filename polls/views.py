# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import views
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from polls.models import Board, List, Card
from polls.forms import CreateListForm, CreateCardForm, CreateBoardForm, BoardEditForm, ListEditForm, CardEditForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, request
from django.urls import reverse_lazy


# Create your views here.

# Register

class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("board")

# Board

class CreateBoardView(LoginRequiredMixin, CreateView):
    form_class = CreateBoardForm
    template_name = "boards/board/board.html"
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
        return self.request.user.board_set.all()


class BoardDeleteView(LoginRequiredMixin, DeleteView):
    model = Board
    pk_url_kwarg = "id"
    template_name = "boards/board/delete.html"
    success_url = reverse_lazy("board")
    


# List

class BoardListView(LoginRequiredMixin, CreateView):
    form_class = CreateListForm
    template_name = "boards/board/list.html"
    success_url = reverse_lazy("detail")
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['list_create'] = CreateListForm()
        id = self.kwargs['id']
        context['board'] = self.request.user.board_set.get(id=id)
        return context

    def form_valid(self, form):
        form.instance.board_id = self.kwargs['id']
        return super().form_valid(form)
  


class ListDetailView(LoginRequiredMixin, DetailView):
    template_name = "boards/board/detail.html"
    context_object_name = 'list'
    pk_url_kwarg = "id"

    def get_queryset(self):
        return List.objects.filter(board__username=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('Got context!', context)
        return context


class ListEditView(LoginRequiredMixin, UpdateView):
    model = List
    form_class = ListEditForm
    pk_url_kwarg = "id"
    template_name = "boards/board/edit.html"
    success_url = reverse_lazy("board")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['list_edit'] = ListEditForm()
        id = self.kwargs['id']
        context['board'] = self.request.user.board_set.get(id=id)
        return context

    def form_valid(self, form):
        form.instance.board_id = self.kwargs['id']
        return super().form_valid(form)


class ListDeleteView(LoginRequiredMixin, DeleteView):
    model = List
    pk_url_kwarg = "id"
    template_name = "boards/board/delete.html"
    success_url = reverse_lazy("board")



# Card

class ListCardView(CreateView, LoginRequiredMixin):
    form_class = CreateCardForm
    template_name = "boards/board/list.html"
    success_url = reverse_lazy("board_detail")
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['card_create'] = CreateCardForm()
        id = self.kwargs['id']
        print(id)
        context['list'] = self.request.user.board.list_set.get(id=id)
        return context

    def form_valid(self, form):
        form.instance.card_id = self.kwargs['id']
        return super().form_valid(form)
  
  

class CardDetailView(ListView, LoginRequiredMixin):
    form_class = CreateCardForm
    template_name = "boards/board/detail.html"
    context_object_name = 'card'
    pk_url_kwarg = "id"

    def get_queryset(self):
        return list.card_set.all()

class CardEditView(LoginRequiredMixin, UpdateView):
    model = Card
    form_class = CardEditForm
    pk_url_kwarg = "id"
    # template_name = "boards/card/edit.html"
    success_url = reverse_lazy("card_create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['list_create'] = CreateListForm()
        # context['list_edit'] = ListEditForm()
        # context['card_create'] = CreateCardForm()
        context['card_edit'] = CardEditForm()
        return context


class CardDeleteView(LoginRequiredMixin, DeleteView):
    model = Card
    pk_url_kwarg = "id"
    template_name = "boards/board/delete.html"
    success_url = reverse_lazy("list_create")