from django.urls import path
from .views import chat_room

urlpatterns = [
    path("chat/<str:user1>/<str:user2>/", chat_room, name="chat_room"),
]
