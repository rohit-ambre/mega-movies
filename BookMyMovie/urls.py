from django.urls import path,re_path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:m>', views.movie, name='movie'),
    path('theatre/<int:m>/<int:day>', views.theatre, name='theatre'),
    path('seat/<int:m>/<int:day>/<int:show>', views.seat, name='seat'),
    path('booking/<int:id>', views.booking, name='booking'),
    path('history/', views.history, name='history')

]