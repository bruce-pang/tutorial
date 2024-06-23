import datetime

import django
from django.shortcuts import render
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from serializer_quik.models import Depart, User, Tag


# 由于json.dumps()无法序列化datetime, decimal类型，所以需要使用DRF的序列化器
#class DepartSerializer(serializers.Serializer): #字段多了，可以使用ModelSerializer
#    title = serializers.CharField()
#    order = serializers.IntegerField()
#    count = serializers.IntegerField()

class BaseSerializer(serializers.Serializer):
    xx = serializers.CharField(source="name")

class DepartSerializer(serializers.ModelSerializer): # 多字段建议使用ModelSerializer
    class Meta:
        model = Depart
        fields = "__all__"

class D1(serializers.ModelSerializer):
    class Meta:
        model = Depart
        fields = ["title", "order"]

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer, BaseSerializer):
    ctime = serializers.DateTimeField(format="%Y-%m-%d", source="createtime")
    #ctime = serializers.DateTimeField(format="%Y-%m-%d", source="updatetime")
    gender = serializers.CharField(source="get_gender_display") # 通过get_字段名_display()方法获取choices的值
    # depart = serializers.CharField(source="depart.title")
    # age = serializers.IntegerField()
    # xxx = serializers.SerializerMethodField() # 自定义你想要显示的数据
    # tags = serializers.SerializerMethodField()

    depart = D1()
    tags = TagsSerializer(many=True) # 多对多关联，需要指定many=True

    class Meta:
        model = User
        # fields = "__all__" # 正常被序列化
        fields = ["name", "age", "gender","depart", "ctime", "xx", "tags"] # 指定序列化的字段
    def get_xxx(self, obj):
        return "{}-{}".format(obj.name, obj.age)

    def get_tags(self, obj):
        # [Tag对象, Tag对象, Tag对象]
        tag_list = obj.tags.all()
        print(tag_list)
        return [ {"id": row.id, "caption": row.caption} for row in tag_list]

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