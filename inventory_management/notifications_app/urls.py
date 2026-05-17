from django.urls import path
from .views import *

urlpatterns = [

    path(
        '',
        notification_list,
        name='notification_list'
    ),

]