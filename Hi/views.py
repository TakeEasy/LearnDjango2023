import datetime

from django.shortcuts import render, HttpResponse, redirect, reverse
from Hi import models
from django.http import JsonResponse

import json


# Create your views here.


def index(request):
    """

    :param request: 请求相关数据 比之前的env更加牛逼
    :return:
    """
    user_list = {"username": "Year", "age": 18, "hobby": "reading"}
    # return HttpResponse("你好哈 这是 Hi app")
    return render(request, 'first.html', {'data': user_list})  # 自动去templates文件夹查找
    # return render(request, 'first.html', locals())  # 自动去templates文件夹查找
    # return redirect("https://www.baidu.com/")


def login(request):
    """

    :param request:
    :return:
    """
    if request.method == "POST":
        print(request.POST)  # 获取用户提交的post请求的数据 不包括文件
        username = request.POST.get("username")  # 只会拿列表里的最后一个值
        password = request.POST.get("password")
        hobby = request.POST.getlist("hobby")
        # 不推荐使用索引取
        # userobj = models.User.objects.filter(username=username)[0]
        userobj = models.User.objects.filter(username=username).first()
        if userobj:
            if password == userobj.password:
                return HttpResponse("登陆成功!!")
            else:
                return HttpResponse("登陆失败!!")
        else:
            return HttpResponse("用户不存在!!")
        return render(request, 'login.html')
    # get请求携带数据最多4kB post 没有限制
    return render(request, 'login.html')


def reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 第一种增加
        # res = models.User.objects.create(username=username,password=password)
        # 第二种增加
        userobj = models.User(username=username, password=password)
        userobj.save()
        # print(res)
    return render(request, 'register.html')


def userlist(request):
    # data = models.User.objects.filter()
    user_queryset = models.User.objects.all()
    return render(request, 'userlist.html', locals())


def edituser(request):
    edit_id = request.GET.get('user_id')
    edit_obj = models.User.objects.filter(id=edit_id).first()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 修改数据放式1
        # models.User.objects.filter(id=edit_id).update(username=username,password=password)
        # 修改方式2
        """
            字段特别多的时候 效率非常低
            因为是从头到尾 所有字段全部重新赋值
        """
        edit_obj.username = username
        edit_obj.password = password
        edit_obj.save()
        return redirect('/userlist/')

    return render(request, 'useredit.html', locals())


def deleteuser(request):
    delete_id = request.GET.get('user_id')
    delete_obj = models.User.objects.filter(id=delete_id).first()

    models.User.objects.filter(id=delete_id).delete()

    return redirect('/userlist/')


def bibable(request, a, b, c):
    print(reverse('bibale', args=(1, 2, 3)))
    print(reverse('bibale', kwargs={'a': 1, 'b': 2, 'c': 3}))
    print(reverse('Hi:index'))
    return HttpResponse(f'{a},{b},{c}')


import json


def ab_json(request):
    user_dict = {'username': 'year帅帅帅', 'password': 123, 'hobby': 'reading'}
    l = [1, 2, 3, 45, 5]
    # json_str = json.dumps(user_dict,ensure_ascii=False)
    # return HttpResponse(json_str)
    # return JsonResponse(l,safe=False) 默认只能序列化字典,想序列化别的 需要加safe=False
    return JsonResponse(user_dict, json_dumps_params={'ensure_ascii': False})


def fileuploads(request):
    if request.method == 'POST':
        print(request.body)  # 原生的浏览器发过来的二进制数据
        print(request.POST)  # 获取普通数据 键值对
        print(request.FILES)  # 获取文件数据
        file_obj = request.FILES.get('file')
        print(file_obj.name)
        with open(file_obj.name, 'wb') as f:
            for line in file_obj.chunks():  # 推荐加上chunks方法,其实差不多
                f.write(line)

    print(request.path)  # 只能拿到访问请求的路由路径
    print(request.path_info)
    print(request.get_full_path())  # 包括?后面的参数 完整的url

    return render(request, 'fileuploads.html')


from django.views import View

"""
这种叫CBV class base view
跟FBV 各有千秋
"""


class MyLogin(View):  # urls里面配置 要写 views.MyLogin.as_view()
    def get(self, request):
        return HttpResponse("get 方法")

    def post(self, request):
        return HttpResponse("post 方法")


def filters(request):
    s = 'hahahahaha'
    file_size = 123123123
    current_time = datetime.datetime.now()
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    hhh = '<h1>我的乖乖</h1>'

    from django.utils.safestring import mark_safe
    hhh2 = '<h1>我的乖乖2</h1>'
    safe_hhh = mark_safe(hhh2)
    return render(request, 'filters.html', locals())


def ab_ajax(request):
    if request.method == "POST":
        print(request.POST)
        i1 = request.POST.get('i1')
        i2 = request.POST.get('i2')
        i3 = int(i1) + int(i2)
        print(i3)
        d = {'code': 100, 'msg': i3}
        # return HttpResponse(json.dumps(d))
        return JsonResponse(d)
    return render(request, 'ab_ajax.html')


def ab_file(request):
    if request.is_ajax():
        if request.method == 'POST':
            print(request.POST)
            print(request.FILES)
    return render(request, 'ab_file.html')


from django.core import serializers


def ab_ser(request):
    user_queryset = models.User.objects.all()
    # user_list = []
    # for user_obj in user_queryset:
    #     tmp = {
    #         'pk': user_obj.pk,
    #         'username': user_obj.username,
    #         'age': user_obj.age,
    #         'gender': user_obj.get_gender_display()
    #     }
    #     user_list.append(tmp)
    # return JsonResponse(user_list, safe=False)
    # return render(request, '')
    res = serializers.serialize('json', user_queryset)
    return HttpResponse(res)


