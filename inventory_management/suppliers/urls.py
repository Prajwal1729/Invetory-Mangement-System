from django.urls import path
from .views import *

urlpatterns = [

    path(
        '',
        supplier_list,
        name='supplier_list'
    ),

    path(
        'add/',
        add_supplier,
        name='add_supplier'
    ),

    path(
        'update/<int:id>/',
        update_supplier,
        name='update_supplier'
    ),

    path(
        'delete/<int:id>/',
        delete_supplier,
        name='delete_supplier'
    ),

]