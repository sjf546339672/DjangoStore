import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_framework.views import APIView

from mymanage.models import UsersModel


def index(request):
    return HttpResponse("111")


class RegisterView(APIView):

    def get(self, request):
        return render(request, "web/register.html")

    @csrf_exempt
    def post(self, requset):
        all_data = requset.POST
        username = all_data["username"]
        name = all_data["name"]
        password = all_data["password"]
        repassword = all_data["repassword"]
        sex = int(all_data["sex"])  # 1表示男 0表示女
        data = {
            "username": username,
            "name": name,
            "password": password,
            "sex": sex,
        }
        username_count = UsersModel.objects.filter(username=username).count()
        name_count = UsersModel.objects.filter(name=name).count()

        if (username_count > 0) or (name_count > 0) or \
                (password != repassword) or \
                password == "":
            return render(requset, "web/register.html")
        else:
            UsersModel.objects.create(**data)
            return render(requset, "web/login.html")


class LoginView(APIView):

    def get(self, request):
        return render(request, "web/login.html")

    def post(self, request):
        all_data = request.POST
        username = all_data["username"]
        password = all_data["password"]
        user = UsersModel.objects.get(username=username)
        print(user.state)
        return HttpResponse("11111")




