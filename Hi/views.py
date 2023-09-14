from django.shortcuts import render, HttpResponse, redirect
from Hi import models


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
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #第一种增加
        #res = models.User.objects.create(username=username,password=password)
        #第二种增加
        userobj = models.User(username=username,password=password)
        userobj.save()
        #print(res)
    return render(request, 'register.html')
