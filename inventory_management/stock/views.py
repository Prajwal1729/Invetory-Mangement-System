from django.http import JsonResponse
from .forms import StockTransactionForm
from django.shortcuts import render
from .models import StockTransaction
from notifications_app.utils import create_notification
from accounts.decorators import role_required

@role_required(['ADMIN', 'INVENTORY MANAGER'])
def manage_stock(request):

    if request.method == 'POST':

        form = StockTransactionForm(request.POST)

        if form.is_valid():

            stock = form.save(commit=False)

            product = stock.product
            quantity = stock.quantity

            # STOCK IN
            if stock.transaction_type == 'IN':

                product.quantity += quantity

            # STOCK OUT
            elif stock.transaction_type == 'OUT':

                # Prevent negative stock
                if quantity > product.quantity:

                    return JsonResponse({
                        'status': 'error',
                        'message': f'Only {product.quantity} items available in stock'
                    })

                product.quantity -= quantity

            # LOW STOCK WARNING
            low_stock_warning = False

            if product.quantity <= product.minimum_stock_level:
                low_stock_warning = True

                create_notification(
                    user=request.user,
                    title='Low Stock Alert',
                    message=f'{product.product_name} stock is low.',
                    notification_type='LOW_STOCK'
                )

            # OUT OF STOCK
            if product.quantity == 0:
                product.product_status = 'Inactive'

                create_notification(
                    user=request.user,
                    title='Out Of Stock',
                    message=f'{product.product_name} is out of stock.',
                    notification_type='OUT_OF_STOCK'
                )

            else:

                product.product_status = 'Active'

            product.save()

            # SAVE HISTORY
            stock.created_by = request.user
            stock.save()

            message = 'Stock updated successfully'

            if low_stock_warning:

                message += ' | Warning: Low Stock Alert'

            return JsonResponse({
                'status': 'success',
                'message': message
            })

        return JsonResponse({
            'status': 'error',
            'errors': form.errors
        })

    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request'
    })

@role_required(['ADMIN', 'INVENTORY MANAGER'])
def stock_history(request):

    stock_logs = StockTransaction.objects.select_related(
        'product',
        'created_by'
    ).order_by('-created_at')

    context = {
        'stock_logs': stock_logs
    }

    return render(
        request,
        'stock/stock_history.html',
        context
    )