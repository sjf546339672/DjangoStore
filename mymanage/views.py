import io
import json
import random

from PIL import Image, ImageDraw, ImageFont
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_framework.views import APIView

from mymanage.models import UsersModel


def index(request):
    return render(request, 'web/index.html')


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
        user = get_object_or_404(UsersModel, username=username, password=password)
        return render(request, 'web/login.html', {"user": user})


class CreateVericationCode(APIView):

    def post(self, request):
        def verication_code():
            # 定义背景颜色
            bgcolor = (
            random.randrange(20, 100), random.randrange(20, 100), 100)
            width, height = 100, 25  # 定义宽高

            im = Image.new('RGB', (width, height), bgcolor)  # 创建画面对象
            draw = ImageDraw.Draw(im)  # 创建画笔对象

            # 调用画笔的point()函数绘制噪点
            for i in range(0, 100):
                xy = (random.randrange(0, width), random.randrange(0, height))
                fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
                draw.point(xy=xy, fill=fill)

            str_code = "0123456789"  # 验证码备选值
            rand_str = ""
            # 随机获取四位验证码
            for i in range(0, 4):
                rand_str += str_code[random.randrange(0, len(str_code))]
            print(rand_str)

            # 构造字体对象，ubuntu的字体路径为/usr/share/fonts/truetype/freefont”
            font = ImageFont.truetype('static/msyh.txt', 21)  # 改为静态资源目录下的字体文件
            fontcolor = (
            255, random.randrange(0, 255), random.randrange(0, 255))

            # 绘制四个字
            draw.text(xy=(5, -3), text=rand_str[0], font=font, fill=fontcolor)
            draw.text(xy=(25, -3), text=rand_str[1], font=font, fill=fontcolor)
            draw.text(xy=(50, -3), text=rand_str[2], font=font, fill=fontcolor)
            draw.text(xy=(75, -3), text=rand_str[3], font=font, fill=fontcolor)

            # 释放画笔
            del draw

            # 存入session,用于进一步验证
            request.session["verifycode"] = rand_str
            """
            python2的为
            # 内存文件操作
            import cStringIO
            buf = cStringIO.StringIO()
            """
            # 内存文件操作-->此方法为python3的
            buf = io.BytesIO()
            # 将图片保存在内存中，文件类型为png
            im.save(buf, "png")
            # 将内存中的图片数据返回给客户端，MIME类型为图片png
            return HttpResponse(buf.getvalue(), "image/png")
