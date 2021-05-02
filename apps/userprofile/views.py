from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def userprofile(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user': user
    }
    return render(request, 'userprofile/userprofile.html', context)

@login_required
def follow_user(request, username):
    user = get_object_or_404(User, username=username)

    request.user.userprofile.follows.add(user.userprofile)

    return redirect('userprofile', username=username)

@login_required
def unfollow_user(request, username):
    user = get_object_or_404(User, username=username)

    request.user.userprofile.follows.remove(user.userprofile)

    return redirect('userprofile', username=username)

def followers(request, username):
    user = get_object_or_404(User, username=username)

    context = {
        'user': user
    }
    return render(request, 'userprofile/followers.html', context)

def follows(request, username):
    user = get_object_or_404(User, username=username)

    context = {
        'user': user
    }
    return render(request, 'userprofile/follows.html', context)