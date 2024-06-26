from django.conf.urls.static import static
from django.urls import path
from mainpage import views
from metall import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('lestnicy/', views.stair, name='stair'),
    path('lestnicy/karkasi/', views.stair, name='karkas'),
    path('lestnicy/na-monokosoure/', views.stair, name='mono'),
    path('lestnicy/na-kosourah/', views.stair, name='poli'),

    path('navesy/', views.shelter, name='shelter'),
    path('zabori/', views.fence, name='fence'),
    path('besedki/', views.pergola, name='pergola'),
    path('krylco/', views.porch, name='porch'),
    path('otzivi/', views.reviews, name='reviews'),
    path('projects/', views.projects, name='projects'),
    path('contacts/', views.contacts, name='contacts'),
    path('message/', views.send_email, name='message'),
    path('thanks/', views.thanks_page, name='thanks'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)