from django.test import TestCase

# Create your tests here.
import os
import sys

'''
从manage.py 里copy一些起始代码 再加两行 可以做到单个文件测试一些后端代码
'''


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LearnDjango2023.settings')
    import django
    django.setup()

    # 在这里写 测试 代码 包括 import相关代码 应为必须要等django环境就绪之后才能运行
    from Hi import models
    # models.User.objects.all()

    # 增
    # res = models.User.objects.create(username='shenqing', password='123', age=18, info='enene', hobby='watching')
    # print(res)
    # user_obj = models.User(username='shenqing', password='123', age=18, info='enene', hobby='watching')
    # user_obj.save()

    # 删
    """
    pk就是主键字段 不需要知道主键字段具体叫什么
    """
    # res = models.User.objects.filter(pk=4, username='shenqing').delete()
    # print(res)
    # user_obj = models.User.objects.filter(pk=4).first()
    # user_obj.delete()

    # 修改
    # models.User.objects.filter(pk=4).update(username='shenqingnima')
    """
    get可以直接返回当前对象
    但是不推荐使用
        因为一旦不存在该方法会直接报错
        而filter则不会
    """
    # user_obj = models.User.objects.get(pk=4)
    # user_obj.username = 'shenqingnima'
    # user_obj.save()

    # 必知必会13条
    """
    1.all()  查询所有
    2.filter() 带有过滤条件的查询
    3.get()  直接拿数据对象 但是不存在直接报错
    4.first() 拿queryset的第一个
    5.last()  拿queryset的最后一个

    6.values() 可以指定获取的字段 select username,age from ... 返回 queryset 列表套字典
    """
    # res = models.User.objects.values('username', 'age')
    # print(res)
    """ 
    7.values_list() 返回 queryset 列表套元组
    """
    # res = models.User.objects.values_list('username', 'age')
    # print(res.query) 可以查看内部封装的sql语句 只能用于queryset对象
    """
    查看sql语句的方法二: 所有的sql语句都能查看 copy logging的配置到settings.py 以后会自动后台打印

    8.distinct() 去重 是一摸一样的数据 带主键永远不一样
    res = models.User.objects.values('username', 'age').distinct()
    print(res)

    9.order_by() 排序
    res = models.User.objects.order_by('age') 默认升序
    res = models.User.objects.order_by('-age') 加减号 降序

    10.reverse() 数据反转,前提是已经排过序了
    res = models.User.objects.all()
    res = models.User.objects.order_by('age').reverse()

    11.count() 统计当前数据的数量
    res = models.User.objects.all().count()
    print(res)

    12.exclude() 排除
    res = models.User.objects.exclude(username='shenqing')
    print(res)

    13.exists() 判断存在与否 一般不用 因为 filter之后就可以判断是否True
    res = models.User.objects.filter(pk=4).exists()
    print(res)
    """

    # 神奇的双下划线查询
    # 1 年龄大于35岁的用户
    # res = models.User.objects.filter(age__gt=35)
    # print(res)
    # 2 年龄小于35
    # res = models.User.objects.filter(age__lt=35)
    # print(res)
    # 3 大于等于小于等于
    # res = models.User.objects.filter(age__gte=32)
    # print(res)

    # # 4 年龄是18 或者32 或着40
    # res = models.User.objects.filter(age__in=[18, 32, 40])
    # print(res)
    # # 5 年龄再18到40之间的 顾头顾尾
    # res = models.User.objects.filter(age__range=[18, 40])
    # print(res)
    #
    # # 6 查询名字里含有n的数据 模糊查询
    # res = models.User.objects.filter(username__contains='s')
    # print(res)
    # # 7 是否区分大小写 默认区分 忽略大小写
    # res = models.User.objects.filter(username__icontains='s')
    # print(res)
    #
    # res = models.User.objects.filter(username__startswith='j')
    # res = models.User.objects.filter(username__endswith='j')
    #
    # # 8 查询出注册时间是 1月 数据
    # res = models.User.objects.filter(register_time__month='1')
    # res = models.User.objects.filter(register_time__year='2023')
    # print(res)

    # ---------------------------------------------------------------------------------------------------------------

    # # 一对多外键增删改查
    # # 增 1 直接写实际外键id
    # models.Book.objects.create(title='三国演义', price=18.88, publish_id=1)
    # # 增 2 用对象
    # publish_obj = models.Publish.objects.filter(pk=1).first()
    # models.Book.objects.create(title='红楼梦', price=18.88, publish=publish_obj)
    #
    # # 删除
    # models.Publish.objects.filter(pk=1).delete()  # 设定了级联删除
    #
    # # 修改
    # models.Book.objects.filter(pk=1).update(publish_id=2)
    # models.Book.objects.filter(pk=1).update(publish=publish_obj)

    #

    # # 多对多 增删改查 其实就是第三张关系表的增删改查
    #     # # 增 给book添加author
    #     # book_obj = models.Book.objects.filter(pk=1).first()
    #     # print(book_obj.authors)  # 类似你已经找到第三张关系表了
    #     # book_obj.authors.add(1, 2, 3)  # 多对多 你可以放多几个
    #     #
    #     # author_obj = models.Author.objects.filter(pk=1).first()
    #     # book_obj.authors.add(author_obj)  # 也可以直接add对象
    #     #
    #     # # 删除
    #     # book_obj.authors.remove(2)
    #     # author_obj = models.Author.objects.filter(pk=2).first()
    #     # book_obj.authors.remove(author_obj)  # 同样可以放多个
    #     #
    #     # # 改
    #     # book_obj = models.Book.objects.filter(pk=1).first()
    #     # book_obj.authors.set([1, 3])  # 必须传一个可迭代对象
    #     # book_obj.authors.set([author_obj])  # 同样可以传对象
    #     #
    #     # # 清空
    #     # book_obj.authors.clear()

    """
    正反向概念
    正向
        看外键字段在我手上 我查你 就是正向
    反向
        不在我手上 我查你 就是反向
        
        
    正向查询按字段
    反向查询按表名小写加_set
    """

    # 多表查询
    # 子查询 基于对象的跨表查询
    # 查询书主键1的出版社 正向
    """
    在书写orm语句的时候跟sql语句一样
    不要一句化写完 如果比较复杂 可以写一点看一点
    拿到结果是多个 就.all()
    """
    # book_obj = models.Book.objects.filter(pk=1).first()
    # res = book_obj.publish
    # print(res)
    # print(res.name)
    # print(res.add)
    # 查询book主键1的作者 正向
    # res = book_obj.authors    Hi.Author.None
    # res = book_obj.authors.all()
    # print(res)
    # 查询author shenqing的电话号码 正向
    # author_obj = models.Author.objects.filter(name='shenqing').filter()
    # res = author_obj.author_detail
    # print(res)
    # print(res.phone)
    # print(res.addr)

    """
    当查询结果有多个的时候 要加_set.all()
    只有一个的时候 就直接.
    """
    # 查询publish是。。出版社的书 反向
    # publish_obj = models.Publish.objects.filter(name='东方出版社').first()
    # res = publish_obj.book_set.all()
    # print(res)
    # # 查询Author是jason的Book 反向
    # author_obj = models.Author.objects.filter(name='jason').first()
    # res = author_obj.book_set.all()
    # print(res)
    # 查询电话号码是。。。的作者信息 反向
    # author_detail_obj = models.AuthorDetail.objects.filter(phone=110).first()
    # res = author_detail_obj.author
    # print(res.name)

    # # 联表查询 基于双下划线的跨表查询
    # # 查询jason的手机号 正向 一行
    # res = models.Author.objects.filter(name='jason').values('author_detail__phone')
    # print(res)
    # # 反向 不能用.Author 只能通过detail 反向查
    # res = models.AuthorDetail.objects.filter(author__name='jason').values('phone', 'author__name')  # filter里同样可以用__
    # # 查询book pk1 的publish和bookname 正向
    # res = models.Book.objects.filter(pk=1).values('publish__name', 'title')
    # print(res)
    # # 反向
    # res = models.Publish.objects.filter(book__pk=1).values('name', 'book__title')
    # print(res)
    # # 查询book pk1 的author name 正向
    # res = models.Book.objects.filter(pk=1).values('authors__name')
    # print(res)
    # # 反向
    # res = models.Author.objects.filter(book__pk=1).values('name')
    # print(res)
    #
    # #
    #
    # # 查询book PK1 的author的phone 正向
    # res = models.Book.objects.filter(pk=1).values('authors__author_detail__phone')
    # print(res)
    # # 反向
    # res = models.AuthorDetail.objects.filter(author__book__pk=1).values('phone')
    # print(res)
    """
    只要掌握正反向
    就可以用__进行无限跨表查询 就是无限 join表
    """


if __name__ == '__main__':
    main()
