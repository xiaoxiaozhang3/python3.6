# -*- coding: utf-8 -*-
# @Time : 2019/9/10 10:30
# @Author : xiaoxiaozhang
# @Site : 
# @File : urls.py
# @Software: PyCharm
from django.http import HttpResponse
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^cookis/',views.index)
]