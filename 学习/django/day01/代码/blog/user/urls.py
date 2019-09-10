from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='lg'),
    url(r'^index/$', views.index),

    # get方式以/来按照顺序传递参数
    url(r'^list/(\w+)/(\d+)/$', views.list),

    # get方式以/按照路由的正则名称传递参数
    url(r'^info/(?P<name>\w+)/(?P<age>\d+)/$', views.info),


    # get方式以？的形式传参
    url(r'^foo/$', views.foo),


    # post方式传参数
    url(r'^posts/$', views.posts),


    # put方式传参
    url(r'^puts/$', views.puts),


    # delete方式传参
    url(r'^deletes/$', views.deletes),

    # 把所有的请求方法卸载一个视图函数中
    url(r'methods',views.methods),



]