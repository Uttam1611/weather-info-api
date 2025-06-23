from django.urls import path
from .views import WeatherHistoryView, WeatherView, home

urlpatterns = [
    path('weather/', WeatherView),
    path('history/', WeatherHistoryView.as_view()),
    path('', home), 
]