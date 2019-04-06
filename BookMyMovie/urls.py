from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:m>', views.movie, name='movie'),
    # path(r'^[0-9]/calender/$', views.calender, name='calender')

]