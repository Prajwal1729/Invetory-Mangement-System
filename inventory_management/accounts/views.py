from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
import re

from .forms import RegisterForm
from .models import CustomUser

from products.models import Product
from categories.models import Category

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer

def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        password = request.POST.get('password1')

        password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_]).{6,}$'
        phone = request.POST.get('phone')

        if not re.match(password_pattern, password):

            return JsonResponse({
                'status': 'error',
                'errors': {
                    'password1': [
                        'Password must contain uppercase, lowercase and special character'
                    ]
                }
            })

        if not phone.isdigit():

            return JsonResponse({
                'status': 'error',
                'errors': {
                    'phone': [
                        'Phone number must contain only digits'
                    ]
                }
            })

        if len(phone) != 10:

            return JsonResponse({
                'status': 'error',
                'errors': {
                    'phone': [
                        'Phone number must be exactly 10 digits'
                    ]
                }
            })
        if form.is_valid():

            form.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Registration successful'
            })

        return JsonResponse({
            'status': 'error',
            'errors': form.errors
        })

    form = RegisterForm()

    return render(request, 'accounts/register.html', {
        'form': form
    })


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        # Username Validation

        if not username:

            return JsonResponse({
                'status': 'error',
                'message': 'Username is required'
            })

        # Password Validation

        if not password:

            return JsonResponse({
                'status': 'error',
                'message': 'Password is required'
            })

        if len(password) < 6:

            return JsonResponse({
                'status': 'error',
                'message': 'Password must be at least 6 characters'
            })

        # Check User

        if not CustomUser.objects.filter(username=username).exists():

            return JsonResponse({
                'status': 'error',
                'message': 'User does not exist'
            })

        # Authenticate

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            refresh = RefreshToken.for_user(user)

            return JsonResponse({

                'status': 'success',
                'message': 'Login successful',

                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),

                'role': user.role,
                'redirect_url': '/dashboard/'
            })

        return JsonResponse({
            'status': 'error',
            'message': 'Invalid username or password'
        })

    return render(request, 'accounts/login.html')


@login_required
def profile_view(request):

    return render(request, 'accounts/profile.html')


def logout_view(request):

    logout(request)

    return redirect('login')



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_api(request):

    serializer = UserSerializer(request.user)

    return Response(serializer.data)

