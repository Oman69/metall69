from django.http import HttpResponse
from django.shortcuts import render
from mainpage.models import Stair,Shelter, Pergola, Fence
import random


def get_random_project(query_set):
    if len(query_set) > 0:
        return list(query_set)[random.randint(0, len(query_set)-1)]


def home(request):
    random_stair = get_random_project(Stair.objects.all())
    random_fence = get_random_project(Fence.objects.all())
    random_shelter = get_random_project(Shelter.objects.all())
    random_pergola = get_random_project(Pergola.objects.all())
    random_projects = [random_stair, random_fence, random_shelter, random_pergola]

    context = {
        'Random_projects': random_projects
    }
    return render(request, 'mainpage/home.html', context)


def stair(request):
    return render(request, 'mainpage/lestnicy.html')


def shelter(request):
    return HttpResponse('Навесы!')


def fence(request):
    return HttpResponse('Ограждение!')


def pergola(request):
    return HttpResponse('Беседки!')