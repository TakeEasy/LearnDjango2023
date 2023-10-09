from django.contrib import admin
from django.urls import path
from Hi import views

urlpatterns = [
    path('LibraryAdmin/', views.index,name='index'),
    path('index/',views.ab_json)

]