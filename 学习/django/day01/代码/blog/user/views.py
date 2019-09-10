import datetime
import os

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import json

# Create your views here.
from django.urls import reverse

from blog import settings


def login(request):

    return HttpResponse('login')


# 跳转到login这个地址
def index(request):

    # reverse生成路由地址，需要加上一个路由名称
    url = reverse('us:lg')

    return redirect(url)


# 如果获取路由中正则匹配的参数值，需要在视图函数里面加参数
# 参数的格式和路由中的参数的个数一直
def list(request, age, name):
    print(name)
    print(age)
    return HttpResponse('list')


def info(request, age, name):
    print(name, age)
    return HttpResponse('info')


def foo(request):

    # 以？形式传参，获取参数的方式是  request.GET, 结果是一个字典
    name = request.GET.get('name')
    age = request.GET.get('age')
    namelist = request.GET.getlist('name') # 获取多个名称一样的参数的值
    print(name)
    print(age)
    print(namelist)

    return HttpResponse('foo')



def posts(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    namelist = request.POST.getlist('name')
    print(name)
    print(age)
    print(namelist)

    return HttpResponse('posts')



def puts(request):

    # 用request对象的body属性
    data = request.body

    # 先把字节转成字符串
    data = data.decode()

    # 把字符串转成字典
    data = json.loads(data)

    print(data)
    print(data.get('name'))

    return HttpResponse('puts')




def deletes(request):

    # 用request对象的body属性
    data = request.body

    # 先把字节转成字符串
    data = data.decode()

    # 把字符串转成字典
    data = json.loads(data)

    print(data)
    print(data.get('name'))

    return HttpResponse('deletes')

# 上传图片
def files(request):

    # 需要用到request对象的FILE属性
    file = request.FILES.get('img')

    #获取图片的名称
    filename = file.name

    # 获取文件的后缀
    _, ext = os.path.splitext(filename)

    # 20190910093030
    new_file_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ext


    # 把上传的图片信息写入到需要保存的文件中
    filepath = os.path.join(settings.BASE_DIR, 'uploads', new_file_name)

    # 打开这个文件路径
    with open(filepath, 'ab') as fp:

        # 写入图片信息要把图片切分成多个模块来写入
        # chunks 把文件信息切分成多个块保存在列表里面
        for chunk in file.chunks():
            fp.write(chunk)

def methods(request):

    # 判断请求方式 request.method
    if request.method == 'GET':
        data = 'get'
    elif request.method == 'POST':
        data = 'post'
    elif request.method == 'PUT':
        data = 'put'
    else:
        data = 'delete'

    print(request.path)

def jsondata(request):

    # 如果要传递json数据
    # 那么直接用jsonResponse加上字典类型的数据
    data ={'name': 'laowang', 'age': 40}

    # JsonResponse中safa默认为True，那么只能返回json格式的数据
    # 如果想返回列表类型的数据，需要把safe参数的值改为False
    return JsonResponse(data, safe=False)