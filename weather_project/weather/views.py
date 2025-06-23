# Create your views here.
import requests
from rest_framework.views import APIView
from rest_framework.response import Response

class WeatherView(APIView):
    def get(self, request):
        city = request.GET.get('city', 'London')
        api_key = '4d0166f3ea050e398272a82bebcb2ce4'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        resp = requests.get(url)
        data = resp.json()
        return Response(data)