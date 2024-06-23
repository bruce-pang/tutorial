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
from django.urls import path
from quikstart import views as quick_views
from serializer_quik import views as serial_views
from permission_demo import views as perm_views

urlpatterns = [
    # path('login/', quick_views.LoginView.as_view()),
    # path('user/', quick_views.UserView.as_view()),
    # path('order/', quick_views.OrderView.as_view()),

    path('api/<str:version>/depart/', serial_views.DepartView.as_view(), name='depart'),
    path('api/<str:version>/user/', serial_views.UserView.as_view(), name='user'),

    path('login/', perm_views.LoginView.as_view()),
    path('user/', perm_views.UserView.as_view()),
    path('order/', perm_views.OrderView.as_view()),
    path('avatar/', perm_views.AvatarView.as_view()),
]
