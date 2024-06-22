
from rest_framework.permissions import BasePermission
import random
from quikstart.models import UserInfo

class MyPermission(BasePermission):
    def has_permission(self, request, view):
        # 获取请求中的数据,校验....
        if request.user.is_authenticated:
            user = UserInfo.objects.get(user=request.user)
            if user.role == 'admin':
                return True
            else:
                return False
        else:
            return False
