from asgiref.sync import async_to_sync
import json
from channels.generic.websocket import WebsocketConsumer


class TestConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_name = 'test_hotelrecsys'

    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name,
            self.channel_name
        )

    def notice(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message
        }))
