from django.contrib import admin
from django.urls import path,  include
from django.contrib.auth import views as auth_views
from polls.views import (
    RegistrationView, 
    CreateBoardView, 
    BoardDetailView,
    BoardEditView,
    BoardDeleteView, 
    UserBoardList,
    UserListDetail,
    ListEditView,
    ListDeleteView, 
    UserListCard, 
    UserListDetail,
    UserCardDetail, 
    CardEditView,
    CardDeleteView,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register/", RegistrationView.as_view()),
    path("board/", CreateBoardView.as_view(), name="board"),
    path("board/detail/<id>/", BoardDetailView.as_view(), name="board_detail"),
    # path("board/edit<id>/", BoardEditView.as_view()),
    # path("board/delete<id>/", BoardDeleteView.as_view()),
    # path("list/", UserBoardList.as_view()),
    # path("list/detail<id>", UserListDetail.as_view()),
    # path("list/edit<id>", ListEditView.as_view()),
    # path("list/delete<id>", ListDeleteView.as_view()),
    # path("card/", UserListCard.as_view()),
    # path("card/detail<id>", UserCardDetail.as_view()),
    # path("card/edit<id>", CardEditView.as_view()),
    # path("card/delete<id>", CardDeleteView.as_view()),
    # path('polls/', include('polls.urls')),
]
