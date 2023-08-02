from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'mainpage/home.html')


def stair(request):
    return HttpResponse('Лестницы!')


def shelter(request):
    return HttpResponse('Навесы!')


def fence(request):
    return HttpResponse('Ограждение!')


def pergola(request):
    return HttpResponse('Беседки!')