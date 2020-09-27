# coding: utf-8
from django.urls import path

from .views import (index, RegisterView, LoginView, CreateVericationCode)

urlpatterns = [
    path("index/", index, name="index"),
    path("", RegisterView.as_view(), name="register"),  # 注册界面
    path("login", LoginView.as_view(), name="login"),  # 登录界面
    path("verify", CreateVericationCode.as_view(), name="myadmin_verify"),
    path("verify_test", CreateVericationCode.as_view(), name="admin")
]

