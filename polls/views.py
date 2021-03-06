# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import views
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, View
from polls.models import Board, List, Card
from polls.forms import CreateListForm, CreateCardForm, CreateBoardForm, BoardEditForm, ListEditForm, CardEditForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, request
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.decorators.http import require_GET, require_POST


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

class CreateListView(LoginRequiredMixin, CreateView):
    model = List
    fields= ['title']

    def form_valid(self, form):
        form.instance.board_id = self.kwargs['id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('board_detail', args=[self.kwargs['id']])
  


class ListDetailView(LoginRequiredMixin, DetailView):
    template_name = "boards/board/list_detail.html"
    context_object_name = 'list'
    pk_url_kwarg = "id"

    def get_queryset(self):
        return List.objects.filter(board__username=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ListEditView(LoginRequiredMixin, UpdateView):
    model = List
    form_class = ListEditForm
    pk_url_kwarg = "id"
    template_name = "boards/board/list_edit.html"
    success_url = reverse_lazy("board")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_edit'] = ListEditForm()
        id = self.kwargs['id']
        context['board'] = Board.objects.filter(pk=id)

        return context


class ListDeleteView(LoginRequiredMixin, DeleteView):
    model = List
    pk_url_kwarg = "id"
    template_name = "boards/board/list_delete.html"
    context_object_name = 'list'
    success_url = reverse_lazy("board")

    def get_queryset(self):
        return List.objects.filter(board__username=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



# Card

class CreateCardView(LoginRequiredMixin, CreateView):
    model = Card
    fields = ['description']

    def form_valid(self, form):
        form.instance.list_id = self.kwargs['id']
        return super().form_valid(form)

    def get_success_url(self):
        list = List.objects.get(id=self.kwargs['id'])
        board = list.board
        return reverse('board_detail', args=[board.id])
  

class CardEditView(LoginRequiredMixin, UpdateView):
    model = Card
    form_class = CardEditForm
    pk_url_kwarg = "id"
    template_name = "boards/card/card_edit.html"
    success_url = reverse_lazy("board")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['card_edit'] = CardEditForm()
        return context


class CardDeleteView(LoginRequiredMixin, View):
    def post(self, request, id):
        card = Card.objects.get(id=id)
        list = card.list
        board = list.board
        if board.username == request.user:
            card.delete()
            return redirect('board_detail', board.id)
        else:
            return redirect('board')

class CardMoveView(LoginRequiredMixin, UpdateView):
    model = Card
    fields = ['list']
    pk_url_kwarg = 'id'

    def get_success_url(self):
        card = Card.objects.get(id=self.kwargs['id'])
        list = card.list
        board = list.board
        return reverse('board_detail', args=[board.id])

# Ordering Lists/Cards


