from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import include


def index(request) :
    return HttpResponse('<h1>咖啡</h1>')

