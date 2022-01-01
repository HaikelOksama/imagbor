"""uas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from imabor.views import base_url, home_view, nature_view, space_view, building_view, animasi_view, dynamic_image_view, about_view, result_view, subtags_view

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', home_view, name='home'),
    path('images/', home_view, name='home'),
    path('nature/', nature_view, name='nature'),
    path('building/', building_view, name='building'),
    path('space/', space_view, name='space'),
    path('animasi/', animasi_view, name='animasi'),
    path('about/', about_view, name='about'),
    path('images/<int:my_id>/', dynamic_image_view, name='images_id'),
    path('subtag/<str:my_subtag>/', subtags_view, name='subtags'),
    path('result/', result_view, name='result'),
]
