
from rest_framework.permissions import BasePermission
import random
from quikstart.models import UserInfo

class UserPermission(BasePermission):
    code = 403
    message = {'status': False, 'msg': '无权访问'} # 自定义错误信息
    def has_permission(self, request, view):
        # 获取请求中的数据,校验....
        if request.user.role == 1:
            return True
        return True

class ManagerPermission(BasePermission):
    message = {'status': False, 'msg': '无权访问'} # 自定义错误信息
    def has_permission(self, request, view):
        # 获取请求中的数据,校验....
        if request.user.role == 2:
            return True
        return True

class BossPermission(BasePermission):
    message = {'status': False, 'msg': '无权访问'} # 自定义错误信息
    def has_permission(self, request, view):
        # 获取请求中的数据,校验....
        if request.user.role == 1:
            return True
        return True

# class MyPermission3(BasePermission):
#     message = {'status': False, 'msg': '无权访问'} # 自定义错误信息
#     def has_permission(self, request, view):
#         # 获取请求中的数据,校验....
#         print("MyPermission3")
#         return True