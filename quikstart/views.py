from rest_framework.response import Response
from rest_framework.views import APIView

from ext.auth import HeaderAuthentication


# 注意：MyAuth类是自定义的认证类，用于用户认证， 如果要全局使用，需要在settings.py中配置，但是就不能定义在这里了，会造成循环引用
class LoginView(APIView):
    authentication_classes = [] # 不需要走认证
    def post(self, request, *args, **kwargs):
        self.dispatch()
        return Response("LoginView post")

class UserView(APIView):
    authentication_classes = [HeaderAuthentication,] # 需要走认证
    # def get(self, request, pk, name):
    def get(self, request, *args, **kwargs):
        # print(request.user) # 当前登录的用户 -> 匿名用户（源码DRF.request-> _not_authenticated）
        # print(request.auth)
        return Response("UserView get")


class OrderView(APIView):
    def get(self, request):
        print(request.user, request.auth)
        return Response("OrderView")