from django.contrib import admin
from django.urls import path,  include
from django.contrib.auth import views as auth_views
from polls.views import (
    RegistrationView, 
    CreateBoardView, 
    UserDetailView,
    UserEditView,
    UserDeleteView, 
    UserBoardList,
    UserListDetail,
    UserListEdit,
    UserListDelete, 
    UserListCard, 
    UserListDetail,
    UserCardDetail, 
    UserCardEdit,
    UserCardDelete,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register/", RegistrationView.as_view()),
    path("board/", CreateBoardView.as_view()),
    path("board/detail<id>/", UserDetailView.as_view()),
    path("board/edit<id>/", UserEditView.as_view()),
    path("board/delete<id>/", UserDeleteView.as_view()),
    path("list/", UserBoardList.as_view()),
    path("list/detail<id>", UserListDetail.as_view()),
    path("list/edit<id>", UserListEdit.as_view()),
    path("list/delete<id>", UserListDelete.as_view()),
    path("card/", UserListCard.as_view()),
    path("card/detail<id>", UserCardDetail.as_view()),
    path("card/edit<id>", UserCardEdit.as_view()),
    path("card/delete<id>", UserCardDelete.as_view()),
    path('polls/', include('polls.urls')),
]
