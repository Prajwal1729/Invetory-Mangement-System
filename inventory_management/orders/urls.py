from django.urls import path

from .views import *

urlpatterns = [

    path(
        '',
        order_list,
        name='order_list'
    ),

    path(
        'create/',
        create_order,
        name='create_order'
    ),

    path(
        'update-status/<int:id>/',
        update_order_status,
        name='update_order_status'
    ),

    path(
        'cancel/<int:id>/',
        cancel_order,
        name='cancel_order'
    ),
]