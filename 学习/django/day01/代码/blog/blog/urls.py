"""blog URL Configuration

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

from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 导入子应用的urls
    # 第一个参数是子应用的路由前缀，不要加$
    # 第二个参数是导入子应用路由
    url(r'^user/', include('user.urls', namespace='us')),

    # url第一个参数是配置路由的正则表达式
    # 第二个参数是视图函数,函数名称不加括号
    url(r'^index/$', views.index),

    url(r'^index/list/$', views.list),

    # cookies的子应用
    url(r'^cookies/', include('cookies.urls')),

    url(r'^uesr/', include('user.urls')),

    url(r'^viewclass/', include('viewclass.urls')),




]
