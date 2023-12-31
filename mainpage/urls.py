from django.conf.urls.static import static
from django.urls import path
from mainpage import views
from metall import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('lestnicy/', views.stair, name='stair'),
    path('navesy/', views.shelter, name='shelter'),
    path('zabori/', views.fence, name='fence'),
    path('besedki/', views.pergola, name='pergola'),
    path('otzivi/', views.reviews, name='reviews'),
    path('projects/', views.projects, name='projects'),
    path('contacts/', views.contacts, name='contacts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)