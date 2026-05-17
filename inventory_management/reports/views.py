from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
from stock.models import StockTransaction
from orders.models import Order
from suppliers.models import Supplier

import openpyxl

from reportlab.pdfgen import canvas


def reports_dashboard(request):

    # Low Stock

    low_stock_products = Product.objects.filter(
        quantity__lte=10
    )

    # Most Sold Products

    most_sold_products = Product.objects.order_by(
        '-quantity'
    )[:10]

    # Recent Stock Activity

    recent_stock_activity = StockTransaction.objects.order_by(
        '-created_at'
    )[:10]

    # Supplier Wise Inventory

    suppliers = Supplier.objects.all()

    context = {

        'low_stock_products': low_stock_products,

        'most_sold_products': most_sold_products,

        'recent_stock_activity': recent_stock_activity,

        'suppliers': suppliers,
    }

    return render(
        request,
        'reports/reports_dashboard.html',
        context
    )


# Export PDF

def export_pdf_report(request):

    response = HttpResponse(
        content_type='application/pdf'
    )

    response[
        'Content-Disposition'
    ] = 'attachment; filename="inventory_report.pdf"'

    p = canvas.Canvas(response)

    p.setFont("Helvetica-Bold", 16)

    p.drawString(
        200,
        800,
        "Inventory Report"
    )

    y = 760

    products = Product.objects.all()

    for product in products:

        p.setFont("Helvetica", 12)

        p.drawString(
            50,
            y,
            f"{product.product_name} | Qty: {product.quantity} | Price: {product.price}"
        )

        y -= 20

    p.showPage()

    p.save()

    return response


# Export Excel

def export_excel_report(request):

    workbook = openpyxl.Workbook()

    worksheet = workbook.active

    worksheet.title = "Inventory Report"

    headers = [
        'Product Name',
        'SKU',
        'Category',
        'Supplier',
        'Price',
        'Quantity',
        'Status'
    ]

    worksheet.append(headers)

    products = Product.objects.all()

    for product in products:

        worksheet.append([

            product.product_name,

            product.product_sku,

            product.category.name,

            product.supplier.supplier_name,

            str(product.price),

            product.quantity,

            product.product_status
        ])

    response = HttpResponse(
        content_type='application/ms-excel'
    )

    response[
        'Content-Disposition'
    ] = 'attachment; filename="inventory_report.xlsx"'

    workbook.save(response)

    return response