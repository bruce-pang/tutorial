import datetime

import django
from django.shortcuts import render
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from serializer_quik.models import Depart, User


# 由于json.dumps()无法序列化datetime, decimal类型，所以需要使用DRF的序列化器
#class DepartSerializer(serializers.Serializer): #字段多了，可以使用ModelSerializer
#    title = serializers.CharField()
#    order = serializers.IntegerField()
#    count = serializers.IntegerField()

class DepartSerializer(serializers.ModelSerializer): # 多字段建议使用ModelSerializer
    class Meta:
        model = Depart
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    # ctime = serializers.DateTimeField(format="%Y-%m-%d", source="createtime")
    #ctime = serializers.DateTimeField(format="%Y-%m-%d", source="updatetime")
    gender = serializers.CharField(source="get_gender_display") # 通过get_字段名_display()方法获取choices的值
    depart = serializers.CharField(source="depart.title")
    age = serializers.IntegerField()
    class Meta:
        model = User
        # fields = "__all__" # 正常被序列化
        fields = ["name", "age", "gender","depart", "createtime"] # 指定序列化的字段

class DepartView(APIView):
    authentication_classes = []
    def get(self, request, *args, **kwargs):
        # 1.从数据库中获取数据
        # dept_obj = Depart.objects.all().first() # 获取第一个对象
        queryset = Depart.objects.all() # 获取所有对象 QuerySet类型
        # 2.JSON序列化
        ser = DepartSerializer(instance=queryset, many=True) # 序列化的结果是字典类型
        # 3.返回响应
        context = {
            "code": 200,
            "data": ser.data
        }
        return Response(context)

class UserView(APIView):
    authentication_classes = []
    def get(self, request, *args, **kwargs):
        # User.objects.all().update(createtime=datetime.datetime.now())
        User.objects.all().update(createtime=timezone.now())
        # 1.从数据库中获取数据
        user_list = User.objects.all()# 获取第一个对象
        # 2.JSON序列化
        ser = UserSerializer(instance=user_list, many=True) # 序列化的结果是字典类型
        # 3.返回响应
        context = {
            "code": 200,
            "data": ser.data
        }
        return Response(context)