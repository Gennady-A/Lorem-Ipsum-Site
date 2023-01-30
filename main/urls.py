from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('Lorem_Ipsum', views.lorem_ipsum, name='LoremIpsum'),
    path('Rus', views.rusLI, name='Rus'),
    path('Eng', views.engLI, name='Eng'),
    path('Dan', views.danLI, name='Dan'),
    path('Deu', views.deuLI, name='Deu'),
]