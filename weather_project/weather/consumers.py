import json
from channels.generic.websocket import AsyncWebsocketConsumer
import requests
import asyncio

class WeatherConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.city = self.scope['url_route']['kwargs'].get('city', 'London')
        self.send_task = asyncio.create_task(self.send_weather())

    async def send_weather(self):
        api_key = "4d0166f3ea050e398272a82bebcb2ce4" 
        while True:
            resp = requests.get(
                f'https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={api_key}&units=metric')
            data = resp.json()
            await self.send(json.dumps(data))
            await asyncio.sleep(60)  # Fetch every 60s

    async def disconnect(self, close_code):
        self.send_task.cancel()
