from django.urls import path

from album import views

urlpatterns = [
    path('album', views.album, name="album"),
]