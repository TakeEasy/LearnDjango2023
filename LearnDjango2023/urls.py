"""
URL configuration for LearnDjango2023 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from Hi import views
# from Hi import urls as Hi_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    # 登陆功能
    path('login/', views.login),
    path('register/', views.reg),
    path('userlist/', views.userlist),
    path('edituser/', views.edituser),
    path('deleteuser/', views.deleteuser),
    path('bibable/<int:a>/<int:b>/<int:c>/', views.bibable, name='bibale'),
    #path('hi/', include(Hi_urls))
    path('hi/', include('Hi.urls'))
]
