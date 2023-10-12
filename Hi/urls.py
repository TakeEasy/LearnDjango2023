from django.contrib import admin
from django.urls import path
from Hi import views

urlpatterns = [
    path('HiAdmin/', views.index, name='index'),
    path('ab_json/', views.ab_json),
    path('fileuploads/', views.fileuploads),
    path('filters/', views.filters),
    # Form 组件
    path('ab_form/', views.ab_form, name='ab_form'),
    path('ab_formclass/', views.ab_formclass, name='ab_formclass')

]
