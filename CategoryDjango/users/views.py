# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from models import UserInfo
from django.http import HttpResponse
import json
from tools import secure

# Create your views here.


def login(request):
    return_data = dict()
    if request.method == "POST":
        user_name = request.POST.get("user_name", "")
        user_psw = request.POST.get("user_psw", "")
        result = UserInfo.objects.filter(user_name=user_name)
        if result:
            if secure.md5_32(user_psw) == result[0].user_psw:
                return_data["status"] = 1
                return_data["msg"] = "登陆成功"
                return HttpResponse(json.dumps(return_data), content_type="application/json", status=200)
            else:
                return_data["status"] = 0
                return_data["msg"] = "密码错误"
                return HttpResponse(json.dumps(return_data), content_type="application/json", status=404)
        else:
            return_data["status"] = 0
            return_data["msg"] = "用户名不正确"
            return HttpResponse(json.dumps(return_data), content_type="application/json", status=404)

    return render(request, "login.html", {
        "title": "登录页面",
    })


def regist(request):
    # 所有返回数据都写到这里面
    return_data = dict()
    if request.method == "POST":
        user_name = request.POST.get("user_name","")
        user_psw = request.POST.get("user_psw","")
        # 通过正则匹配密码强度，匹配做两次，防止有人恶意更改
        result = UserInfo.objects.filter(user_name=user_name)
        if result:
            return_data["status"] = 0
            return_data["msg"] = "用户名已存在，请换个名字"
            return HttpResponse(json.dumps(return_data),content_type="application/json",status=404)
        else:
            if user_name == "" or user_psw == "":
                return_data["status"] = 0
                return_data["msg"] = "用户名密码不能为空"
                return HttpResponse(json.dumps(return_data), content_type="application/json", status=404)
            user = UserInfo()
            user.user_name = user_name
            user.user_psw = secure.md5_32(user_psw)
            user.user_head = ""
            user.save()
            return_data["status"] = 1
            return_data["msg"] = "注册成功"
            return HttpResponse(json.dumps(return_data), content_type="application/json", status=200)

    return render(request,"regist.html",{
        "title":"注册页面",
    })


