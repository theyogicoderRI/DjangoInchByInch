from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('admin/', admin.site.urls), # so we can get here from home page
    path('accounts/', include('allauth.urls')), # add for allauth
]


