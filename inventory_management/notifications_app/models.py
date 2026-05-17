from django.db import models
from accounts.models import CustomUser


class Notification(models.Model):

    NOTIFICATION_TYPES = (

        ('LOW_STOCK', 'Low Stock'),
        ('OUT_OF_STOCK', 'Out Of Stock'),
        ('ORDER', 'Order'),
        ('SUPPLIER', 'Supplier'),
        ('STOCK', 'Stock'),

    )

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    title = models.CharField(
        max_length=255
    )

    message = models.TextField()

    notification_type = models.CharField(
        max_length=50,
        choices=NOTIFICATION_TYPES
    )

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.title