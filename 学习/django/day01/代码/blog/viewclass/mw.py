# -*- coding: utf-8 -*-
# @Time : 2019/9/10 16:10
# @Author : xiaoxiaozhang
# @Site : 
# @File : mw.py
# @Software: PyCharm

# 新的中间件定义方法就是装饰器的写法
from django.http import HttpResponse


def outer(func):
    def inner(request):
        # 视图函数执行之前需要写的逻辑
        print('before')

        res = func(request) # 执行的是视图函数中的代码

        # 视图函数执行之后的逻辑
        print('after')

        return res

    return inner

# 旧的中间件
from django.utils.deprecation import MiddlewareMixin

class MyMiddleware(MiddlewareMixin):

    # 如果这个函数返回None,会继续往下执行
    # 如果返回响应对象,就停止执行视图函数的代码，继续执行process_response
    def process_request(self, request):
        print('before1')
        return HttpResponse('ok')

    def process_response(self, request, response):

        return response