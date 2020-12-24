from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('board', views.board, name="board"),
    path('board_write', views.board_write, name="board_write"),
    path('board_insert', views.board_insert, name="board_insert"),
    path('board_view', views.board_view, name="board_view"),
]