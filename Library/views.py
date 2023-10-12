import datetime

from django.shortcuts import render, HttpResponse, redirect, reverse
from Library import models
from django.http import JsonResponse


# Create your views here.


def index(request):
    return render(request, 'Libraryindex.html', locals())


from utils.mypage import Pagination


def book_list(request):
    # 先查询出所有的书籍信息
    # book_queryset = models.Book.objects.all()
    # 想访问哪一页
    # book_list = models.Book.objects.all()
    # all_count = book_list.count()
    #
    # current_page = request.GET.get('page', 1)  # 如果没有 默认第一页
    # try:
    #     current_page = int(current_page)
    # except Exception:
    #     current_page = 1
    #
    # per_page_num = 10
    #
    # start_page = (current_page - 1) * per_page_num
    #
    # end_page = current_page * per_page_num
    #
    # page_count, more = divmod(all_count, per_page_num)
    # if more:
    #     page_count += 1
    #
    # html = ''
    # true_current_page = current_page
    # if current_page < 6:
    #     current_page = 6
    # range_end = current_page + 6
    # if current_page + 6 > end_page +1:
    #     range_end = end_page+1
    # for i in range(current_page - 5, range_end + 6):
    #     if true_current_page == i:
    #         html += '<li class="active"><a href="?page=%s">%s</a></li>' % (i, i)
    #     else:
    #         html += '<li><a href="?page=%s">%s</a></li>' % (i, i)
    #
    # book_queryset = models.Book.objects.all()[start_page:end_page]
    book_queryset = models.Book.objects.all()
    current_page = request.GET.get('page', 1)
    all_count = book_queryset.count()
    page_obj = Pagination(current_page=current_page, all_count=all_count)

    page_queryset = book_queryset[page_obj.start:page_obj.end]


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
    """
    前后端再用ajax交互的时候 后端通常给ajax返回一个字典格式的数据
    """
    if request.is_ajax():
        if request.method == 'POST':
            back_dict = {'code': 100, 'msg': ''}
            delete_id = request.POST.get('delete_id')
            models.Book.objects.filter(pk=delete_id).delete()
            back_dict['msg'] = '数据已经删除'
            return JsonResponse(back_dict)

    models.Book.objects.filter(pk=delete_id).delete()
    return redirect('book_list')
