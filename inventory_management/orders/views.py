
import uuid
 
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
 
from .models import Order
from .forms import OrderForm
from products.models import Product
from notifications_app.utils import create_notification
from accounts.decorators import role_required


@role_required(['ADMIN'])
@login_required
def order_list(request):
 
    search = request.GET.get('search', '').strip()
    status = request.GET.get('status', '').strip()
 
    orders = Order.objects.all().order_by('-id')
 
    if search:
        orders = orders.filter(
            Q(order_number__icontains=search) |
            Q(supplier__supplier_name__icontains=search) |
            Q(product__product_name__icontains=search) |
            Q(created_by__username__icontains=search)
        )
 
    if status:
        orders = orders.filter(status=status)
 
    paginator = Paginator(orders, 10)  # 10 orders per page
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
 
    form = OrderForm()
 
    return render(request, 'orders/order_list.html', {
        'page_obj': page_obj,
        'form': form,
        'search': search,
        'selected_status': status,
    })


@role_required(['ADMIN'])
def create_order(request):

    if request.method == 'POST':

        form = OrderForm(request.POST)

        if form.is_valid():

            order = form.save(commit=False)

            product = Product.objects.get(
                id=request.POST.get('product')
            )

            quantity = int(request.POST.get('quantity'))

            order.order_number = f"ORD-{uuid.uuid4().hex[:6].upper()}"

            order.total_price = (
                product.price * quantity
            )

            order.created_by = request.user

            order.save()

            create_notification(
                title='New Order Created',
                message=f'Order #{order.id} has been created.',
                notification_type='ORDER_CREATED',
                roles=['ADMIN']
            )

            return JsonResponse({
                'status': 'success',
                'message': 'Order created successfully'
            })

        return JsonResponse({
            'status': 'error',
            'errors': form.errors
        })

@role_required(['ADMIN'])
def update_order_status(request, id):

    order = get_object_or_404(Order, id=id)

    if request.method == 'POST':

        new_status = request.POST.get('status')

        if order.status == 'Completed':

            return JsonResponse({
                'status': 'error',
                'message': 'Completed order cannot be modified'
            })

        if order.status == 'Completed' and new_status == 'Cancelled':

            return JsonResponse({
                'status': 'error',
                'message': 'Completed order cannot be cancelled'
            })

        order.status = new_status

        order.save()

        create_notification(
            title='Order Status Updated',
            message=f'Order {order.order_number} marked as {order.status}.',
            notification_type='ORDER_COMPLETED',
            roles=['ADMIN']
        )

        return JsonResponse({
            'status': 'success',
            'message': 'Order status updated successfully'
        })

    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request'
    })

@role_required(['ADMIN'])
def cancel_order(request, id):

    order = get_object_or_404(Order, id=id)

    if order.status == 'Completed':

        return JsonResponse({
            'status': 'error',
            'message': 'Completed order cannot be cancelled'
        })


    if order.status == 'Cancelled':
        return JsonResponse({
            'status': 'error',
            'message': 'Order already cancelled'
        })

    order.status = 'Cancelled'

    order.save()


    create_notification(
        title='Order Cancelled',
        message=f'Order {order.order_number} has been cancelled.',
        notification_type='ORDER_CREATED',
        roles=['ADMIN']
    )

    return JsonResponse({
        'status': 'success',
        'message': 'Order cancelled successfully'
    })