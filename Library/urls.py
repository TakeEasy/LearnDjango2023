from django.contrib import admin
from django.urls import path
from Library import views

urlpatterns = [
    path('LibraryAdmin/', views.index, name='admin'),
    path('index/', views.index, name='index'),
    path('book/list/', views.book_list, name='book_list'),
    path('book/add/', views.book_add, name='book_add'),
    path('book/edit/<int:edit_id>/', views.book_edit, name='book_edit'),
    path('book/delete/<int:delete_id>', views.book_delete,name='book_delete')
]
