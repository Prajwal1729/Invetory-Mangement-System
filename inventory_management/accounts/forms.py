from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser

        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'phone',
            'role',
            'password1',
            'password2'
        ]

    def clean_email(self):

        email = self.cleaned_data.get('email')

        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Email already exists"
            )

        return email

    def clean_phone(self):

        phone = self.cleaned_data.get('phone')

        if len(phone) != 10:
            raise forms.ValidationError(
                "Phone number must be 10 digits"
            )

        return phone