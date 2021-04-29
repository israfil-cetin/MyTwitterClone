from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Cik


# Create your views here.

@login_required
def feed(request):
    userids = [request.user.id]

    for users in request.user.userprofile.follows.all():
        userids.append(users.user.id)

    ciks = Cik.objects.filter(created_by_id__in=userids)
    return render(request, 'feed/feed.html', {'ciks': ciks})


@login_required
def search(request):
    query = request.GET.get('query', '')

    if len(query) > 0:
        users = User.objects.filter(username__icontains=query)
    else:
        users = []
    context = {
        'query': query,
        'users': users,
    }
    return render(request, 'feed/search.html', context)