from django.urls import path
from .views import *

urlpatterns = [

    path(
        '',
        notification_list,
        name='notification_list'
    ),
    path(
        'read/<int:id>/',
        mark_as_read,
        name='mark_as_read'
    ),

]