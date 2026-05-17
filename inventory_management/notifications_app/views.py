from django.shortcuts import render
from .models import Notification


def notification_list(request):

    notifications = Notification.objects.all().order_by('-created_at')

    return render(

        request,

        'notifications/notification_list.html',

        {

            'notifications': notifications

        }
    )