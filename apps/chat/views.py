from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Chat, ChatMessage
from django.contrib.auth.models import User


# Create your views here.

@login_required
def chats(request):
    chats = request.user.chats.all()

    return render(request, 'chat/chats.html', {'chats': chats})


@login_required
def chat(request, user_id):
    chats = Chat.objects.filter(users__in=[request.user.id])
    chats = chats.filter(users__in=[user_id])

    if chats.count() == 1:
        chat = chats[0]
    else:
        recipient = User.objects.get(pk=user_id)
        chat = Chat.objects.create()
        chat.users.add(request.user)
        chat.users.add(recipient)
        chat.save()
    return render(request, 'chat/chat.html', {'chat': chat})
