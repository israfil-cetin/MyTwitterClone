from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from .models import Cik

# Create your views here.

@login_required
def feed(request):
    userids = [request.user.id]

    for users in request.user.userprofile.follows.all():
        userids.append(users.user.id)

    ciks = Cik.objects.filter(created_by_id__in=userids)
    return render(request, 'feed/feed.html', {'ciks': ciks})