from rest_framework.response import Response
from rest_framework.views import APIView

class SuperNBView(APIView):
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