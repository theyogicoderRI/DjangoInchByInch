from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    #path('users/', include('django.contrib.auth.urls')), #remove this when using allauth

]