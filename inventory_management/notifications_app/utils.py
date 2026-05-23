from .models import Notification
from accounts.models import CustomUser


def create_notification(title, message, notification_type, roles=None):

    users = CustomUser.objects.all()

    if roles:
        users = users.filter(role__in=roles)

    notifications = []

    for user in users:

        notifications.append(

            Notification(
                user=user,
                title=title,
                message=message,
                notification_type=notification_type
            )
        )

    Notification.objects.bulk_create(notifications)