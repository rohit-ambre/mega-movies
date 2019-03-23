"""Mega_Movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from BookMyMovie import views as BM_views
from Movies import views as M_views
from User import views as user_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',M_views.testredirect, name='test'),
    path('BookMovie/', include('BookMyMovie.urls')),
    path('Movies/', include('Movies.urls')),
    path('register/', user_view.register, name='register'),
    path('profile/', user_view.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='User/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='User/logout.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler404 = 'BookMyMovie.views.handler404'
handler500 = 'BookMyMovie.views.handler500'