from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import F, Q
from django.core.paginator import Paginator

from products.models import Product
from products.forms import ProductForm
from stock.models import StockTransaction
from categories.models import Category


@login_required
def dashboard_view(request):

    search_query = request.GET.get('q', '').strip()

    products_qs = Product.objects.all().order_by('-id')

    if search_query:
        products_qs = products_qs.filter(
            Q(product_name__icontains=search_query) |
            Q(product_sku__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(category__name__icontains=search_query) |
            Q(supplier__supplier_name__icontains=search_query) |
            Q(barcode__icontains=search_query)
        )

    paginator = Paginator(products_qs, 10)  # 10 products per page
    page_number = request.GET.get('page', 1)
    products = paginator.get_page(page_number)

    total_products = Product.objects.count()

    low_stock_products = Product.objects.filter(
        quantity__lte=F('minimum_stock_level'),
        quantity__gt=0
    ).count()

    out_of_stock_products = Product.objects.filter(
        quantity=0
    ).count()

    stock_history = StockTransaction.objects.select_related(
        'product', 'created_by'
    ).order_by('-created_at')[:10]

    total_categories = Category.objects.count()

    form = ProductForm()

    context = {
        'products': products,
        'total_products': total_products,
        'low_stock_products': low_stock_products,
        'out_of_stock_products': out_of_stock_products,
        'total_categories': total_categories,
        'form': form,
        'stock_history': stock_history,
        'search_query': search_query,
    }

    return render(request, 'dashboard/dashboard.html', context)