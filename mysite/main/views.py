from django.shortcuts import render
from django.http import HttpResponse
from main import *


def index(request):
    return render(request, 'main/index.html')
