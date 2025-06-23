# weather/views.py
from django.http import JsonResponse
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from django.shortcuts import render
from django.utils import timezone
from .models import WeatherRecord

def home(request):
    return render(request, 'index.html')

def WeatherView(request):
    city = request.GET.get('city')
    api_key = '4d0166f3ea050e398272a82bebcb2ce4' 

    # Fetch current weather
    current_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    current_data = requests.get(current_url).json()

    # Fetch 5-day/3-hour forecast
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"
    forecast_data = requests.get(forecast_url).json()

    hourly = forecast_data.get('list', [])[:8]  # next 24 hours

    return JsonResponse({"current": current_data, "hourly": hourly})

class WeatherHistoryView(APIView):
    def get(self, request):
        city = request.GET.get('city', 'London')
        records = WeatherRecord.objects.filter(city__iexact=city).order_by('-timestamp')[:10]
        data = [
            {
                "temp": r.temp,
                "humidity": r.humidity,
                "timestamp": r.timestamp
            } for r in records
        ]
        return Response(data)