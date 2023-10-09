import datetime

from django.shortcuts import render, HttpResponse, redirect, reverse
from Library import models
from django.http import JsonResponse


# Create your views here.


def index(request):
    return render(request, 'Libraryindex.html', locals())
