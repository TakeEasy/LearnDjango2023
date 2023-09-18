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


class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    """
    book publish 一对多 外键放在多的一边
    """
    publish = models.ForeignKey(to='Publish', on_delete=models.CASCADE)  # 默认和主键字段做关联 to_Field可以设置 ForeignKey 会自动加_id后缀
    """
    book author 多对多 外键在任何一边都可以 推荐建在查询频率高的一边
    """
    authors = models.ManyToManyField(to='Author')  # authors是虚拟字段 主要表示多对多关系 orm 自动帮你创建中间表


class Publish(models.Model):
    name = models.CharField(max_length=255)
    add = models.CharField(max_length=255)


class Author(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    """
    Author AuthorDetail 一对一 外键建在任意一边都可 推荐建在查询频率高的一边
    """
    author_detail = models.OneToOneField(to='AuthorDetail',on_delete=models.CASCADE)


class AuthorDetail(models.Model):
    phone = models.BigIntegerField()
    addr = models.CharField(max_length=255)
