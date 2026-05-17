from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    ROLE_CHOICES = (

        ('ADMIN', 'ADMIN'),
        ('STAFF', 'STAFF'),
        ('INVENTORY MANAGER', 'INVENTORY MANAGER')
    )

    role = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES,
        default='STAFF'
    )

    phone = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )