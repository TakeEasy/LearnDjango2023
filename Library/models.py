from django.db import models

# Create your models here.


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