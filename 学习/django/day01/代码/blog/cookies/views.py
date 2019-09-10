from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):

    # 创建cookies是用到响应对象来创建
    # 响应对象有： HttpResponse JsonResponse redirect

    res = HttpResponse('cookies')

    # 设置cookie
    # res.set_cookie('username','laowang')

    # 获取cookie，使用请求对象的request对象的COOKIES属性
    cookie = request.COOKIES.get('username')

    # 删除cookie，用响应对象
    # HttpResponse.delete_cookie(key)

    return res

def sess(request):

    # 设置session
    # request.session['name'] = 'abc'

    # 获取session，用request对象
    data = request.session.get("name")
    print(data)

    # 删除整个 session
    # request.session.flush()

    # 设置session的过期时间
    request.session.set_expiry(20)

    return HttpResponse('sess')