from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Chat, ChatMessage

# Create your views here.

@login_required
def chats(request):
    chats = request.user.chats.all()

    return render(request, 'chat/chats.html', {'chats':chats})