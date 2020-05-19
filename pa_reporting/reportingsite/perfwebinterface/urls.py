from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='<doctype>...'),
    path('home', views.home, name='<doctype>...'),
    path('results', views.results, name='performance-results'),
    path('compare', views.compare, name='performance-compare'),
    path('statistics', views.statistics, name='performance-statistics'),
    path('links', views.links, name='performance-links'),
    path('contact', views.contact, name='performance-contact'),
    path('about', views.about, name='performance-about'),
]
