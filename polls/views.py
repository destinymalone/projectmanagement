# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import views
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from polls.models import CreateBoard, UserBoardList, UserListCard
from polls.forms import BoardListForm, UserCardForm, CreateBoardForm, BoardEditForm, ListEditForm, CardEditForm
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


class BoardDetailView(LoginRequiredMixin, DetailView):
    template_name = "boards/board/detail.html"
    context_object_name = 'board'
    pk_url_kwarg = "id"

    def get_queryset(self):
        return self.request.user.createboard_set.all()

# class BoardEditView(LoginRequiredMixin, UpdateView):
#     model = CreateBoard
#     form_class = BoardEditForm
#     pk_url_kwarg = "id"
#     template_name = "boards/board/edit.html"
#     success_url = reverse_lazy("boards/board/board.html")


# class BoardDeleteView(LoginRequiredMixin, DeleteView):
#     model = CreateBoard
#     pk_url_kwarg = "id"
#     success_url = reverse_lazy("boards/board/board.html")

class UserBoardList(LoginRequiredMixin, CreateView):
    form_class = BoardListForm
    template_name = "boards/list/list.html"
    success_url = reverse_lazy("list_create")

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(object_list=object_list, **kwargs)
    #     context["header"] = CreateBoard.objects.get(title=title)
    #     return context


class UserListDetail(LoginRequiredMixin, DetailView):
    form_class = BoardListForm
    template_name = 'boards/board/detail.html'
    context_object_name = 'list_detail'
    pk_url_kwarg = "id"

    def get_queryset(self):
        return self.request.user.userboardlist_set.all()



# class ListEditView(LoginRequiredMixin, UpdateView):
#     model = UserBoardList
#     form_class = ListEditForm
#     pk_url_kwarg = "id"
#     template_name = "boards/list/edit.html"
#     success_url = reverse_lazy("boards/list/list.html")


# class ListDeleteView(LoginRequiredMixin, DeleteView):
#     model = UserBoardList
#     pk_url_kwarg = "id"
#     success_url = reverse_lazy("boards/list/list.html")

# class UserListCard(CreateView, LoginRequiredMixin):
#     form_class = UserCardForm
#     template_name = "boards/card.html"
#     success_url = reverse_lazy("boards/card/card.html")

# class UserCardDetail(ListView, LoginRequiredMixin):
#     form_class = UserCardForm
#     template_name = "boards/card/card.html"
#     def get_context_data(self, **kwargs):
#             context = super(UserListDetail).get_context_data(**kwargs)
#             context['card'] = UserBoardList.objects.filter(id=self.object.id)
#             success_url = reverse_lazy("boards/card/card.html")
#             return context
#     # card = UserListCard.objects.all()

# class CardEditView(LoginRequiredMixin, UpdateView):
#     model = UserListCard
#     form_class = CardEditForm
#     pk_url_kwarg = "id"
#     template_name = "boards/card/edit.html"
#     success_url = reverse_lazy("boards/card/card.html")


# class CardDeleteView(LoginRequiredMixin, DeleteView):
    # model = UserListCard
    # pk_url_kwarg = "id"
    # success_url = reverse_lazy("boards/card/cards.html")