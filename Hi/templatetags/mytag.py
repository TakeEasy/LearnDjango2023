# 自定义 过滤器 必须在templatetags文件下 任意py文件 写上下面这两句
from django import template

register = template.Library()


# 自定义过滤器 最多两个参数 前后
@register.filter(name='baby')
def my_sum(v1, v2):
    return v1 + v2


# 自定义标签 任意多参数
@register.simple_tag(name='plus')
def index(a, b, c, d):
    return '%s-%s-%s-%s' % (a, b, c, d)


# 自定义inclusion_tag
"""
内部原理
    先定义一个方法
    在页面上调用这个方法 可以传值
    该方法会生成一些数据然后传递给一个html页面
    之后将渲染好的结果放到调用的位置
"""


@register.inclusion_tag('userlist.html')
def userlist(n):
    user_list = {'username': 'year', 'age': 18, 'hobby': 'reading'}
    data_l = ['第{}个'.format(i) for i in range(n)]
    return locals()
    # return {'data_l':data_l}
