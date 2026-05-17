from django.urls import path
from .views import *

urlpatterns = [

    path(
        '',
        category_list,
        name='category_list'
    ),

    path(
        'add/',
        add_category,
        name='add_category'
    ),

    path(
        'update/<int:id>/',
        update_category,
        name='update_category'
    ),

    path(
        'delete/<int:id>/',
        delete_category,
        name='delete_category'
    ),
]