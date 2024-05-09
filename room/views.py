from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Room, Message


@login_required
def rooms(request):
    salas = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': salas})

@login_required
def room(request, slug):
    sala = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=sala)[0:100]

    return render(request, 'room/room.html', {'room': sala, 'messages': messages})
