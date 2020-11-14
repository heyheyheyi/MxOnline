from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        user_name = request.POST.get("username", "")
        password = request.POST.get("password", "")

        #用户通过用户名和密码查询用户是否存在
        user = authenticate(username=user_name, password=password)
        if user is not None:
            #查询到用户
            login(request, user)
            #登录成功后返回页面
            return render(request, "index.html")
        else:
            return render(request, "login.html", {"msg": "用户名或者密码错误"})
