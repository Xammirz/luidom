
from os import name
from django import views
from django.urls import path, include
from .views import IndexView,  AboutView, ContactView
urlpatterns = [   
    path('', IndexView.as_view(), name='index' ),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
