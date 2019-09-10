from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


from django.views import View

# 类视图要继承View父类
class Index(View):

    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)

    # 类视图规定不同的请求方式要通过相同名称的请求方法来定义
    def get(self, requset):

        return HttpResponse('get')

    def post(self, resquert):

        return HttpResponse('post')