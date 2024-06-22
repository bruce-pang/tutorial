import uuid

from rest_framework.response import Response
from rest_framework.views import APIView
from quikstart.models import UserInfo
from ext.auth import HeaderAuthentication


# 注意：MyAuth类是自定义的认证类，用于用户认证， 如果要全局使用，需要在settings.py中配置，但是就不能定义在这里了，会造成循环引用
class LoginView(APIView):
    authentication_classes = [] # 不需要走认证
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
        # print(request.user) # 当前登录的用户 -> 匿名用户（源码DRF.request-> _not_authenticated）
        # print(request.auth)
        return Response("UserView get")


class OrderView(APIView):
    def get(self, request):
        print(request.user, request.auth)
        return Response("OrderView")