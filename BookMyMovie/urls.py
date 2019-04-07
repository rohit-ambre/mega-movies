from django.urls import path,re_path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:m>', views.movie, name='movie'),
    path('theatre/<int:m>', views.theatre, name='theatre')

]