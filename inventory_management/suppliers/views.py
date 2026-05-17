from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator

from .models import Supplier
from .forms import SupplierForm


def supplier_list(request):
 
    search = request.GET.get('search', '').strip()
 
    suppliers = Supplier.objects.all().order_by('-id')
 
    if search:
        suppliers = suppliers.filter(
            supplier_name__icontains=search
        )
 
    paginator = Paginator(suppliers, 10)  # 10 suppliers per page
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
 
    form = SupplierForm()
 
    context = {
        'page_obj': page_obj,
        'form': form,
        'search': search,       
    }
 
    return render(
        request,
        'suppliers/supplier_list.html',
        context
    )

def add_supplier(request):

    if request.method == 'POST':

        form = SupplierForm(request.POST)

        if form.is_valid():

            form.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Supplier added successfully'
            })

        return JsonResponse({
            'status': 'error',
            'errors': form.errors
        })

    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request'
    })


def update_supplier(request, id):

    supplier = get_object_or_404(
        Supplier,
        id=id
    )

    if request.method == 'POST':

        form = SupplierForm(
            request.POST,
            instance=supplier
        )

        if form.is_valid():

            form.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Supplier updated successfully'
            })

        return JsonResponse({
            'status': 'error',
            'errors': form.errors
        })


def delete_supplier(request, id):

    if request.method == 'POST':

        supplier = get_object_or_404(
            Supplier,
            id=id
        )

        supplier.delete()

        return JsonResponse({
            'status': 'success',
            'message': 'Supplier deleted successfully'
        })

    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request'
    })