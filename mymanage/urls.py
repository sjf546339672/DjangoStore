# coding: utf-8
from django.urls import path

from .views import (index, RegisterView, LoginView)

urlpatterns = [
    path("index/", index, name="index"),
    path("", RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
]
