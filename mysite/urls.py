from django.contrib import admin
from django.urls import path,  include
from django.contrib.auth import views as auth_views
from polls.views import (RegistrationView, CreateBoardView, UserDetailView, UserBoardList, UserListCard, UserListDetail, UserCardDetail)



urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register/", RegistrationView.as_view()),
    path("board/", CreateBoardView.as_view()),
    path("board/detail<id>/", UserDetailView.as_view()),
    path("list/", UserBoardList.as_view()),
    path("list/detail", UserListDetail.as_view()),
    path("card/", UserListCard.as_view()),
    path("card/detail", UserCardDetail.as_view()),
    path('polls/', include('polls.urls')),
]
