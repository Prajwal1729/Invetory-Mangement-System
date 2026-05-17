from django.db import models
from products.models import Product
from accounts.models import CustomUser


class StockTransaction(models.Model):

    TRANSACTION_TYPE = (
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPE
    )

    quantity = models.PositiveIntegerField()

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.product.product_name} - {self.transaction_type}"
    

