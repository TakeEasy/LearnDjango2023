import datetime

from django.db import models


# Create your models here.

"""
mysql 的原生操作 看数据库learnPython2023里面保存的查询 practiceSQL1
orm 的操作 看Hi.tests.py
"""

"""
orm中常用的字段和参数
AutoField
    主键字段 primary_key=True
CharField        varchar
    verbose_name 字段的可读名
    max_length 长度
IntegerField    int
BigIntegerField bigint
DecimalField
    max_digits=8
    decimal_places=2
EmailField   varchar(254)

DateField    date
DateTimeField   datetime
    auto_now: 每次修改数据更新时间
    auto_now_add: 每次创建时添加时间 后面不会改了

BooleanField   
    传布尔值 数据库里会存0/1 

TextField   
    该字段可以用来存大段内容 比如文章内容 没有字数限制
FileField 
    upload_to='/data' 给该字段传一个文件对象 会自动将文件保存到该目录下 然后存文件路径 
    
    
ForeignKey(unique=True) === OneToOneField()  django推荐使用后面
    to_field 默认链接主键
    on_delete 关联删除行为 
"""

"""
django 还支持自定义字段
"""


class MyCharField(models.Field):
    def __int__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        super().__init__(max_length, *args, **kwargs)

    def db_type(self, connection):
        return 'char(%s)' % self.max_length


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

    gender_choices = (
        (1, '男'),
        (2, '女'),
        (3, '其他')
    )
    """
    user_obj.get_getnder_display()
    """
    gender = models.IntegerField(choices=gender_choices, default=1)

    info = models.CharField(max_length=255, verbose_name='个人介绍', null=True)
    hobby = models.CharField(max_length=255, verbose_name='爱好', default='reading')
    register_time = models.DateTimeField(auto_now_add=True)
    """
    DateFieldmi
    DateTImeField
        两个重要参数
        auto_now: 每次操作数据的时候 该字段会自动将当前时间更新
        auto_now_add: 在创建数据的时候会自动将当前时间输入
    """

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
    kucun = models.IntegerField(default=10000)
    maichu = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now_add=True)
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
    email = models.EmailField()  # 该字段不是给models看的 而是后面校验性组件看的


class Author(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    """
    Author AuthorDetail 一对一 外键建在任意一边都可 推荐建在查询频率高的一边
    """
    author_detail = models.OneToOneField(to='AuthorDetail', on_delete=models.CASCADE)


class AuthorDetail(models.Model):
    phone = models.BigIntegerField()  # 或者直接用charField
    addr = models.CharField(max_length=255)
