from django.urls import path
from .views import profile_api

urlpatterns = [
    path('profile/', profile_api),
]