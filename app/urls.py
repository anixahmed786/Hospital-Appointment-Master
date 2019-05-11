from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail', views.detail, name='detail'),
    path('elements', views.elements, name='elements'),
    path('news', views.news, name='news'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('base', views.base, name='base'),
    path('test/', views.test, name='test'),
    path('appoinment/', views.appoinment, name='appoinment'),
    path('contact_doc/', views.contact_doc, name='contact_doc'),
]