from django.urls import path

from . import views

urlpatterns = [
    path('',views.landing, name='landing'),
    path('<str:imdb>', views.display, name='display')
]