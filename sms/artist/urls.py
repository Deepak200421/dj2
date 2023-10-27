"""
URL configuration for sms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.template.context_processors import static
from django.urls import path
from . import views

urlpatterns = [
    path('works/',views.myworks,name="artist/myworks"),
    path('',views.profile,name="artist/profile"),
    path('history/',views.history,name="artist/history"),
    path('climate/', views.climate,name='artist/climate'),
    path('hanees/', views.hanees, name="artist/hanees"),
    path('send_otp/', views.send_otp, name="artist_send_otp"),
    path('validate_otp/', views.validate_otp, name="artist_validate_otp"),
    path('list_persons', views.list_persons, name="artist/list_persons"),
    path("index/", views.home, name="artist/index"),
    path("payment/", views.order_payment, name="payment"),
    path("callback/", views.callback, name="callback"),

]