def ab_pl(request):
    # for i in range(10000):
    #     models.Book.objects.create(title='第%s本书'%i)
    # book_queryset = models.Book.objects.all()
    book_list = []
    for i in range(10000):
        book_obj = models.Book(title='第%s本书' % i)
        book_list.append(book_obj)
    models.Book.objects.bulk_create(book_list)
    book_queryset = models.Book.objects.all()
    return render(request, '', locals())


def ab_form(request):
    back_dic = {'username': '', 'password': ''}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if 'aaa' in username:
            back_dic['username'] = '违规字符串'
        if len(password) < 3:
            back_dic['password'] = '密码长度小于3'
    return render(request, 'ab_form.html', locals())


from django import forms
from django.core.validators import RegexValidator


class MyForm(forms.Form):
    # initial 默认值
    # required 控制字段是否必填
    #
    username = forms.CharField(min_length=3, max_length=8, lable='用户名',
                               error_messages={
                                   'min_length': '用户名最少3位',
                                   'max_length': '用户名最长8位',
                                   'required': '必须要填'
                               },
                               widget=forms.TextInput(attrs={'class': 'form-control c1 c2', 'username': 'aaa'}))
    password = forms.CharField(min_length=3, max_length=8, widget=forms.EmailInput)
    confirm_password = forms.CharField(min_length=3, max_length=8, widget=forms.PasswordInput)
    email = forms.EmailField(label='邮箱',
                             error_messages={
                                 'invalid': '邮箱格式不正确'
                             })
    phone = forms.CharField(
        validators=[RegexValidator(r'^[0-9]+$', '请输入数字'),
                    RegexValidator(r'^186[0-9]+$', '数字必须以186开头')
                    ])
    gender = forms.ChoiceField(
        choices=((1, '男'), (2, '女')),
        label='性别',
        initial=3,
        widget=forms.RadioSelect()
    )

    # 钩子函数
    # 局部钩子 单个字段
    def clean_username(self):
        # 获取输入数据
        username = self.cleaned_data.get('username')
        if '666' in username:
            # 提示前端 展示错误信息
            self.add_error('username', '含有非法字段')
        # 将钩子函数勾出来的数据再放回去
        return username

    # 全局钩子
    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if not confirm_password == password:
            self.add_error('confirm_password', '两次密码不一致')
        # 所有数据再放回去
        return self.cleaned_data


# form_obj = MyForm({'username': 'aaaaaa', 'password': '123', 'email': 'asda'})
# # 数据有没有效
# form_obj.is_valid()
# # 有效的数据
# form_obj.cleaned_data
# # 哪些错误
# form_obj.errors
#
# # 多传直接忽略 也不影响
# # 默认情况下 数据是必须要填写

def ab_formclass(request):
    form_obj = MyForm()
    if request.method == 'POST':
        # 获取输入数据并校验
        form_obj = MyForm(request.POST)
        # 判断数据是否合法
        if form_obj.is_valid():
            # 如果合法 存储数据
            return HttpResponse('OK')
        else:
            # 展示错误信息到前端
            pass
    return render(request, 'ab_formclass.html', locals())


# 校验用户是否登陆的装饰器
def login_auth(func):
    def inner(request, *args, **kwargs):
        target_url = request.get_full_path()
        if request.COOKIES.get('username'):
            return func(request, *args, **kwargs)
        else:
            return redirect('/Hi/ab_login/?next=%s' % target_url)

    return inner


def ab_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'year' and password == '123':
            # 获取用户登陆前想访问的url
            target_url = request.GET.get('next')
            if target_url:
                obj = redirect(target_url)
            else:
                # 保存用户登陆状态
                obj = redirect('Hi/ab_home/')
            # 让浏览器记录cookie内容
            obj.set_cookie('username', 'year666', max_age=30)
            # obj.delete_cookie('username')
            # 浏览器不光会存 还会再后面访问中带上
            return obj
    return render(request, 'ab_login.html', locals())


def ab_home(request):
    # 获取cookie信息 判断有没有登陆
    if request.COOKIES.get('username') == 'year666':
        return render(request, 'ab_home.html', locals())

    return render(request, 'ab_login.html', locals())


def ab_session(request):
    # session 数据是保存在服务段的, 给客户端的是一串随机字符串
    # 默认情况下操作session 需要django默认的一张django_session表
    # 数据库迁移命令中会默认创建 默认session过期时间是14天 可以人为修改
    request.session['username'] = 'year666'
    request.session.set_expiry()
    # 括号内 四种参数
    # 1整数 多少秒
    # 2日期对象 到指定日期失效
    # 3 0 浏览器窗口关闭失效
    # 4 不写 取决于django默认的全局失效时间
    # 获取
    # username = request.session.get('username')
    # request.session.delete() #删除当前会话的所有session 只会删除服务端
    # request.session.flush() # 浏览器和服务端都清空


from django.utils.decorators import method_decorator

'''
CBV中Django不建议直接在类方法中加装饰器
'''


# @method_decorator(login_auth,name='get') 放式二
# @method_decorator(login_auth,name='post')
class MyLogin(View):
    @method_decorator(login_auth) # 放式三 会直接作用与当前类的所有方法
    def dispatch(self, request, *args, **kwargs):
        pass

    @method_decorator(login_auth)  # 放式一
    def get(self, request):
        return HttpResponse('')

    @method_decorator(login_auth)
    def post(self, request):
        return HttpResponse('')
