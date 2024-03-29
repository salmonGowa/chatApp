import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name=self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name="chat_%s" % self.room_name

        #joining a room group

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

  

    def disconnect(self,close_code):
        #leaving a group chat
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

        
    def receive(self,text_data):
        text_data_json =json.loads(text_data)
        message=text_data_json["message"]

        self.send(text_data=json.dumps({"message":message}))    