# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from models import Category
# Create your views here.
import urllib
import urllib2
import requests
import json
import re


def index(request):
    # response = requests.get("http://api.map.baidu.com/telematics/v3/weather?location= 郑州市&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?")
    # result = response.text
    # result = json.loads(result)
    # weather = result['results'][0]['weather_data'][0]
    # url = "http://v.juhe.cn/weather/index"
    # response = requests.get(url,{
    #     "cityname":u"郑州",
    #     "dtype":"json",
    #     "key":"5aa4a1690e74840738b6cf611a400e8d"
    # })
    # json_str = response.text
    # print json_str
    return render(request, "index.html",)
    # return render(request, "index.html",{
    #     "city_name":u"郑州",
    #     "weather":weather,
    # })


def cate_add(request):
    if request.method == "POST":
        cate_name = request.POST.get("cate_name","")
        cate_pid = int(request.POST.get("cate_pid",0))
        if cate_pid == 0:
            cate = Category()
            cate.cate_name = cate_name
            cate.cate_pid = cate_pid
            cate.cate_level = 0
            # 插入
            cate.save()
            cate.cate_path = str(cate.id) + ','
            # 更新
            cate.save()
        else:
            # 查一下上级元素
            p_cate = Category.objects.filter(id=cate_pid)
            if not p_cate:
                return HttpResponse("Parent Category Not Exists!!!")
            # 因为一个分类顶多在表里找到一个 所以取第0个
            p_cate = p_cate[0]
            cate = Category()
            cate.cate_name = cate_name
            cate.cate_pid = cate_pid
            cate.cate_level = 0
            cate.save()
            cate.cate_level = p_cate.cate_level + 1
            cate.cate_path = p_cate.cate_path+str(cate.id) + ','
            cate.save()

        return HttpResponse("add successfully")
    categorys = select_all_categorys()
    return render(request,"cate_add.html",{
        "categorys":categorys,
    })


def cate_delete(request):
    error = dict()
    if request.method == "POST":
        id = int(request.POST.get("id",0))
        cate = Category.objects.filter(id=id)
        if cate:
            cate[0].delete()
            error['status'] = 1
            error['msg'] = u"删除成功！！！"
            return HttpResponse(json.dumps(error), content_type="application/json", status=200)
        else:
            error['status'] = 0
            error['msg'] = u"该分类不存在！！！"
            return HttpResponse(json.dumps(error), content_type="application/json", status=404)
    error['status'] = 0
    error['msg'] = u"请求方法不合适！！！"
    return HttpResponse(json.dumps(error),content_type="application/json",status=404)


def cate_update(request):
    error = dict()
    if request.method == "POST":
        id = int(request.POST.get("id",0))
        cate_name = request.POST.get("cate_name",0)
        cate_pid = int(request.POST.get("cate_pid",0))
        cate = Category.objects.filter(id=id)
        if cate:
            cate = cate[0]
            cate.cate_name = cate_name
            cate.cate_pid = cate_pid
            cate.save()
            error['status'] = 1
            error['msg'] = u"删除成功！！！"
            return HttpResponse(json.dumps(error), content_type="application/json", status=200)

        else:

            error['status'] = 0
            error['msg'] = u"该分类不存在！！！"
            return HttpResponse(json.dumps(error), content_type="application/json", status=404)

    error['status'] = 0
    error['msg'] = u"请求方法不合适"
    return HttpResponse(json.dumps(error),content_type="application/json")


def cate_select(request):
    categorys = select_all_categorys()
    return render(request,"cate_select.html",{
        "categorys":categorys,
    })


def select_all_categorys():
    categorys = Category.objects.order_by("cate_path").all()
    for cate in categorys:
        cate.cate_name = "|--" * cate.cate_level + cate.cate_name
    return categorys


def get_weather(request):
    response = requests.get("http://api.map.baidu.com/telematics/v3/weather?location= 郑州市&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?")
    # 这里result是json字符串
    result = response.text
    # result = json.loads(result)
    # weather = result['results'][0]['weather_data'][0]
    return HttpResponse(result)


def get_phone(request):
    if request.method == "POST":

        phone = request.POST.get("phone","")
    else:
        phone = request.GET.get("phone", "")
    pattern = re.compile("^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$")
    if pattern.match(phone):

    # 参数只有一个 用%s不值当，所以用+拼接
        response = requests.get("http://sj.apidata.cn/?mobile=" + phone)
        result = response.text
        return HttpResponse(result,content_type="application/json",status=400)

    error = dict()
    error['status'] = 0
    error['message'] = "Not a phone"
    # 字典怎么转成字符串
    #json.dumps() # 字典转字符串
    # json.loads() 字符串转字典

    return HttpResponse(json.dumps(error),content_type="application/json")

def music(request):

    if request.method == "GET":
        type = request.GET.get("type", "")
        if type:
            url = "http://tingapi.ting.baidu.com/v1/restserver/ting?format=json&method=baidu.ting.billboard.billList&type=2&size=50&offset=0"
            response = requests.get(url)
            result = response.text
            return HttpResponse(result)
    return render(request,"music.html")
