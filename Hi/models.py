from django.db import models


# Create your models here.


class User(models.Model):
    # 由于一张表必须要有一个主键字段 并且一般都叫id
    # 所以orm当你不定义主键字段 就会默认帮你创建一个id的主键字段
    # 如果你想创建的表的主键字段没有想起别的名字  就可以省略
    id = models.AutoField(primary_key=True)
    # CharField必须要指定max_length参数 不指定直接报错
    # verbose_name 所有字段都可以设置 是对于字段的解释
    username = models.CharField(max_length=255, verbose_name='用户名')
    # password = models.IntegerField(null=True)
    password = models.CharField(max_length=64, verbose_name='密码', null=True)
    age = models.IntegerField(verbose_name="年龄", default=18)
    info = models.CharField(max_length=255, verbose_name='个人介绍', null=True)
    hobby = models.CharField(max_length=255, verbose_name='爱好', default='reading')

    def __str__(self):
        return f'{self.username}'

"""
    python.exe manage.py makemigrations     将操作记录在小本本上
    python.exe manage.py migrate 将操作真正同步到数据库里
    只要修改了models.py里的内容 想同步到数据库 就必须执行上面两个命令
"""
