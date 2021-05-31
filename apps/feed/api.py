import json
import re
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Cik, Like
from apps.notification.utilities import create_notification



@login_required
def api_add_cik(request):
    data = json.loads(request.body)
    body = data['body']

    cik = Cik.objects.create(body=body,created_by=request.user)

    results = re.findall("(^|[^@\w])@(\w{1,20})", body)

    for result in results:
        result = result[1]

        print(result)

        if User.objects.filter(username=result).exists() and result != request.user.username:
            create_notification(request, User.objects.get(username=result), 'mention')

    return JsonResponse({'success': True})

@login_required
def api_add_like(request):
    data = json.loads(request.body)
    cik_id = data['cik_id']

    if not Like.objects.filter(cik_id=cik_id).filter(created_by=request.user).exists():
        like = Like.objects.create(cik_id=cik_id, created_by=request.user)
        cik = Cik.objects.get(pk=cik_id)
        create_notification(request, cik.created_by, 'like')


    return JsonResponse({'success': True})