"""movieratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from movieratings_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^accounts/dashboard/$', views.dashboard, name='dashboard'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^accounts/profile/delete_entry/$', views.delete_entry, name="delete_entry"),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^movie_detail/', views.movie_detail, name="movie_detail"),
    url(r'^top_20_movies/', views.top_20_movies, name="top_20_movies"),
    url(r'^admin/', admin.site.urls),
    url(r'^top_5_unseen/', views.top_5_unseen, name="top_5_unseen")
]
