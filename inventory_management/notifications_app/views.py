from django.shortcuts import render, redirect
from .models import Notification
from django.contrib.auth.decorators import login_required


@login_required
def notification_list(request):

    notifications = Notification.objects.filter(
        user=request.user
    )

    return render(
        request,
        'notifications/notification_list.html',
        {'notifications': notifications}
    )


@login_required
def mark_as_read(request, id):

    notification = Notification.objects.get(
        id=id,
        user=request.user
    )

    notification.is_read = True
    notification.save()

    return redirect('/notifications/')