from django.utils import timezone
from django.db import models

class Depart(models.Model):
    title = models.CharField(verbose_name='部门', max_length=50)
    order = models.IntegerField(verbose_name='排序', default=0)
    count = models.IntegerField(verbose_name='人数', default=0)

class Tag(models.Model):
    caption = models.CharField(verbose_name='标签', max_length=64)


class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(verbose_name='年龄', default=18)
    gender = models.SmallIntegerField(verbose_name='性别', choices=((0, '男'), (1, '女')))
    depart = models.ForeignKey(verbose_name='部门',to='Depart', on_delete=models.CASCADE) # 外键关联， on_delete=models.CASCADE表示删除关联数据时，关联数据也删除
    createtime = models.DateTimeField(verbose_name='创建时间',auto_now_add=True) # 创建时间
    updatetime = models.DateTimeField(verbose_name='更新时间',  default=timezone.now) # 更新时间

    tags = models.ManyToManyField(verbose_name='标签',to='Tag') # 多对多关联, 会自动创建中间表