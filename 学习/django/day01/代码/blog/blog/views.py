# 视图函数一定要有一个参数，但一般建议就是request
from django.http import HttpResponse


def index(request):

    # 返回hello world的数据
    return HttpResponse('hello world')


def list(request):

    # 返回hello world的数据
    return HttpResponse('list')