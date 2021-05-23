import json

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import ChatMessage

@login_required
def api_add_message(request):
    data = json.loads(request.body)
    content = data['content']
    conversation_id = data['chat_id']

    message = ChatMessage.objects.create(chat_id=conversation_id, content=content, created_by=request.user)


    return JsonResponse({'success': True})