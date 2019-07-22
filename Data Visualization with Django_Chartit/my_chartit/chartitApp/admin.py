from django.contrib import admin
from .models import SalesReport, MonthlyWeatherByCity, MonthlyWeatherSeattle, DailyWeather, Author, Publisher, Genre, Book, City, BookStore, SalesHistory

admin.site.register(SalesReport)
admin.site.register(MonthlyWeatherByCity)
admin.site.register(MonthlyWeatherSeattle)
admin.site.register(DailyWeather)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(City)
admin.site.register(BookStore)
admin.site.register(SalesHistory)
