from .models import Notification


def notifications(request):
    if request.user.is_authenticated:
        return {'notification': request.user.notifications.filter(is_read=False)}
    else:
        return {'notification': []}
