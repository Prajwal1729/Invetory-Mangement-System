from django.urls import path

from .views import *


urlpatterns = [

    path(
        'add/',
        add_product,
        name='add_product'
    ),

    path(
        'delete/<int:id>/',
        delete_product,
        name='delete_product'
    ),

        path(
        'update/<int:id>/',
        update_product,
        name='update_product'
    ),
]