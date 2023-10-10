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

