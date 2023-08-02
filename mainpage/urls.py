from django.urls import path
from mainpage import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lestnicy/', views.stair, name='stair'),
    path('navesy/', views.shelter, name='shelter'),
    path('zabori/', views.fence, name='fence'),
    path('besedki/', views.pergola, name='pergola'),
]