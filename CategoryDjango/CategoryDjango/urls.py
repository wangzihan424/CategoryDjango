"""CategoryDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from main import views as main_views
from users import views as users_views



urlpatterns = [
    url(r'^cate_add/', main_views.cate_add, name="cate_add"),
    url(r'^cate_delete/', main_views.cate_delete, name="cate_delete" ),
    url(r'^cate_update/', main_views.cate_update, name="cate_update"),
    url(r'^cate_select/', main_views.cate_select, name="cate_select"),
    url(r'^weather/',main_views.get_weather, name="weather"),
    url(r'^phone',main_views.get_phone,name="phone"),
    url(r'^music/',main_views.music, name="music"),
    url(r'^login/',users_views.login, name="login"),
    url(r'^regist/',users_views.regist, name="regist"),
    url(r'', main_views.index),
]
