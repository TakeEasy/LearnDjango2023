import datetime

from django.shortcuts import render, HttpResponse, redirect, reverse
from Library import models
from django.http import JsonResponse


# Create your views here.


def index(request):
    return render(request, 'Libraryindex.html', locals())


def book_list(request):
    # 先查询出所有的书籍信息
    book_queryset = models.Book.objects.all()
    return render(request, 'booklist.html', locals())


def book_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_date = request.POST.get('publishdate')
        publish_id = request.POST.get('publish')
        authors_list = request.POST.getlist('authors')
        # 操作数据库
        # 书籍表
        book_obj = models.Book.objects.create(title=title, price=price, publish_date=publish_date,
                                              publish_id=publish_id)
        # 书籍与作者关系表
        book_obj.authors.add(*authors_list)
        # 跳转到书籍的展示页面
        """
        redirect 可以直接给url
        也可以写别名
        如果别名需要参数 必须使用reverse
        """
        return redirect('book_list')

    # 先获取当前系统钟所有的出版社信息和作者信息供人选择
    publish_queryset = models.Publish.objects.all()
    author_queryset = models.Author.objects.all()
    return render(request, 'bookadd.html', locals())


def book_edit(request, edit_id):
    edit_obj = models.Book.objects.filter(pk=edit_id).first()
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_date = request.POST.get('publishdate')
        publish_id = request.POST.get('publish')
        authors_list = request.POST.getlist('authors')

        models.Book.objects.filter(pk=edit_id).update(title=title, price=price, publish_date=publish_date,
                                                      publish_id=publish_id)
        # 改第三张关系表
        edit_obj.authors.set(authors_list)
        return redirect('book_list')
    publish_queryset = models.Publish.objects.all()
    author_queryset = models.Author.objects.all()
    return render(request, 'bookedit.html', locals())


def book_delete(request, delete_id):
    models.Book.objects.filter(pk=delete_id).delete()
    return redirect('book_list')
