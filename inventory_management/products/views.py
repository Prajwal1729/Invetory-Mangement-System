from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Update the import path below if your decorators.py is located elsewhere
# For example, if it's in the same directory as views.py, use:
# from .decorators import role_required
from notifications_app.utils import create_notification

from accounts.decorators import role_required

from .models import Product
from .forms import ProductForm

from categories.models import Category
from suppliers.models import Supplier

@login_required
@role_required(['ADMIN', 'INVENTORY MANAGER'])
def add_product(request):

    if request.method == 'POST':

        form = ProductForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            product = form.save(commit=False)

            product.created_by = request.user

            product.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Product added successfully'
            })

        print(form.errors)

        if product.quantity <= product.minimum_stock_level:
            create_notification(
                title='Low Stock Alert',
                message=f'{product.product_name} stock is low.',
                notification_type='LOW_STOCK',
                roles=['ADMIN', 'INVENTORY MANAGER']
            )

        return JsonResponse({
            'status': 'error',
            'errors': form.errors
        })

    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request'
    })


@csrf_exempt
@role_required(['ADMIN', 'INVENTORY MANAGER'])
def update_product(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    if request.method == 'POST':

        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product
        )

        if form.is_valid():

            form.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Product updated successfully'
            })
        
        if product.quantity <= product.minimum_stock_level:
            create_notification(
                title='Low Stock Alert',
                message=f'{product.product_name} stock is low.',
                notification_type='LOW_STOCK',
                roles=['ADMIN', 'INVENTORY MANAGER']
            )

        if product.quantity == 0:
            create_notification(
                title='Out Of Stock',
                message=f'{product.product_name} is out of stock.',
                notification_type='OUT_OF_STOCK',
                roles=['ADMIN', 'INVENTORY MANAGER']
            )

        return JsonResponse({
            'status': 'error',
            'errors': form.errors
        })

@role_required(['ADMIN', 'INVENTORY MANAGER'])
def delete_product(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    product.delete()

    return JsonResponse({
        'status': 'success',
        'message': 'Product deleted successfully'
    })

