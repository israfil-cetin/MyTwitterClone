import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Cik, Like


@login_required
def api_add_cik(request):
    data = json.loads(request.body)
    body = data['body']

    cik = Cik.objects.create(body=body,created_by=request.user)

    return JsonResponse({'success': True})

@login_required
def api_add_like(request):
    data = json.loads(request.body)
    cik_id = data['cik_id']

    if not Like.objects.filter(cik_id=cik_id).filter(created_by=request.user).exists():
        like = Like.objects.created(cik_id=cik_id, created_by=request.user)



    return JsonResponse({'success': True})