from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Count,Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Category
from .forms import CategoryForm

@login_required
def category_list(request):
 
    search_query = request.GET.get('q', '').strip()
    status = request.GET.get('status', '')
 
    categories = Category.objects.annotate(
        product_count=Count('product')
    ).order_by('-id')
 
    if status:
        categories = categories.filter(status=status)
 
    if search_query:
        categories = categories.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
 
    paginator = Paginator(categories, 10)  # 10 categories per page
    page_number = request.GET.get('page', 1)
    categories = paginator.get_page(page_number)
 
    form = CategoryForm()
 
    return render(request, 'categories/category_list.html', {
        'categories': categories,
        'form': form,
        'search_query': search_query,
        'selected_status': status,
    })

def add_category(request):

    if request.method == 'POST':

        form = CategoryForm(request.POST)

        if form.is_valid():

            form.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Category added successfully'
            })

        return JsonResponse({
            'status': 'error',
            'errors': form.errors
        })

    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request'
    })


def update_category(request, id):

    category = get_object_or_404(Category, id=id)

    if request.method == 'POST':

        form = CategoryForm(
            request.POST,
            instance=category
        )

        if form.is_valid():

            form.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Category updated successfully'
            })

        return JsonResponse({
            'status': 'error',
            'errors': form.errors
        })


def delete_category(request, id):

    category = get_object_or_404(Category, id=id)

    category.delete()

    return JsonResponse({
        'status': 'success',
        'message': 'Category deleted successfully'
    })