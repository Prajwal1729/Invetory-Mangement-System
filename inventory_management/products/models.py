import uuid

from django.db import models
from django.conf import settings

from categories.models import Category
from suppliers.models import Supplier


class Product(models.Model):

    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

    product_name = models.CharField(
        max_length=255
    )

    product_sku = models.CharField(
        max_length=100,
        unique=True,
        blank=True
    )

    product_image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True
    )

    description = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='product'
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    quantity = models.IntegerField()

    minimum_stock_level = models.IntegerField(
        default=5
    )

    barcode = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )

    product_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Active'
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):

        if not self.product_sku:
            self.product_sku = f"SKU-{uuid.uuid4().hex[:8].upper()}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name