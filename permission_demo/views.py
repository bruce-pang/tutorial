import uuid

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from ext.permission import UserPermission, ManagerPermission, BossPermission
from ext.request import MyRequest
from ext.view import SuperNBView
from permission_demo.models import UserInfo


# 注意：MyAuth类是自定义的认证类，用于用户认证， 如果要全局使用，需要在settings.py中配置，但是就不能定义在这里了，会造成循环引用
class LoginView(APIView):
    authentication_classes = [] # 不需要走认证
    permission_classes = [] # 不需要走权限
    def post(self, request, *args, **kwargs):
        # 1.接收用户提交的用户名和密码
        # print(request._request.body)
        # print(request.data)
        uname = request.data.get("username")
        pwd = request.data.get("password")
        # 2.校验用户名和密码
        user_obj = UserInfo.objects.filter(username=uname, password=pwd).first()
        if not user_obj:
            return Response({"code": 10000, "error": "用户名或密码错误"})
        # 3.生成token
        token = str(uuid.uuid4())
        # 4.保存token
        user_obj.token = token
        user_obj.save()
        return Response({"code": 10001, "data": token})

class UserView(APIView):
    #authentication_classes = [HeaderAuthentication,] # 需要走认证
    # def get(self, request, pk, name):
    def get(self, request, *args, **kwargs):
        print(request.user) # 当前登录的用户 -> 匿名用户（源码DRF.request-> _not_authenticated）
        print(request.auth)
        return Response("UserView get")

# class OrderView(APIView):
class OrderView(SuperNBView): # 继承自定义的视图类, 用于权限校验
    # 管理员,经理 可以访问
    permission_classes = [ManagerPermission, BossPermission ] # 应用在单个视图中
    def get(self, request):
        print(request.user, request.auth)
        return Response('order get')
    # def check_permissions(self, request): # 只能应用于局部的权限校验
    #     no_permission_objs = []
    #     for permission in self.get_permissions():
    #          if permission.has_permission(request, self):
    #              return
    #          else:
    #              no_permission_objs.append(permission)
    #     else:
    #         self.permission_denied(
    #                  request,
    #                  message=getattr(no_permission_objs[0], 'message', None),
    #                  code=getattr(no_permission_objs[0], 'code', None))

class AvatarView(SuperNBView):
    # 经理/员工 可以访问
    permission_classes = [UserPermission, ManagerPermission, BossPermission ] # 应用在单个视图中
    def get(self, request):
        print(request.user, request.auth)
        return Response('avatar get')
    def check_permissions(self, request): # 只能应用于局部的权限校验
        no_permission_objs = []
        for permission in self.get_permissions():
             if permission.has_permission(request, self):
                 return
             else:
                 no_permission_objs.append(permission)
        else:
            self.permission_denied(
                     request,
                     message=getattr(no_permission_objs[0], 'message', None),
                     code=getattr(no_permission_objs[0], 'code', None))


    def initialize_request(self, request, *args, **kwargs):
        # super().initialize_request(request, *args, **kwargs)
        parser_context = self.get_parser_context(request)

        return MyRequest( # 重写initialize_request方法，返回自定义的Request对象
            request,
            parsers=self.get_parsers(),
            authenticators=self.get_authenticators(),
            negotiator=self.get_content_negotiator(),
            parser_context=parser_context
        )