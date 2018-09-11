from django.conf.urls import url
from chat import Consumers

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', Consumers.ChatConsumer),
]
