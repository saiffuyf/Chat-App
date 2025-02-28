from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def chat_room(request, user1, user2):
    return render(request, "chatUI.html", {"user1": user1, "user2": user2})

