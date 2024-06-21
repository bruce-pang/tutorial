"""
URL configuration for tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path # django组件
from quikstart import views # app组件，引入views.py，用于绑定对应的路由url

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('auth/', views.auth), # FBV: function based view -> 请求进来 函数()

    # /user/123/ => pk=123
    path('user/<int:pk>/<str:name>/', views.UserView.as_view()), # CBV: class based view -> 请求进来 函数()


    path(r'^api/(?P<version>\w+)/users/$', views.UserView.as_view()), # CBV: class based view -> 请求进来 函数()


    # /info/xxxxx/ => dt=xxxxx
    path('info/<str:dt>/', views.InfoView.as_view()), # CBV: class based view -> 请求进来 函数()


]
