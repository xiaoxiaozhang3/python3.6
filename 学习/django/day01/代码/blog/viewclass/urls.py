# -*- coding: utf-8 -*-
# @Time : 2019/9/10 11:18
# @Author : xiaoxiaozhang
# @Site : 
# @File : urls.py
# @Software: PyCharm
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^index/$', views.Index.as_view())
]