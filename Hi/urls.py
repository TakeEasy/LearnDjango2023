from django.contrib import admin
from django.urls import path
import views

urlpatterns = [
    path('HiAdmin/', views.index,name='index'),
    path('ab_json/',views.ab_json),
    path('fileuploads/',views.fileuploads),
    path('filters/',views.filters)

]