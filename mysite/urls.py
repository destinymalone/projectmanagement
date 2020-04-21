from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path,  include
from django.contrib.auth import views as auth_views
from polls.views import (
    RegistrationView, 
    CreateBoardView, 
    BoardDetailView,
    BoardDeleteView, 
    CreateListView,
    # ListDetailView,
    ListEditView,
    ListDeleteView,   
    CreateCardView, 
    CardEditView,
    CardDeleteView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register/", RegistrationView.as_view()),
    path("", CreateBoardView.as_view(), name="board"),
    path("board/detail/<id>/", BoardDetailView.as_view(), name="board_detail"),
    path("board/delete<id>/", BoardDeleteView.as_view(), name="board_delete"),
    path("list/<id>", CreateListView.as_view(), name="list_create"),
    # path("list/detail/<id>/", ListDetailView.as_view(), name="list_detail"),
    path("list/edit/<id>/", ListEditView.as_view(), name="list_edit"),
    path("list/delete/<id>/", ListDeleteView.as_view(), name="list_delete"),
    path("card/<id>/", CreateCardView.as_view(), name="card_create"),
    path("card/edit/<id>/", CardEditView.as_view(), name="card_edit"),
    path("card/delete/<id>/", CardDeleteView.as_view(), name="card_delete"),
]

urlpatterns += staticfiles_urlpatterns()
