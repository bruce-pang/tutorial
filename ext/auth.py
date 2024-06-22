from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from quikstart.models import UserInfo

class QueryParamsAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # 去做用户认证：
        # 1. 获取前端传递的token
        # 2. 校验token合法性
        # 3. 返回值
        # 3.1 如果合法，返回元组（用户，token） 认证成功 request.user = user,request.auth = token
        # 3.2 抛出异常 认证失败 -> 返回错误信息
        # 3.3 返回None 多个认证类 [类1, 类2, 类3] -> 类1认证返回None就会继续走类2认证，类2认证返回None就会继续走类3认证，最后都返回None就会返回 -> 匿名用户

        # /xxx/xxx/xxx/?token=123123123
        dj_res = request._request # Django的request
        #token = request._request.GET.get('token') # 通过Django的request获取token
        #token = request._request.GET["token"] # 通过Django的request获取token
        token = request.query_params.get("token") # 通过DRF的request获取token
        print("QueryParamsAuthentication token:", token)
        if not token:
            return
        user_obj = UserInfo.objects.filter(token=token).first()

        if user_obj:
            return (user_obj, token) #返回元组（用户，token）, request.user = user,request.auth = token
        # raise AuthenticationFailed("认证失败")
        #raise AuthenticationFailed({"code": 20000, "error": "认证失败"}) # 返回错误信息
        return

    def authenticate_header(self, request):
        # return 'Basic realm="API"' # 返回头部信息
        return 'Token'

class ParamAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get("token") # 从URL中获取token
        print(token)
        if not token:
            return
        user_obj = UserInfo.objects.filter(token=token).first()
        if user_obj:
            return (user_obj, token)  # 返回元组（用户，token）, request.user = user,request.auth = token
        # raise AuthenticationFailed("认证失败")
        # raise AuthenticationFailed({"code": 20000, "error": "认证失败"}) # 返回错误信息
        return

    def authenticate_header(self, request): # 认证失败默认返回的头部信息
        return 'Token'

class HeaderAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get("HTTP_AUTHORIZATION")
        print("HeaderAuthentication token:", token)
        if not token:
            return
        user_obj = UserInfo.objects.filter(token=token).first()

        if user_obj:
            return (user_obj, token)  # 返回元组（用户，token）, request.user = user,request.auth = token
        # raise AuthenticationFailed("认证失败")
        # raise AuthenticationFailed({"code": 20000, "error": "认证失败"}) # 返回错误信息
        return

    def authenticate_header(self, request):
        return 'Token'

class NotAuthentication(BaseAuthentication):
    def authenticate(self, request):
        raise AuthenticationFailed({"code": 20000, "error": "认证失败"})

    def authenticate_header(self, request):
        return 'Token'