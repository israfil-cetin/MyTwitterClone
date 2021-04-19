import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Cik
@login_required
def api_add_cik(request):
    data = json.loads(request.body)
    body = data['body']

    cik = Cik.objects.create(body=body,created_by=request.user)

    return JsonResponse({'success': True})