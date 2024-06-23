from django.db import models

class UserInfo(models.Model):
    """
    用户信息表
    """
    username = models.CharField(verbose_name="用户名",max_length=32)
    password = models.CharField(verbose_name="密码",max_length=64)
    # 临时方式、JWT
    token = models.CharField(verbose_name="token",max_length=64, null=True, blank=True)
    role = models.IntegerField("角色", choices=((1, "普通用户"), (2, "VIP"), (3, "SVIP")), default=1)
