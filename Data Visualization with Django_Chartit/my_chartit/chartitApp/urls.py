from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sales', views.sales, name='sales'),
    path('weather', views.weather_chart_view, name='weather_chart_view'),
    path('citySales', views.citySales, name='citySales'),
    path('weatherByCity', views.weatherByCity, name='weatherByCity'),
    path('pivot', views.pivot, name='pivot'),
]
