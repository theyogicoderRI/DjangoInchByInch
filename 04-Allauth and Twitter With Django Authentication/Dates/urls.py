from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('', include('date_track.urls')),
    path('admin/', admin.site.urls),

    path('accounts/', include('allauth.urls')), # add for allauth
]


