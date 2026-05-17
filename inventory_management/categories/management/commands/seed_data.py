from django.core.management.base import BaseCommand

from categories.models import Category
from suppliers.models import Supplier


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        categories = [
            'Electronics',
            'Fashion',
            'Furniture',
            'Grocery'
        ]

        for category in categories:

            Category.objects.get_or_create(
                name=category,
                status='Active'
            )

        suppliers = [

            {
                'supplier_name': 'ABC Suppliers',
                'contact_person': 'Rahul',
                'email': 'abc@gmail.com',
                'phone_number': '9876543210',
                'address': 'Mumbai'
            },

            {
                'supplier_name': 'Global Traders',
                'contact_person': 'Amit',
                'email': 'global@gmail.com',
                'phone_number': '9876543211',
                'address': 'Pune'
            }
        ]

        for supplier in suppliers:

            Supplier.objects.get_or_create(
                email=supplier['email'],
                defaults=supplier
            )

        self.stdout.write(
            self.style.SUCCESS(
                'Default data added successfully'
            )
        )