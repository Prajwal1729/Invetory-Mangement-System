from django.db import models

class Supplier(models.Model):

    supplier_name = models.CharField(
        max_length=255
    )

    contact_person = models.CharField(
        max_length=255
    )

    email = models.EmailField(
        unique=True
    )

    phone_number = models.CharField(
        max_length=15
    )

    address = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.supplier_name