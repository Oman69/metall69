from django.http import HttpResponse
from django.shortcuts import render
from mainpage.models import Stair,Shelter, Pergola, Fence, ProjectVideo, ReviewVideo
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
    all_stairs = Stair.objects.all()
    return render(request, 'mainpage/lestnicy.html', {'Projects': all_stairs})


def shelter(request):
    all_shelters = Shelter.objects.all()
    return render(request, 'mainpage/navesy.html', {'Projects': all_shelters})


def fence(request):
    all_fence = Fence.objects.all()
    return render(request, 'mainpage/zabori.html', {'Projects': all_fence})


def pergola(request):
    all_pergolas = Pergola.objects.all()
    return render(request, 'mainpage/besedki.html', {'Projects': all_pergolas})


def reviews(request):
    review_videos = ReviewVideo.objects.all()
    return render(request, 'mainpage/otzivy.html', {'Videos': review_videos})

def projects(request):
    projects_videos = ProjectVideo.objects.all()
    return render(request, 'mainpage/projects.html', {'Videos': projects_videos})

def contacts(request):
    return render(request, 'mainpage/contacts.html')