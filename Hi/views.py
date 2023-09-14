from django.shortcuts import render, HttpResponse, redirect


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
    if request.method=="GET":
        return render(request, 'login.html')

