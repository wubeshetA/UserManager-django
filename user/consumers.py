# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class UserConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({"message": "you are connected!"}))

    async def disconnect(self, close_code):
        pass
    
    @classmethod
    async def user_updated(self, event):
        # Send a "user updated" message to the WebSocket
        await self.send(text_data=json.dumps({"message": "updated"}))
        
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print("message recieved: ", message)