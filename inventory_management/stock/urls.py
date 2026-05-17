from django.urls import path
from .views import *

urlpatterns = [

    path(
        'manage/',
        manage_stock,
        name='manage_stock'
    ),
    path(
    'history/',
    stock_history,
    name='stock_history'
),

]